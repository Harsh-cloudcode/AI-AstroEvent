

import math
from datetime import datetime, timedelta

from fastapi import APIRouter, Query

from app.api.weather import get_weather
from app.api.sun import get_sun
from app.api.planets import get_planets
from app.api.deep_objects import get_deep_sky
from app.api.constellations import get_constellations
from app.api.meteor_showers import get_meteor_showers
from app.api.atronomical_events import get_astronomical_events

# 7Timer astronomical weather
try:
    from app.api.astro_weather import get_astro_weather
except Exception:
    get_astro_weather = None

from app.services.ai_recommendation import generate_recommendation


router = APIRouter()


# ============================================================
# BASIC HELPERS
# ============================================================

def safe_call(function, *args, **kwargs):
    """
    Safely execute an API/module function.

    If one astronomy module fails, the complete observation
    analysis should still continue.
    """
    try:
        return function(*args, **kwargs)

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "type": type(e).__name__,
        }


def first_not_none(*values):
    for value in values:
        if value is not None:
            return value

    return None


def get_list(data, keys=None):
    """
    Extract a list from different possible API response structures.
    """

    if data is None:
        return []

    if isinstance(data, list):
        return data

    if not isinstance(data, dict):
        return []

    if keys:
        for key in keys:
            value = data.get(key)

            if isinstance(value, list):
                return value

    for key in [
        "objects",
        "planets",
        "targets",
        "items",
        "results",
        "showers",
        "events",
        "data",
    ]:
        value = data.get(key)

        if isinstance(value, list):
            return value

    return []


def normalize_object(item):
    """
    Convert arbitrary astronomy object data into a dictionary.
    """

    if isinstance(item, dict):
        return dict(item)

    return {
        "name": str(item)
    }


def normalize_list(items):
    return [
        normalize_object(item)
        for item in items
        if item is not None
    ]


# ============================================================
# OBJECT NAME EXTRACTION
# ============================================================

def clean_name(value):
    """
    Convert a possible name value into a clean string.

    Handles:
        string
        number
        nested dictionary
        enum-like objects
    """

    if value is None:
        return None

    if isinstance(value, str):
        value = value.strip()

        if value:
            return value

        return None

    if isinstance(value, (int, float)):
        return str(value)

    # Enum-like object
    enum_name = getattr(value, "name", None)

    if isinstance(enum_name, str) and enum_name.strip():
        return enum_name.strip()

    enum_value = getattr(value, "value", None)

    if isinstance(enum_value, str) and enum_value.strip():
        return enum_value.strip()

    if isinstance(value, dict):

        # Most common nested name fields
        for key in [
            "name",
            "display_name",
            "object_name",
            "target_name",
            "planet_name",
            "shower_name",
            "constellation_name",
            "body_name",
            "title",
            "label",
            "text",
            "value",
            "code",
            "id",
        ]:

            nested = value.get(key)

            result = clean_name(nested)

            if result:
                return result

    return None


def get_object_name(item):
    """
    Robust astronomy object name extraction.

    Supports data from:

        Astronomy Engine
        SpaceCatalog
        MeteorShowerCal
        custom astronomy modules

    Important fields include:

        name
        body
        planet
        target
        object
        constellation
        shower
        planet_name
        shower_name
        constellation_name
        etc.
    """

    if item is None:
        return "Unknown object"

    # Direct string
    if isinstance(item, str):

        value = item.strip()

        return value if value else "Unknown object"

    # Enum-like object
    if not isinstance(item, dict):

        result = clean_name(item)

        return result if result else "Unknown object"

    # --------------------------------------------------------
    # DIRECT NAME FIELDS
    # --------------------------------------------------------

    direct_keys = [
        "name",
        "object_name",
        "objectName",
        "target_name",
        "targetName",

        "display_name",
        "displayName",

        "planet_name",
        "planetName",

        "shower_name",
        "showerName",

        "constellation_name",
        "constellationName",

        "deep_sky_name",
        "deepSkyName",

        "body_name",
        "bodyName",

        "designation",

        "title",
        "label",
        "text",
    ]

    for key in direct_keys:

        if key not in item:
            continue

        result = clean_name(item.get(key))

        if result:
            return result

    # --------------------------------------------------------
    # ASTRONOMY ENGINE / OBJECT FIELDS
    # --------------------------------------------------------

    nested_object_keys = [
        "body",
        "planet",
        "target",
        "object",
        "constellation",
        "shower",
        "body_name",
        "bodyName",
    ]

    for key in nested_object_keys:

        if key not in item:
            continue

        value = item.get(key)

        result = clean_name(value)

        if result:
            return result

    # --------------------------------------------------------
    # METEOR SHOWER IDENTIFIERS
    # --------------------------------------------------------

    for key in [
        "shower_code",
        "iau_code",
        "iauCode",
        "abbr",
        "abbreviation",
        "code",
        "id",
    ]:

        result = clean_name(item.get(key))

        if result:
            return result

    # --------------------------------------------------------
    # CONSTELLATION IDENTIFIERS
    # --------------------------------------------------------

    for key in [
        "constellation_id",
        "constellation_code",
        "constellation_abbr",
        "iau",
        "iau_abbreviation",
    ]:

        result = clean_name(item.get(key))

        if result:
            return result

    # --------------------------------------------------------
    # NESTED DATA
    # --------------------------------------------------------

    for key in [
        "data",
        "result",
        "details",
        "info",
        "metadata",
    ]:

        value = item.get(key)

        if isinstance(value, dict):

            result = get_object_name(value)

            if result != "Unknown object":
                return result

    # --------------------------------------------------------
    # FINAL FALLBACK
    # --------------------------------------------------------

    # Sometimes an object contains one useful string field
    # that was not covered above.

    ignored_keys = {
        "visible",
        "observability",
        "difficulty",
        "recommendation",
        "description",
        "altitude",
        "azimuth",
        "rise",
        "set",
        "rise_time",
        "set_time",
        "best_time",
        "transit",
        "magnitude",
        "distance",
    }

    for key, value in item.items():

        if key in ignored_keys:
            continue

        result = clean_name(value)

        if result:
            return result

    return "Unknown object"


