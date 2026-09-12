# import requests

# from datetime import datetime, timedelta, timezone

# from fastapi import APIRouter, Query

# router = APIRouter()

# SPACE_CATALOG_URL = "https://spacecatalog.org/api/v1/visible"


# def get_visible_constellations(
#     latitude,
#     longitude,
#     start_local,
#     end_local
# ):
#     constellations = {}

#     current = start_local

#     while current <= end_local:

#         # India/local observation time -> UTC
#         utc_time = current.astimezone(timezone.utc)

#         time_string = utc_time.strftime(
#             "%Y-%m-%dT%H:%M:%SZ"
#         )

#         params = {
#             "lat": latitude,
#             "lon": longitude,
#             "time": time_string,
#             "min_alt": 20,
#             "limit": 100
#         }

#         response = None

#         # Retry remote connection up to 3 times
#         for attempt in range(3):

#             try:

#                 response = requests.get(
#                     SPACE_CATALOG_URL,
#                     params=params,
#                     timeout=30
#                 )

#                 response.raise_for_status()

#                 break

#             except (
#                 requests.exceptions.ConnectionError,
#                 requests.exceptions.Timeout
#             ):

#                 if attempt == 2:
#                     raise

#         data = response.json()

#         if not isinstance(data, dict):
#             current += timedelta(hours=1)
#             continue

#         objects = data.get("objects", [])

#         if not isinstance(objects, list):
#             objects = []

#         for obj in objects:

#             if not isinstance(obj, dict):
#                 continue

#             constellation = obj.get("constellation")

#             if not constellation:
#                 continue

#             altitude = obj.get("altitude_deg")

#             if altitude is None:
#                 continue

#             try:
#                 altitude = float(altitude)
#             except (ValueError, TypeError):
#                 continue

#             if altitude < 20:
#                 continue

#             azimuth = obj.get("azimuth_deg")
#             direction = obj.get("bearing")

#             if constellation not in constellations:

#                 constellations[constellation] = {
#                     "name": constellation,
#                     "visible": True,
#                     "best_time": current.isoformat(),
#                     "best_altitude": altitude,
#                     "azimuth": azimuth,
#                     "direction": direction
#                 }

#             else:

#                 existing = constellations[constellation]

#                 existing_altitude = existing.get(
#                     "best_altitude",
#                     -999
#                 )

#                 if altitude > existing_altitude:

#                     existing["best_altitude"] = altitude

#                     existing["best_time"] = current.isoformat()

#                     existing["azimuth"] = azimuth

#                     existing["direction"] = direction

#         current += timedelta(hours=1)

#     result = list(constellations.values())

#     result.sort(
#         key=lambda x: x.get(
#             "best_altitude",
#             -999
#         ),
#         reverse=True
#     )

#     return result


# @router.get("/constellations")
# def get_constellations(
#     latitude: float = Query(...),
#     longitude: float = Query(...),
#     from_date: str = Query(...),
#     to_date: str = Query(...),
#     from_time: str = Query("20:00"),
#     to_time: str = Query("02:00")
# ):

#     try:

#         # --------------------------------------------------
#         # Parse observation period
#         # --------------------------------------------------

#         start_local = datetime.strptime(
#             f"{from_date} {from_time}",
#             "%Y-%m-%d %H:%M"
#         )

#         end_local = datetime.strptime(
#             f"{to_date} {to_time}",
#             "%Y-%m-%d %H:%M"
#         )

#         if end_local <= start_local:

#             return {
#                 "success": False,
#                 "error": "To date/time must be after From date/time"
#             }

#         # --------------------------------------------------
#         # IMPORTANT
#         # --------------------------------------------------
#         # Your location is India.
#         #
#         # We use +05:30 explicitly instead of ZoneInfo,
#         # so Windows does not need the IANA timezone database.
#         # --------------------------------------------------

#         india_timezone = timezone(
#             # timedelta(hours=5, minutes=30)
#             timedelta(minutes=5)
#         )

#         start_local = start_local.replace(
#             tzinfo=india_timezone
#         )

#         end_local = end_local.replace(
#             tzinfo=india_timezone
#         )

#         # --------------------------------------------------
#         # Get visible constellations
#         # --------------------------------------------------

#         constellations = get_visible_constellations(
#             latitude=latitude,
#             longitude=longitude,
#             start_local=start_local,
#             end_local=end_local
#         )

#         # --------------------------------------------------
#         # Response
#         # --------------------------------------------------

#         return {
#             "success": True,