# ============================================================
# OBJECT TYPE
# ============================================================

def add_object_type(item, object_type):
    """
    Add a predictable type for frontend / AI usage.
    """

    result = dict(item)

    result["type"] = object_type

    return result


# ============================================================
# VISIBILITY NORMALIZATION
# ============================================================

def normalize_visibility(item):
    """
    Preserve source visibility if present.

    We do NOT invent astronomical visibility.
    """

    result = dict(item)

    visible = result.get("visible")

    if isinstance(visible, bool):
        return result

    observability = result.get("observability")

    if isinstance(observability, str):

        value = observability.lower()

        if "not visible" in value:
            result["visible"] = False

        elif "below horizon" in value:
            result["visible"] = False

        elif "unobservable" in value:
            result["visible"] = False

        elif "visible" in value:
            result["visible"] = True

        elif "observable" in value:
            result["visible"] = True

    return result


# ============================================================
# PLANETS
# ============================================================

def normalize_planets(data):

    objects = get_list(
        data,
        [
            "objects",
            "planets",
            "targets",
        ],
    )

    normalized = []

    for item in objects:

        item = normalize_object(item)

        name = get_object_name(item)

        item["name"] = name

        item["type"] = "planet"

        item = normalize_visibility(item)

        normalized.append(item)

    return normalized


# ============================================================
# DEEP SKY
# ============================================================

def normalize_deep_sky(data):

    objects = get_list(
        data,
        [
            "objects",
            "targets",
            "deep_sky",
        ],
    )

    normalized = []

    for item in objects:

        item = normalize_object(item)

        item["name"] = get_object_name(item)

        item["type"] = "deep_sky"

        item = normalize_visibility(item)

        normalized.append(item)

    return normalized


# ============================================================
# CONSTELLATIONS
# ============================================================

def normalize_constellations(data):

    objects = get_list(
        data,
        [
            "objects",
            "targets",
            "constellations",
        ],
    )

    normalized = []

    for item in objects:

        item = normalize_object(item)

        item["name"] = get_object_name(item)

        item["type"] = "constellation"

        item = normalize_visibility(item)

        normalized.append(item)

    return normalized


# ============================================================
# METEOR SHOWERS
# ============================================================

def get_peak_time(item):
    """
    Extract peak time only when supplied by the API.
    Never invent a peak time.
    """

    if not isinstance(item, dict):
        return None

    return first_not_none(
        item.get("peak_time"),
        item.get("peakTime"),
        item.get("maximum_time"),
        item.get("maximumTime"),
        item.get("peak_datetime"),
        item.get("peak_datetime_local"),
    )


def get_peak_date(item):
    """
    Extract peak date only when supplied by the API.
    """

    if not isinstance(item, dict):
        return None

    return first_not_none(
        item.get("peak_date"),
        item.get("peakDate"),
        item.get("maximum_date"),
        item.get("maximumDate"),
    )


def get_peak_rate(item):
    """
    Extract meteor shower peak rate / ZHR when supplied.
    """

    if not isinstance(item, dict):
        return None

    return first_not_none(
        item.get("peak_rate"),
        item.get("peakRate"),
        item.get("zhr"),
        item.get("maximum_rate"),
        item.get("maximumRate"),
        item.get("rate"),
    )