#             "location": {
#                 "latitude": latitude,
#                 "longitude": longitude,
#                 "timezone": "Asia/Kolkata"
#             },

#             "observation": {
#                 "from_date": from_date,
#                 "to_date": to_date,
#                 "from_time": from_time,
#                 "to_time": to_time,
#                 "start_local": start_local.isoformat(),
#                 "end_local": end_local.isoformat()
#             },

#             "count": len(constellations),

#             "constellations": constellations,

#             "source": {
#                 "name": "SpaceCatalog.org",
#                 "url": "https://spacecatalog.org/api"
#             }
#         }

#     except requests.exceptions.RequestException as e:

#         return {
#             "success": False,
#             "error": "Unable to fetch constellation data",
#             "details": str(e),
#             "type": type(e).__name__
#         }

#     except Exception as e:

#         return {
#             "success": False,
#             "error": str(e),
#             "type": type(e).__name__
#         }

import requests

from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Query


router = APIRouter()


# =========================================================
# API URLS
# =========================================================

SPACE_CATALOG_URL = (
    "https://spacecatalog.org/api/v1/visible"
)

WEATHER_URL = (
    "https://api.open-meteo.com/v1/forecast"
)


# =========================================================
# CONSTANTS
# =========================================================

INDIA_TIMEZONE = timezone(
    timedelta(hours=5, minutes=30)
)

MAX_RESULTS = 10


# =========================================================
# WEATHER
# =========================================================

def get_cloud_cover(
    latitude,
    longitude,
    start_local,
    end_local
):

    try:

        response = requests.get(

            WEATHER_URL,

            params={

                "latitude":
                    latitude,

                "longitude":
                    longitude,

                "hourly": [

                    "cloud_cover",

                    "precipitation_probability",

                    "visibility"

                ],

                "timezone":
                    "auto",

                "forecast_days":
                    7

            },

            timeout=20

        )

        response.raise_for_status()

        data = response.json()

        hourly = data.get(
            "hourly",
            {}
        )

        times = hourly.get(
            "time",
            []
        )

        clouds = hourly.get(
            "cloud_cover",
            []
        )

        precipitation = hourly.get(
            "precipitation_probability",
            []
        )

        visibility = hourly.get(
            "visibility",
            []
        )

        selected_clouds = []

        selected_precipitation = []

        selected_visibility = []


        # =================================================
        # SELECT WEATHER FOR OBSERVATION PERIOD
        # =================================================

        for index, time_string in enumerate(times):

            try:

                weather_time = datetime.fromisoformat(
                    time_string
                )

                if weather_time.tzinfo is None:

                    weather_time = weather_time.replace(
                        tzinfo=INDIA_TIMEZONE
                    )

            except Exception:

                continue


            if (
                start_local
                <= weather_time
                <= end_local
            ):

                if index < len(clouds):

                    value = clouds[index]

                    if value is not None:

                        selected_clouds.append(
                            float(value)
                        )


                if index < len(precipitation):

                    value = precipitation[index]

                    if value is not None:

                        selected_precipitation.append(
                            float(value)
                        )


                if index < len(visibility):

                    value = visibility[index]

                    if value is not None:

                        selected_visibility.append(
                            float(value)
                        )


        # =================================================
        # NO WEATHER DATA
        # =================================================

        if not selected_clouds:

            return {

                "known":
                    False,

                "cloud_cover_percent":
                    None,

                "precipitation_probability_percent":
                    None,

                "visibility_m":
                    None

            }


        # =================================================
        # WEATHER RESULT
        # =================================================

        return {

            "known":
                True,

            "cloud_cover_percent":
                round(
                    sum(selected_clouds)
                    / len(selected_clouds),
                    1
                ),

            "precipitation_probability_percent":
                round(
                    sum(selected_precipitation)
                    / len(selected_precipitation),
                    1
                )
                if selected_precipitation
                else None,

            "visibility_m":
                round(
                    sum(selected_visibility)
                    / len(selected_visibility),
                    0
                )
                if selected_visibility
                else None

        }


    except Exception:

        return {

            "known":
                False,

            "cloud_cover_percent":
                None,

            "precipitation_probability_percent":
                None,

            "visibility_m":
                None

        }


# =========================================================
# CLOUD QUALITY
# =========================================================