def normalize_meteor_showers(data):

    objects = get_list(
        data,
        [
            "showers",
            "objects",
            "targets",
            "meteor_showers",
        ],
    )

    normalized = []

    for item in objects:

        item = normalize_object(item)

        item["name"] = get_object_name(item)

        item["type"] = "meteor_shower"

        item = normalize_visibility(item)

        # Preserve / expose peak information if API supplies it
        peak_date = get_peak_date(item)
        peak_time = get_peak_time(item)
        peak_rate = get_peak_rate(item)

        if peak_date is not None:
            item["peak_date"] = peak_date

        if peak_time is not None:
            item["peak_time"] = peak_time

        if peak_rate is not None:
            item["peak_rate"] = peak_rate

        normalized.append(item)

    return normalized


# ============================================================
# EVENTS
# ============================================================

def normalize_events(data):

    if not data:

        return {
            "eclipses": [],
            "conjunctions": [],
            "oppositions": [],
            "occultations": [],
        }

    if not isinstance(data, dict):

        return {
            "eclipses": [],
            "conjunctions": [],
            "oppositions": [],
            "occultations": [],
        }

    events = data.get("events")

    if isinstance(events, dict):

        return {
            "eclipses": events.get(
                "eclipses",
                []
            ) or [],

            "conjunctions": events.get(
                "conjunctions",
                []
            ) or [],

            "oppositions": events.get(
                "oppositions",
                []
            ) or [],

            "occultations": events.get(
                "occultations",
                []
            ) or [],
        }

    return {
        "eclipses": data.get(
            "eclipses",
            []
        ) or [],

        "conjunctions": data.get(
            "conjunctions",
            []
        ) or [],

        "oppositions": data.get(
            "oppositions",
            []
        ) or [],

        "occultations": data.get(
            "occultations",
            []
        ) or [],
    }


# ============================================================
# DATE / TIME
# ============================================================

def parse_local_datetime(date_string, time_string):

    return datetime.strptime(
        f"{date_string} {time_string}",
        "%Y-%m-%d %H:%M",
    )


def build_observation_range(
    from_date,
    to_date,
    from_time,
    to_time,
):

    start = parse_local_datetime(
        from_date,
        from_time,
    )

    end = parse_local_datetime(
        to_date,
        to_time,
    )

    # Overnight session
    if end <= start:
        end += timedelta(days=1)

    return start, end


# ============================================================
# WEATHER
# ============================================================

def parse_weather_hour(value):

    if not isinstance(value, str):
        return None

    value = value.strip()

    try:

        return datetime.fromisoformat(
            value.replace(
                "Z",
                "+00:00",
            )
        ).replace(tzinfo=None)

    except Exception:

        return None


def empty_weather_selection():

    return {
        "times": [],
        "temperature": [],
        "humidity": [],
        "dew_point": [],
        "cloud_cover": [],
        "precipitation_probability": [],
        "visibility": [],
        "wind_speed": [],
        "wind_direction": [],
        "wind_gusts": [],
    }


def filter_weather_to_session(
    weather_data,
    from_date,
    to_date,
    from_time,
    to_time,
):

    if not isinstance(weather_data, dict):
        return empty_weather_selection()

    hourly = weather_data.get("hourly")

    if not isinstance(hourly, dict):
        return empty_weather_selection()

    raw_times = hourly.get("time", [])

    if not isinstance(raw_times, list):
        raw_times = []

    try:

        session_start, session_end = (
            build_observation_range(
                from_date,
                to_date,
                from_time,
                to_time,
            )
        )

    except Exception:

        return empty_weather_selection()

    selected_indexes = []

    for index, raw_time in enumerate(raw_times):

        parsed_time = parse_weather_hour(
            raw_time
        )

        if parsed_time is None:
            continue

        if (
            session_start
            <= parsed_time
            <= session_end
        ):
            selected_indexes.append(index)

    fields = {
        "temperature": "temperature_2m",
        "humidity": "relative_humidity_2m",
        "dew_point": "dew_point_2m",
        "cloud_cover": "cloud_cover",
        "precipitation_probability":
            "precipitation_probability",
        "visibility": "visibility",
        "wind_speed": "wind_speed_10m",
        "wind_direction": "wind_direction_10m",
        "wind_gusts": "wind_gusts_10m",
    }

    result = {
        "times": [],
    }

    for output_key in fields:
        result[output_key] = []

    for index in selected_indexes:

        result["times"].append(
            raw_times[index]
        )

        for output_key, source_key in fields.items():

            values = hourly.get(
                source_key,
                []
            )

            if (
                isinstance(values, list)
                and index < len(values)
            ):

                result[output_key].append(
                    values[index]
                )

    return result


# ============================================================
# NUMERIC HELPERS
# ============================================================

def numeric_values(values):

    if not isinstance(values, list):
        return []

    result = []

    for value in values:

        if isinstance(value, bool):
            continue

        if isinstance(
            value,
            (int, float)
        ):

            if math.isfinite(
                float(value)
            ):

                result.append(
                    float(value)
                )

    return result


def average(values):

    values = numeric_values(values)

    if not values:
        return None

    return sum(values) / len(values)


def minimum(values):

    values = numeric_values(values)

    if not values:
        return None

    return min(values)


def maximum(values):

    values = numeric_values(values)

    if not values:
        return None

    return max(values)


def round_value(
    value,
    digits=1,
):

    if value is None:
        return None

    try:
        return round(
            float(value),
            digits,
        )

    except Exception:
        return value


# ============================================================
# WEATHER SUMMARY
# ============================================================

def build_weather_summary(
    weather_data,
    from_date,
    to_date,
    from_time,
    to_time,
):

    selected = filter_weather_to_session(
        weather_data,
        from_date,
        to_date,
        from_time,
        to_time,
    )

    cloud = numeric_values(
        selected.get(
            "cloud_cover",
            []
        )
    )

    humidity = numeric_values(
        selected.get(
            "humidity",
            []
        )
    )

    visibility = numeric_values(
        selected.get(
            "visibility",
            []
        )
    )

    wind = numeric_values(
        selected.get(
            "wind_speed",
            []
        )
    )

    temperature = numeric_values(
        selected.get(
            "temperature",
            []
        )
    )

    dew_point = numeric_values(
        selected.get(
            "dew_point",
            []
        )
    )

    precipitation = numeric_values(
        selected.get(
            "precipitation_probability",
            []
        )
    )

    return {

        "selected_period": {
            "from": f"{from_date} {from_time}",
            "to": f"{to_date} {to_time}",
        },

        "data_points": len(
            selected.get(
                "times",
                []
            )
        ),

        "cloud_cover": round_value(
            average(cloud),
            1,
        ),

        "cloud_cover_min": round_value(
            minimum(cloud),
            1,
        ),

        "cloud_cover_max": round_value(
            maximum(cloud),
            1,
        ),

        "humidity": round_value(
            average(humidity),
            1,
        ),

        "humidity_min": round_value(
            minimum(humidity),
            1,
        ),

        "humidity_max": round_value(
            maximum(humidity),
            1,
        ),

        "visibility_km": round_value(
            average(visibility),
            1,
        ),

        "visibility_min_km": round_value(
            minimum(visibility),
            1,
        ),

        "visibility_max_km": round_value(
            maximum(visibility),
            1,
        ),

        "wind_speed_kmh": round_value(
            average(wind),
            1,
        ),

        "wind_speed_max_kmh": round_value(
            maximum(wind),
            1,
        ),

        "temperature_c": round_value(
            average(temperature),
            1,
        ),

        "temperature_min_c": round_value(
            minimum(temperature),
            1,
        ),

        "temperature_max_c": round_value(
            maximum(temperature),
            1,
        ),

        "dew_point_c": round_value(
            average(dew_point),
            1,
        ),

        "dew_point_min_c": round_value(
            minimum(dew_point),
            1,
        ),

        "dew_point_max_c": round_value(
            maximum(dew_point),
            1,
        ),

        "precipitation_probability": round_value(
            average(precipitation),
            1,
        ),
    }


# ============================================================
# WEATHER DISPLAY
# ============================================================

def build_weather_display(
    weather_summary
):

    if not isinstance(
        weather_summary,
        dict,
    ):

        return {
            "cloud_cover": None,
            "humidity": None,
            "visibility": None,
            "wind": None,
            "temperature": None,
            "dew_point": None,
        }

    return {

        "cloud_cover":
            weather_summary.get(
                "cloud_cover"
            ),

        "humidity":
            weather_summary.get(
                "humidity"
            ),

        "visibility":
            weather_summary.get(
                "visibility_km"
            ),

        "wind":
            weather_summary.get(
                "wind_speed_kmh"
            ),

        "temperature":
            weather_summary.get(
                "temperature_c"
            ),

        "dew_point":
            weather_summary.get(
                "dew_point_c"
            ),
    }


# ============================================================
# SUN SUMMARY
# ============================================================