def get_cloud_quality(
    cloud_cover
):

    if cloud_cover is None:

        return {

            "level":
                "unknown",

            "label":
                "Unknown",

            "score":
                0,

            "reason":
                "Cloud information is unavailable."

        }


    if cloud_cover <= 10:

        return {

            "level":
                "excellent",

            "label":
                "Excellent",

            "score":
                4,

            "reason":
                "Very low cloud cover."

        }


    if cloud_cover <= 30:

        return {

            "level":
                "good",

            "label":
                "Good",

            "score":
                3,

            "reason":
                "Low cloud cover."

        }


    if cloud_cover <= 60:

        return {

            "level":
                "fair",

            "label":
                "Fair",

            "score":
                2,

            "reason":
                "Some cloud cover may interfere."

        }


    if cloud_cover <= 80:

        return {

            "level":
                "poor",

            "label":
                "Poor",

            "score":
                1,

            "reason":
                "High cloud cover may interfere."

        }


    return {

        "level":
            "very_poor",

        "label":
            "Very Poor",

        "score":
            0,

        "reason":
            "Heavy cloud cover is likely to block the sky."

    }


# =========================================================
# CONSTELLATION DIFFICULTY
# =========================================================

def calculate_difficulty(
    altitude
):

    try:

        altitude = float(
            altitude
        )

    except Exception:

        altitude = None


    if altitude is None:

        return {

            "level":
                "moderate",

            "label":
                "Moderate",

            "recommendation":
                "Suitable for observation when sky conditions are favorable."

        }


    if altitude >= 60:

        return {

            "level":
                "easy",

            "label":
                "Easy",

            "recommendation":
                "High in the sky and generally easy to locate."

        }


    if altitude >= 40:

        return {

            "level":
                "moderate",

            "label":
                "Moderate",

            "recommendation":
                "Reasonably high in the sky and suitable for observation."

        }


    if altitude >= 20:

        return {

            "level":
                "hard",

            "label":
                "Hard",

            "recommendation":
                "Lower altitude may make the constellation harder to observe."

        }


    return {

        "level":
            "very_hard",

        "label":
            "Very Hard",

        "recommendation":
            "Very low altitude makes observation difficult."

    }


# =========================================================
# FINAL OBSERVABILITY
# =========================================================

def calculate_final_observability(

    altitude,

    cloud_cover,

    light_pollution="unknown"

):

    score = 0


    # =====================================================
    # ALTITUDE
    # =====================================================

    try:

        altitude = float(
            altitude
        )

    except Exception:

        altitude = None


    if altitude is not None:

        if altitude >= 60:

            score += 3

        elif altitude >= 40:

            score += 2.5

        elif altitude >= 30:

            score += 2

        elif altitude >= 20:

            score += 1


    # =====================================================
    # CLOUD
    # =====================================================

    cloud_info = get_cloud_quality(
        cloud_cover
    )

    score += cloud_info["score"]


    # =====================================================
    # LIGHT POLLUTION
    # =====================================================

    if light_pollution is None:

        lp = "unknown"

    else:

        lp = str(
            light_pollution
        ).strip().lower()


    if lp == "low":

        score += 2

    elif lp == "medium":

        score += 1

    elif lp == "high":

        score += 0


    # =====================================================
    # HEAVY CLOUD OVERRIDE
    # =====================================================

    if (
        cloud_cover is not None
        and cloud_cover >= 80
    ):

        return {

            "visible":
                False,

            "quality":
                "very_poor",

            "label":
                "Very Poor",

            "score":
                round(score, 1),

            "reason":
                "Heavy cloud cover is likely to block the constellation."

        }


    # =====================================================
    # FINAL QUALITY
    # =====================================================

    if score >= 7:

        quality = "excellent"

        label = "Excellent"


    elif score >= 5:

        quality = "good"

        label = "Good"


    elif score >= 3:

        quality = "fair"

        label = "Fair"


    elif score >= 1:

        quality = "poor"

        label = "Poor"


    else:

        quality = "very_poor"

        label = "Very Poor"


    # =====================================================
    # REASON
    # =====================================================

    if (
        cloud_cover is not None
        and cloud_cover > 60
    ):

        reason = (
            "The constellation is astronomically "
            "well placed, but high cloud cover may interfere."
        )

    elif lp == "high":

        reason = (
            "The constellation is above the horizon, "
            "but light pollution may reduce visibility."
        )

    elif altitude is not None and altitude >= 60:

        reason = (
            "High altitude provides a favorable "
            "position for observation."
        )

    elif altitude is not None and altitude >= 20:

        reason = (
            "The constellation is above the horizon "
            "and can be observed when sky conditions are favorable."
        )

    else:

        reason = (
            "Suitable observing conditions are required."
        )


    return {

        "visible":
            True,

        "quality":
            quality,

        "label":
            label,

        "score":
            round(score, 1),

        "reason":
            reason

    }