def build_sun_summary(sun_data):

    if not isinstance(
        sun_data,
        dict,
    ):
        return None

    results = sun_data.get(
        "results"
    )

    if not isinstance(
        results,
        dict,
    ):
        return None

    return {

        "sunrise":
            results.get(
                "sunrise"
            ),

        "sunset":
            results.get(
                "sunset"
            ),

        "civil_twilight_begin":
            results.get(
                "civil_twilight_begin"
            ),

        "civil_twilight_end":
            results.get(
                "civil_twilight_end"
            ),

        "nautical_twilight_begin":
            results.get(
                "nautical_twilight_begin"
            ),

        "nautical_twilight_end":
            results.get(
                "nautical_twilight_end"
            ),

        "astronomical_twilight_begin":
            results.get(
                "astronomical_twilight_begin"
            ),

        "astronomical_twilight_end":
            results.get(
                "astronomical_twilight_end"
            ),
    }


# ============================================================
# MOON
# ============================================================

def build_moon_summary(planets):

    """
    Extract Moon ONLY if the planet module provides Moon data.

    Never invent:
        phase
        illumination
        rise
        set
        altitude
        azimuth
    """

    if not isinstance(
        planets,
        list,
    ):
        return None

    moon = None

    for item in planets:

        if not isinstance(
            item,
            dict,
        ):
            continue

        name = item.get(
            "name"
        )

        if not isinstance(
            name,
            str,
        ):

            name = get_object_name(
                item
            )

        if isinstance(
            name,
            str,
        ):

            if (
                name.strip()
                .lower()
                == "moon"
            ):

                moon = item
                break

    if not moon:
        return None

    return {

        "name": "Moon",

        "phase": first_not_none(
            moon.get(
                "phase"
            ),
            moon.get(
                "moon_phase"
            ),
        ),

        "illumination": first_not_none(
            moon.get(
                "illumination"
            ),
            moon.get(
                "moon_illumination"
            ),
        ),

        "rise": first_not_none(
            moon.get(
                "rise"
            ),
            moon.get(
                "moonrise"
            ),
            moon.get(
                "rise_time"
            ),
        ),

        "set": first_not_none(
            moon.get(
                "set"
            ),
            moon.get(
                "moonset"
            ),
            moon.get(
                "set_time"
            ),
        ),

        "altitude": first_not_none(
            moon.get(
                "altitude"
            ),
            moon.get(
                "alt"
            ),
        ),

        "azimuth": first_not_none(
            moon.get(
                "azimuth"
            ),
            moon.get(
                "az"
            ),
        ),
    }


# ============================================================
# VISIBILITY
# ============================================================

def is_visible(item):

    if not isinstance(
        item,
        dict,
    ):
        return False

    value = item.get(
        "visible"
    )

    if isinstance(
        value,
        bool,
    ):
        return value

    observability = item.get(
        "observability"
    )

    if isinstance(
        observability,
        str,
    ):

        lowered = (
            observability
            .lower()
            .strip()
        )

        # Important: check negative values first
        if any(
            word in lowered
            for word in [
                "not visible",
                "below horizon",
                "unobservable",
                "not observable",
            ]
        ):
            return False

        if any(
            word in lowered
            for word in [
                "visible",
                "excellent",
                "good",
                "fair",
                "observable",
            ]
        ):
            return True

    return False


def count_visibility(objects):

    visible = 0
    not_visible = 0

    for item in objects:

        if is_visible(item):
            visible += 1

        else:
            not_visible += 1

    return {
        "visible": visible,
        "not_visible": not_visible,
        "total": len(objects),
    }


def build_visibility_summary(
    planets,
    deep_sky,
    constellations,
    meteor_showers,
):

    all_objects = []

    all_objects.extend(
        planets or []
    )

    all_objects.extend(
        deep_sky or []
    )

    all_objects.extend(
        constellations or []
    )

    all_objects.extend(
        meteor_showers or []
    )

    return count_visibility(
        all_objects
    )


# ============================================================
# DIFFICULTY
# ============================================================

def normalize_difficulty(value):

    if not isinstance(
        value,
        str,
    ):
        return None

    value = value.strip().lower()

    if value in [
        "easy",
        "beginner",
    ]:
        return "Easy"

    if value in [
        "medium",
        "moderate",
    ]:
        return "Medium"

    if value in [
        "hard",
        "difficult",
    ]:
        return "Hard"

    if value in [
        "very hard",
        "expert",
        "extreme",
    ]:
        return "Very Hard"

    return None


def build_difficulty_summary(
    planets,
    deep_sky,
    constellations,
    meteor_showers,
):

    all_objects = []

    all_objects.extend(
        planets or []
    )

    all_objects.extend(
        deep_sky or []
    )

    all_objects.extend(
        constellations or []
    )

    all_objects.extend(
        meteor_showers or []
    )

    summary = {
        "Easy": 0,
        "Medium": 0,
        "Hard": 0,
        "Very Hard": 0,
        "Unknown": 0,
    }

    for item in all_objects:

        if not isinstance(
            item,
            dict,
        ):

            summary["Unknown"] += 1
            continue

        difficulty = normalize_difficulty(
            item.get(
                "difficulty"
            )
        )

        if difficulty:
            summary[difficulty] += 1

        else:
            summary["Unknown"] += 1

    return summary


# ============================================================
# OBSERVATION QUALITY
# ============================================================

def calculate_observation_quality(
    weather_summary,
    visibility_summary,
):

    if not isinstance(
        weather_summary,
        dict,
    ):
        weather_summary = {}

    cloud = weather_summary.get(
        "cloud_cover"
    )

    humidity = weather_summary.get(
        "humidity"
    )

    visibility = weather_summary.get(
        "visibility_km"
    )

    wind = weather_summary.get(
        "wind_speed_kmh"
    )

    score = 0.0

    # CLOUD
    if isinstance(
        cloud,
        (int, float),
    ):

        if cloud <= 10:
            score += 4.0

        elif cloud <= 25:
            score += 3.5

        elif cloud <= 40:
            score += 2.8

        elif cloud <= 60:
            score += 2.0

        elif cloud <= 80:
            score += 1.0

        else:
            score += 0.2

    # HUMIDITY
    if isinstance(
        humidity,
        (int, float),
    ):

        if humidity <= 60:
            score += 2.0

        elif humidity <= 70:
            score += 1.6

        elif humidity <= 80:
            score += 1.1

        elif humidity <= 90:
            score += 0.6

        else:
            score += 0.2

    # VISIBILITY
    if isinstance(
        visibility,
        (int, float),
    ):

        if visibility >= 20:
            score += 1.5

        elif visibility >= 10:
            score += 1.2

        elif visibility >= 5:
            score += 0.8

        elif visibility >= 2:
            score += 0.4

        else:
            score += 0.1

    # WIND
    if isinstance(
        wind,
        (int, float),
    ):

        if wind <= 10:
            score += 1.0

        elif wind <= 20:
            score += 0.7

        elif wind <= 30:
            score += 0.4

        else:
            score += 0.1

    # VISIBLE TARGET BONUS
    if isinstance(
        visibility_summary,
        dict,
    ):

        visible = visibility_summary.get(
            "visible",
            0,
        )

        if isinstance(
            visible,
            int,
        ):

            if visible >= 15:
                score += 1.5

            elif visible >= 10:
                score += 1.2

            elif visible >= 5:
                score += 0.8

            elif visible > 0:
                score += 0.4

    score = max(
        0,
        min(
            10,
            round(
                score,
                1,
            ),
        ),
    )

    if score >= 8:
        label = "Excellent"

    elif score >= 6:
        label = "Good"

    elif score >= 4:
        label = "Fair"

    elif score >= 2:
        label = "Poor"

    else:
        label = "Very Poor"

    return {
        "score": score,
        "label": label,
    }


# ============================================================
# AI INPUT
# ============================================================

def build_ai_input(
    observation,
    weather_summary,
    sun_summary,
    moon_summary,
    planets,
    deep_sky,
    constellations,
    meteor_showers,
    events,
):

    return {

        "observation": observation,

        "weather": weather_summary,

        "sun": sun_summary,

        # If None, Gemini must treat Moon data as unavailable.
        "moon": moon_summary,

        "planets": planets,

        "deep_sky": deep_sky,

        "constellations": constellations,

        "meteor_showers": meteor_showers,

        "events": events,
    }


# ============================================================
# MAIN OBSERVATION API
# ============================================================