# =========================================================
# SPACE CATALOG
# =========================================================

def get_visible_constellations(

    latitude,

    longitude,

    start_local,

    end_local,

    cloud_cover,

    light_pollution="unknown"

):

    constellations = {}

    current = start_local


    # =====================================================
    # SAMPLE EVERY HOUR
    # =====================================================

    while current <= end_local:

        # -------------------------------------------------
        # LOCAL -> UTC
        # -------------------------------------------------

        utc_time = current.astimezone(
            timezone.utc
        )

        time_string = utc_time.strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )


        # -------------------------------------------------
        # SPACE CATALOG PARAMETERS
        # -------------------------------------------------

        params = {

            "lat":
                latitude,

            "lon":
                longitude,

            "time":
                time_string,

            "min_alt":
                20,

            "limit":
                100

        }


        response = None


        # =================================================
        # RETRY
        # =================================================

        for attempt in range(3):

            try:

                response = requests.get(

                    SPACE_CATALOG_URL,

                    params=params,

                    timeout=30

                )

                response.raise_for_status()

                break


            except (

                requests.exceptions.ConnectionError,

                requests.exceptions.Timeout

            ):

                if attempt == 2:

                    raise


        # =================================================
        # PARSE RESPONSE
        # =================================================

        data = response.json()


        if not isinstance(
            data,
            dict
        ):

            current += timedelta(
                hours=1
            )

            continue


        objects = data.get(
            "objects",
            []
        )


        if not isinstance(
            objects,
            list
        ):

            objects = []


        # =================================================
        # COLLECT CONSTELLATIONS
        # =================================================

        for obj in objects:

            if not isinstance(
                obj,
                dict
            ):

                continue


            constellation = obj.get(
                "constellation"
            )


            if not constellation:

                continue


            altitude = obj.get(
                "altitude_deg"
            )


            if altitude is None:

                continue


            try:

                altitude = float(
                    altitude
                )

            except (
                ValueError,
                TypeError
            ):

                continue


            # Only targets at least 20 degrees above horizon

            if altitude < 20:

                continue


            azimuth = obj.get(
                "azimuth_deg"
            )


            direction = obj.get(
                "bearing"
            )


            # =================================================
            # FIRST TIME
            # =================================================

            if constellation not in constellations:

                constellations[
                    constellation
                ] = {

                    "name":
                        constellation,

                    "visible":
                        True,

                    "best_time":
                        current.isoformat(),

                    "best_altitude":
                        altitude,

                    "azimuth":
                        azimuth,

                    "direction":
                        direction

                }


            # =================================================
            # UPDATE BEST POSITION
            # =================================================

            else:

                existing = constellations[
                    constellation
                ]


                existing_altitude = (
                    existing.get(
                        "best_altitude",
                        -999
                    )
                )


                if altitude > existing_altitude:

                    existing[
                        "best_altitude"
                    ] = altitude

                    existing[
                        "best_time"
                    ] = current.isoformat()

                    existing[
                        "azimuth"
                    ] = azimuth

                    existing[
                        "direction"
                    ] = direction


        current += timedelta(
            hours=1
        )


    # =====================================================
    # ADD DIFFICULTY + OBSERVABILITY
    # =====================================================

    result = []


    for constellation in constellations.values():

        altitude = constellation.get(
            "best_altitude"
        )


        # -------------------------------------------------
        # DIFFICULTY
        # -------------------------------------------------

        difficulty = calculate_difficulty(
            altitude
        )


        # -------------------------------------------------
        # FINAL OBSERVABILITY
        # -------------------------------------------------

        final_observability = (
            calculate_final_observability(

                altitude=
                    altitude,

                cloud_cover=
                    cloud_cover,

                light_pollution=
                    light_pollution

            )
        )


        constellation[
            "difficulty"
        ] = difficulty


        constellation[
            "final_observability"
        ] = final_observability


        # -------------------------------------------------
        # REQUIRED COMMON FIELDS
        # -------------------------------------------------

        constellation[
            "visible"
        ] = final_observability.get(
            "visible",
            True
        )


        constellation[
            "observability"
        ] = final_observability.get(
            "quality",
            "unknown"
        )


        constellation[
            "naked_eye"
        ] = True


        constellation[
            "recommendation"
        ] = difficulty.get(
            "recommendation",
            "Suitable for observation when sky conditions are favorable."
        )


        result.append(
            constellation
        )


    # =====================================================
    # SORT
    # =====================================================

    result.sort(

        key=lambda x: (

            x.get(
                "final_observability",
                {}
            ).get(
                "score",
                0
            ),

            x.get(
                "best_altitude",
                -999
            )

        ),

        reverse=True

    )


    # =====================================================
    # TOP RESULTS
    # =====================================================

    return result[
        :MAX_RESULTS
    ]


# =========================================================
# INTERNAL DATA FUNCTION
# =========================================================
#
# IMPORTANT:
# This function does NOT use FastAPI Query().
#
# observation.py must call THIS function.
#
# =========================================================

def get_constellations_data(

    latitude,

    longitude,

    from_date,

    to_date,

    from_time="20:00",

    to_time="02:00",

    light_pollution="unknown"

):

    # =====================================================
    # CLEAN INPUT
    # =====================================================

    from_date = str(
        from_date
    ).strip()

    to_date = str(
        to_date
    ).strip()

    from_time = str(
        from_time
    ).strip()

    to_time = str(
        to_time
    ).strip()


    if light_pollution is None:

        light_pollution = "unknown"

    else:

        light_pollution = str(
            light_pollution
        ).strip().lower()


    # =====================================================
    # DATETIME
    # =====================================================

    start_local = datetime.strptime(

        f"{from_date} {from_time}",

        "%Y-%m-%d %H:%M"

    ).replace(

        tzinfo=INDIA_TIMEZONE

    )


    end_local = datetime.strptime(

        f"{to_date} {to_time}",

        "%Y-%m-%d %H:%M"

    ).replace(

        tzinfo=INDIA_TIMEZONE

    )


    # =====================================================
    # VALIDATE DATE/TIME
    # =====================================================

    if end_local <= start_local:

        raise ValueError(
            "To date/time must be after From date/time"
        )


    # =====================================================
    # WEATHER
    # =====================================================

    weather = get_cloud_cover(

        latitude=
            latitude,

        longitude=
            longitude,

        start_local=
            start_local,

        end_local=
            end_local

    )


    cloud_cover = weather.get(
        "cloud_cover_percent"
    )


    # =====================================================
    # GET CONSTELLATIONS
    # =====================================================

    constellations = (
        get_visible_constellations(

            latitude=
                latitude,

            longitude=
                longitude,

            start_local=
                start_local,

            end_local=
                end_local,

            cloud_cover=
                cloud_cover,

            light_pollution=
                light_pollution

        )
    )


    # =====================================================
    # RESPONSE
    # =====================================================

    return {

        "success":
            True,

        "location": {

            "latitude":
                latitude,

            "longitude":
                longitude,

            "timezone":
                "Asia/Kolkata"

        },

        "observation": {

            "from_date":
                from_date,

            "to_date":
                to_date,

            "from_time":
                from_time,

            "to_time":
                to_time,

            "start_local":
                start_local.isoformat(),

            "end_local":
                end_local.isoformat()

        },

        "conditions": {

            "cloud_cover_percent":
                cloud_cover,

            "precipitation_probability_percent":
                weather.get(
                    "precipitation_probability_percent"
                ),

            "visibility_m":
                weather.get(
                    "visibility_m"
                ),

            "light_pollution":
                light_pollution

        },

        "filters": {

            "min_altitude":
                20,

            "max_results":
                MAX_RESULTS

        },

        "count":
            len(
                constellations
            ),

        "constellations":
            constellations,

        "message": (

            "No suitable constellations "
            "were found for the selected period."

            if not constellations

            else None

        ),

        "source": {

            "name":
                "SpaceCatalog.org",

            "url":
                "https://spacecatalog.org/api"

        }

    }


# =========================================================
# FASTAPI ROUTE
# =========================================================
#
# IMPORTANT:
# Query() is used ONLY here.
#
# =========================================================

@router.get("/constellations")
def get_constellations(

    latitude: float = Query(...),

    longitude: float = Query(...),

    from_date: str = Query(...),

    to_date: str = Query(...),

    from_time: str = Query("20:00"),

    to_time: str = Query("02:00"),

    light_pollution: str = Query("unknown")

):

    try:

        return get_constellations_data(

            latitude=
                latitude,

            longitude=
                longitude,

            from_date=
                from_date,

            to_date=
                to_date,

            from_time=
                from_time,

            to_time=
                to_time,

            light_pollution=
                light_pollution

        )


    except requests.exceptions.RequestException as e:

        return {

            "success":
                False,

            "error":
                "Unable to fetch constellation data",

            "details":
                str(e),

            "type":
                type(e).__name__

        }


    except Exception as e:

        return {

            "success":
                False,

            "error":
                str(e),

            "type":
                type(e).__name__

        }