@router.post("/observation/analyze")
def analyze_observation(

    latitude: float = Query(...),

    longitude: float = Query(...),

    from_date: str = Query(...),

    to_date: str = Query(...),

    from_time: str = Query("20:00"),

    to_time: str = Query("02:00"),

):

    # ========================================================
    # VALIDATE DATE / TIME
    # ========================================================

    try:

        start_datetime, end_datetime = (
            build_observation_range(
                from_date,
                to_date,
                from_time,
                to_time,
            )
        )

    except Exception as e:

        return {

            "success": False,

            "error": (
                "Invalid date/time format. "
                "Use YYYY-MM-DD for dates "
                "and HH:MM for times."
            ),

            "details": str(e),

            "type": type(e).__name__,
        }

    observation = {

        "latitude": latitude,

        "longitude": longitude,

        "from_date": from_date,

        "to_date": to_date,

        "from_time": from_time,

        "to_time": to_time,

        "start_local":
            start_datetime.isoformat(),

        "end_local":
            end_datetime.isoformat(),
    }


    # ========================================================
    # WEATHER
    # ========================================================

    weather_raw = safe_call(
        get_weather,
        latitude,
        longitude,
    )

    weather_summary = build_weather_summary(
        weather_raw,
        from_date,
        to_date,
        from_time,
        to_time,
    )

    weather_display = build_weather_display(
        weather_summary
    )


    # ========================================================
    # 7TIMER
    # ========================================================

    astro_weather = None

    if get_astro_weather is not None:

        astro_weather = safe_call(
            get_astro_weather,

            latitude,
            longitude,

            from_date,
            to_date,

            from_time,
            to_time,
        )


    # ========================================================
    # SUN
    # ========================================================

    sun_raw = safe_call(
        get_sun,

        latitude,
        longitude,

        from_date,
    )

    sun_summary = build_sun_summary(
        sun_raw
    )


    # ========================================================
    # PLANETS
    # ========================================================

    planets_raw = safe_call(
        get_planets,

        latitude,
        longitude,

        from_date,
        to_date,

        from_time,
        to_time,
    )

    planets = normalize_planets(
        planets_raw
    )


    # ========================================================
    # MOON
    # ========================================================

    moon_summary = build_moon_summary(
        planets
    )


    # ========================================================
    # DEEP SKY
    # ========================================================

    deep_sky_raw = safe_call(
        get_deep_sky,

        latitude,
        longitude,

        from_date,
        to_date,

        from_time,
        to_time,
    )

    deep_sky = normalize_deep_sky(
        deep_sky_raw
    )


    # ========================================================
    # CONSTELLATIONS
    # ========================================================

    constellations_raw = safe_call(
        get_constellations,

        latitude,
        longitude,

        from_date,
        to_date,

        from_time,
        to_time,
    )

    constellations = normalize_constellations(
        constellations_raw
    )


    # ========================================================
    # METEOR SHOWERS
    # ========================================================

    meteor_showers_raw = safe_call(
        get_meteor_showers,

        latitude,
        longitude,

        from_date,
        to_date,

        from_time,
        to_time,
    )

    meteor_showers = normalize_meteor_showers(
        meteor_showers_raw
    )


    # ========================================================
    # ASTRONOMICAL EVENTS
    # ========================================================

    events_raw = safe_call(
        get_astronomical_events,

        latitude,
        longitude,

        from_date,
        to_date,

        from_time,
        to_time,
    )

    events = normalize_events(
        events_raw
    )


    # ========================================================
    # VISIBILITY
    # ========================================================

    visibility_summary = (
        build_visibility_summary(
            planets,
            deep_sky,
            constellations,
            meteor_showers,
        )
    )


    # ========================================================
    # DIFFICULTY
    # ========================================================

    difficulty_summary = (
        build_difficulty_summary(
            planets,
            deep_sky,
            constellations,
            meteor_showers,
        )
    )


    # ========================================================
    # OBSERVATION QUALITY
    # ========================================================

    observation_quality = (
        calculate_observation_quality(
            weather_summary,
            visibility_summary,
        )
    )


    # ========================================================
    # OVERVIEW
    # ========================================================

    overview = {

        "cloud_cover":
            weather_summary.get(
                "cloud_cover"
            ),

        "humidity":
            weather_summary.get(
                "humidity"
            ),

        "visibility_km":
            weather_summary.get(
                "visibility_km"
            ),

        "wind_speed_kmh":
            weather_summary.get(
                "wind_speed_kmh"
            ),

        "temperature_c":
            weather_summary.get(
                "temperature_c"
            ),

        "dew_point_c":
            weather_summary.get(
                "dew_point_c"
            ),

        # This remains None when Moon information
        # is unavailable.
        "moon_illumination": (
            moon_summary.get(
                "illumination"
            )
            if moon_summary
            else None
        ),

        "visible_targets":
            visibility_summary.get(
                "visible",
                0,
            ),

        "total_targets":
            visibility_summary.get(
                "total",
                0,
            ),

        "observation_score":
            observation_quality.get(
                "score"
            ),

        "observation_label":
            observation_quality.get(
                "label"
            ),
    }


    # ========================================================
    # AI RECOMMENDATION
    # ========================================================

    ai_recommendation = None

    ai_input = build_ai_input(

        observation=observation,

        weather_summary=weather_summary,

        sun_summary=sun_summary,

        moon_summary=moon_summary,

        planets=planets,

        deep_sky=deep_sky,

        constellations=constellations,

        meteor_showers=meteor_showers,

        events=events,
    )

    try:

        ai_recommendation = (
            generate_recommendation(
                ai_input
            )
        )

    except Exception as e:

        ai_recommendation = {

            "score": None,

            "recommendation":
                "AI recommendation unavailable.",

            "best_time": None,

            "best_targets": [],

            "weather_summary": "",

            "astronomy_summary": "",

            "tips": [],

            "error": str(e),
        }


    # ========================================================
    # MODULE STATUS
    # ========================================================

    module_status = {

        "weather":
            isinstance(
                weather_raw,
                dict,
            )
            and not weather_raw.get(
                "error"
            ),

        "astro_weather":
            isinstance(
                astro_weather,
                dict,
            )
            and not astro_weather.get(
                "error"
            ),

        "sun":
            isinstance(
                sun_raw,
                dict,
            )
            and not sun_raw.get(
                "error"
            ),

        "planets":
            isinstance(
                planets_raw,
                dict,
            )
            and not planets_raw.get(
                "error"
            ),

        "deep_sky":
            isinstance(
                deep_sky_raw,
                dict,
            )
            and not deep_sky_raw.get(
                "error"
            ),

        "constellations":
            isinstance(
                constellations_raw,
                dict,
            )
            and not constellations_raw.get(
                "error"
            ),

        "meteor_showers":
            isinstance(
                meteor_showers_raw,
                dict,
            )
            and not meteor_showers_raw.get(
                "error"
            ),

        "events":
            isinstance(
                events_raw,
                dict,
            )
            and not events_raw.get(
                "error"
            ),

        "ai_recommendation":
            isinstance(
                ai_recommendation,
                dict,
            )
            and not ai_recommendation.get(
                "error"
            ),
    }


    # ========================================================
    # FINAL RESPONSE
    # ========================================================

    return {

        "success": True,

        # ----------------------------------------------------
        # Observation
        # ----------------------------------------------------

        "observation":
            observation,


        # ----------------------------------------------------
        # Quick Summary
        # ----------------------------------------------------

        "overview":
            overview,


        # ----------------------------------------------------
        # Weather
        # ----------------------------------------------------

        "weather":
            weather_raw,

        "weather_summary":
            weather_summary,

        "weather_display":
            weather_display,


        # ----------------------------------------------------
        # Astronomical Weather
        # ----------------------------------------------------

        "astro_weather":
            astro_weather,


        # ----------------------------------------------------
        # Sun
        # ----------------------------------------------------

        "sun":
            sun_raw,

        "sun_summary":
            sun_summary,


        # ----------------------------------------------------
        # Moon
        # ----------------------------------------------------

        "moon":
            moon_summary,


        # ----------------------------------------------------
        # Planets
        # ----------------------------------------------------

        "planets": {

            "success": True,

            "count":
                len(planets),

            "objects":
                planets,
        },


        # ----------------------------------------------------
        # Deep Sky
        # ----------------------------------------------------

        "deep_sky": {

            "success": True,

            "count":
                len(deep_sky),

            "objects":
                deep_sky,
        },


        # ----------------------------------------------------
        # Constellations
        # ----------------------------------------------------

        "constellations": {

            "success": True,

            "count":
                len(constellations),

            "objects":
                constellations,
        },


        # ----------------------------------------------------
        # Meteor Showers
        # ----------------------------------------------------

        "meteor_showers": {

            "success": True,

            "count":
                len(meteor_showers),

            "showers":
                meteor_showers,
        },


        # ----------------------------------------------------
        # Astronomical Events
        # ----------------------------------------------------

        "events": {

            "success": True,

            "count": (

                len(
                    events.get(
                        "eclipses",
                        []
                    )
                )

                +

                len(
                    events.get(
                        "conjunctions",
                        []
                    )
                )

                +

                len(
                    events.get(
                        "oppositions",
                        []
                    )
                )

                +

                len(
                    events.get(
                        "occultations",
                        []
                    )
                )
            ),

            "events":
                events,
        },


        # ----------------------------------------------------
        # Visibility
        # ----------------------------------------------------

        "visibility_summary":
            visibility_summary,

        # Kept for compatibility with your existing frontend.
        "visibility_overview": {

            "visible":
                visibility_summary.get(
                    "visible",
                    0,
                ),

            "not_visible":
                visibility_summary.get(
                    "not_visible",
                    0,
                ),

            "total":
                visibility_summary.get(
                    "total",
                    0,
                ),
        },


        # ----------------------------------------------------
        # Difficulty
        # ----------------------------------------------------

        "difficulty_summary":
            difficulty_summary,


        # ----------------------------------------------------
        # Overall Quality
        # ----------------------------------------------------

        "observation_quality":
            observation_quality,


        # ----------------------------------------------------
        # Gemini
        # ----------------------------------------------------

        "ai_recommendation":
            ai_recommendation,


        # ----------------------------------------------------
        # Module Status
        # ----------------------------------------------------

        "module_status":
            module_status,
    }
