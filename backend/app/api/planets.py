# import astronomy

# from datetime import datetime, timedelta
# from fastapi import APIRouter, Query

# router = APIRouter()


# PLANETS = [
#     astronomy.Body.Mercury,
#     astronomy.Body.Venus,
#     astronomy.Body.Mars,
#     astronomy.Body.Jupiter,
#     astronomy.Body.Saturn,
#     astronomy.Body.Uranus,
#     astronomy.Body.Neptune
# ]


# PLANET_NAMES = {
#     astronomy.Body.Mercury: "Mercury",
#     astronomy.Body.Venus: "Venus",
#     astronomy.Body.Mars: "Mars",
#     astronomy.Body.Jupiter: "Jupiter",
#     astronomy.Body.Saturn: "Saturn",
#     astronomy.Body.Uranus: "Uranus",
#     astronomy.Body.Neptune: "Neptune"
# }


# def get_altitude_category(altitude):
#     """
#     Classify the planet according to altitude above horizon.
#     """

#     if altitude < 0:
#         return "below_horizon"

#     if altitude < 10:
#         return "very_low"

#     if altitude < 20:
#         return "low"

#     if altitude < 40:
#         return "observable"

#     return "excellent"


# def get_planet_observability(planet_name, altitude):
#     """
#     Give practical observing guidance.
#     """

#     # Below horizon
#     if altitude < 0:
#         return {
#             "observability": "not_visible",
#             "naked_eye": False,
#             "difficulty": "not_visible",
#             "recommendation": "Below the horizon during the selected observation period."
#         }

#     # Uranus and Neptune are not practical naked-eye targets.
#     if planet_name == "Neptune":
#         return {
#             "observability": "telescope_required",
#             "naked_eye": False,
#             "difficulty": "very_hard",
#             "recommendation": "Telescope required. Neptune is a very difficult visual target."
#         }

#     if planet_name == "Uranus":
#         return {
#             "observability": "telescope_recommended",
#             "naked_eye": False,
#             "difficulty": "hard",
#             "recommendation": "Best observed with binoculars or a telescope."
#         }

#     # Mercury
#     if planet_name == "Mercury":
#         if altitude < 10:
#             return {
#                 "observability": "very_low",
#                 "naked_eye": True,
#                 "difficulty": "difficult",
#                 "recommendation": "Bright but very low above the horizon. A clear horizon is important."
#             }

#     # Venus
#     if planet_name == "Venus":
#         if altitude < 10:
#             return {
#                 "observability": "very_low",
#                 "naked_eye": True,
#                 "difficulty": "easy_but_low",
#                 "recommendation": "Very bright but very low above the horizon."
#             }

#         return {
#             "observability": "easy",
#             "naked_eye": True,
#             "difficulty": "easy",
#             "recommendation": "Excellent naked-eye target."
#         }

#     # Mars / Jupiter / Saturn
#     if planet_name in ["Mars", "Jupiter", "Saturn"]:

#         if altitude < 10:
#             return {
#                 "observability": "very_low",
#                 "naked_eye": True,
#                 "difficulty": "difficult",
#                 "recommendation": "Above the horizon but very low. Atmospheric effects may reduce visibility."
#             }

#         if altitude < 20:
#             return {
#                 "observability": "low",
#                 "naked_eye": True,
#                 "difficulty": "moderate",
#                 "recommendation": "Visible, but higher altitude would provide a better view."
#             }

#         if altitude < 40:
#             return {
#                 "observability": "good",
#                 "naked_eye": True,
#                 "difficulty": "easy",
#                 "recommendation": "Good naked-eye target and suitable for telescope observation."
#             }

#         return {
#             "observability": "excellent",
#             "naked_eye": True,
#             "difficulty": "easy",
#             "recommendation": "Excellent target. High altitude provides good observing conditions."
#         }

#     return {
#         "observability": get_altitude_category(altitude),
#         "naked_eye": False,
#         "difficulty": "unknown",
#         "recommendation": "Observable during the selected period."
#     }


# def get_planets_data(
#     latitude,
#     longitude,
#     from_date,
#     to_date,
#     from_time,
#     to_time
# ):

#     start_dt = datetime.strptime(
#         f"{from_date} {from_time}",
#         "%Y-%m-%d %H:%M"
#     )

#     end_dt = datetime.strptime(
#         f"{to_date} {to_time}",
#         "%Y-%m-%d %H:%M"
#     )

#     if end_dt <= start_dt:
#         raise ValueError(
#             "To date/time must be after From date/time"
#         )

#     observer = astronomy.Observer(
#         latitude,
#         longitude,
#         0
#     )

#     visible_planets = []

#     for body in PLANETS:

#         planet_name = PLANET_NAMES[body]

#         current = start_dt

#         best_altitude = -90
#         best_azimuth = None
#         best_time = None
#         best_distance = None

#         while current <= end_dt:

#             astro_time = astronomy.Time(
#                 current.year,
#                 current.month,
#                 current.day,
#                 current.hour,
#                 current.minute,
#                 current.second
#             )

#             equator = astronomy.Equator(
#                 body,
#                 astro_time,
#                 observer,
#                 True,
#                 True
#             )

#             horizon = astronomy.Horizon(
#                 astro_time,
#                 observer,
#                 equator.ra,
#                 equator.dec,
#                 "normal"
#             )

#             altitude = horizon.altitude
#             azimuth = horizon.azimuth

#             if altitude > best_altitude:

#                 best_altitude = altitude
#                 best_azimuth = azimuth
#                 best_time = current

#                 try:
#                     vector = astronomy.GeoVector(
#                         body,
#                         astro_time,
#                         True
#                     )

#                     best_distance = vector.dist

#                 except Exception:
#                     best_distance = None

#             current += timedelta(minutes=15)

#         # --------------------------------------------------
#         # IMPORTANT
#         # Only planets above the horizon are returned.
#         # --------------------------------------------------

#         if best_altitude < 0:
#             continue

#         observability = get_planet_observability(
#             planet_name,
#             best_altitude
#         )

#         visible_planets.append({

#             "planet": planet_name,

#             "rise_time": None,

#             "best_time": best_time.strftime(
#                 "%Y-%m-%d %H:%M"
#             ) if best_time else None,

#             "best_altitude": round(
#                 best_altitude,
#                 2
#             ),

#             "best_azimuth": round(
#                 best_azimuth,
#                 2
#             ) if best_azimuth is not None else None,

#             "distance_au": round(
#                 best_distance,
#                 6
#             ) if best_distance is not None else None,

#             "visible": True,

#             "altitude_category": get_altitude_category(
#                 best_altitude
#             ),

#             "observability": observability["observability"],

#             "naked_eye": observability["naked_eye"],

#             "difficulty": observability["difficulty"],

#             "recommendation": observability["recommendation"]
#         })

#     # Highest altitude first
#     visible_planets.sort(
#         key=lambda x: x["best_altitude"],
#         reverse=True
#     )

#     return visible_planets


# @router.get("/planets")
# def get_planets(
#     latitude: float = Query(...),
#     longitude: float = Query(...),
#     from_date: str = Query(...),
#     to_date: str = Query(...),
#     from_time: str = Query("20:00"),
#     to_time: str = Query("02:00")
# ):

#     try:

#         planets = get_planets_data(
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )

#         return {
#             "success": True,

#             "location": {
#                 "latitude": latitude,
#                 "longitude": longitude
#             },

#             "observation": {
#                 "from_date": from_date,
#                 "to_date": to_date,
#                 "from_time": from_time,
#                 "to_time": to_time
#             },

#             "count": len(planets),

#             "planets": planets,

#             "message": (
#                 "No planets are visible during the selected "
#                 "observation period."
#                 if not planets
#                 else None
#             ),

#             "source": {
#                 "name": "Astronomy Engine",
#                 "url": "https://github.com/cosinekitty/astronomy"
#             }
#         }

#     except Exception as e:

#         return {
#             "success": False,
#             "error": str(e),
#             "type": type(e).__name__
#         }


import astronomy

from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Query

router = APIRouter()


# ============================================================
# PLANETS
# ============================================================

PLANETS = [
    astronomy.Body.Mercury,
    astronomy.Body.Venus,
    astronomy.Body.Mars,
    astronomy.Body.Jupiter,
    astronomy.Body.Saturn,
    astronomy.Body.Uranus,
    astronomy.Body.Neptune,
]


PLANET_NAMES = {
    astronomy.Body.Mercury: "Mercury",
    astronomy.Body.Venus: "Venus",
    astronomy.Body.Mars: "Mars",
    astronomy.Body.Jupiter: "Jupiter",
    astronomy.Body.Saturn: "Saturn",
    astronomy.Body.Uranus: "Uranus",
    astronomy.Body.Neptune: "Neptune",
}


# ============================================================
# ALTITUDE CATEGORY
# ============================================================

def get_altitude_category(altitude):

    if altitude < 0:
        return "below_horizon"

    if altitude < 10:
        return "very_low"

    if altitude < 20:
        return "low"

    if altitude < 40:
        return "observable"

    return "excellent"


# ============================================================
# OBSERVABILITY
# ============================================================

def get_planet_observability(planet_name, altitude):

    if altitude < 0:

        return {
            "observability": "not_visible",
            "naked_eye": False,
            "difficulty": {
                "level": "not_visible",
                "label": "Not Visible"
            },
            "recommendation":
                "Below the horizon during the selected observation period."
        }

    # Neptune
    if planet_name == "Neptune":

        return {
            "observability": "telescope_required",
            "naked_eye": False,
            "difficulty": {
                "level": "very_hard",
                "label": "Very Hard"
            },
            "recommendation":
                "Telescope required. Neptune is a very difficult visual target."
        }

    # Uranus
    if planet_name == "Uranus":

        return {
            "observability": "telescope_recommended",
            "naked_eye": False,
            "difficulty": {
                "level": "hard",
                "label": "Hard"
            },
            "recommendation":
                "Best observed with binoculars or a telescope."
        }

    # Mercury
    if planet_name == "Mercury":

        if altitude < 10:

            return {
                "observability": "very_low",
                "naked_eye": True,
                "difficulty": {
                    "level": "difficult",
                    "label": "Difficult"
                },
                "recommendation":
                    "Bright but very low above the horizon. A clear horizon is important."
            }

        if altitude < 20:

            return {
                "observability": "low",
                "naked_eye": True,
                "difficulty": {
                    "level": "moderate",
                    "label": "Moderate"
                },
                "recommendation":
                    "Visible above the horizon, but higher altitude would provide better viewing."
            }

        return {
            "observability": "good",
            "naked_eye": True,
            "difficulty": {
                "level": "moderate",
                "label": "Moderate"
            },
            "recommendation":
                "Visible to the naked eye. A clear horizon and good atmospheric conditions are helpful."
        }

    # Venus
    if planet_name == "Venus":

        if altitude < 10:

            return {
                "observability": "very_low",
                "naked_eye": True,
                "difficulty": {
                    "level": "easy_but_low",
                    "label": "Easy but Low"
                },
                "recommendation":
                    "Very bright but very low above the horizon."
            }

        return {
            "observability": "easy",
            "naked_eye": True,
            "difficulty": {
                "level": "easy",
                "label": "Easy"
            },
            "recommendation":
                "Excellent naked-eye target."
        }

    # Mars / Jupiter / Saturn
    if planet_name in ["Mars", "Jupiter", "Saturn"]:

        if altitude < 10:

            return {
                "observability": "very_low",
                "naked_eye": True,
                "difficulty": {
                    "level": "difficult",
                    "label": "Difficult"
                },
                "recommendation":
                    "Above the horizon but very low. Atmospheric effects may reduce visibility."
            }

        if altitude < 20:

            return {
                "observability": "low",
                "naked_eye": True,
                "difficulty": {
                    "level": "moderate",
                    "label": "Moderate"
                },
                "recommendation":
                    "Visible, but higher altitude would provide a better view."
            }

        if altitude < 40:

            return {
                "observability": "good",
                "naked_eye": True,
                "difficulty": {
                    "level": "easy",
                    "label": "Easy"
                },
                "recommendation":
                    "Good naked-eye target and suitable for telescope observation."
            }

        return {
            "observability": "excellent",
            "naked_eye": True,
            "difficulty": {
                "level": "easy",
                "label": "Easy"
            },
            "recommendation":
                "Excellent target. High altitude provides good observing conditions."
        }

    # Fallback
    return {
        "observability": get_altitude_category(altitude),
        "naked_eye": False,
        "difficulty": {
            "level": "unknown",
            "label": "Unknown"
        },
        "recommendation":
            "Observable during the selected observation period."
    }


# ============================================================
# INTERNAL DATA FUNCTION
# ============================================================

def get_planets_data(
    latitude,
    longitude,
    from_date,
    to_date,
    from_time,
    to_time
):

    # --------------------------------------------------------
    # Parse local date/time
    # --------------------------------------------------------

    start_dt = datetime.strptime(
        f"{from_date} {from_time}",
        "%Y-%m-%d %H:%M"
    )

    end_dt = datetime.strptime(
        f"{to_date} {to_time}",
        "%Y-%m-%d %H:%M"
    )

    # --------------------------------------------------------
    # Handle same-date overnight observation
    #
    # Example:
    # 2026-09-10 20:00
    # to
    # 2026-09-10 02:00
    #
    # means next morning.
    # --------------------------------------------------------

    if end_dt <= start_dt:

        if from_date == to_date:

            end_dt = end_dt + timedelta(days=1)

        else:

            raise ValueError(
                "To date/time must be after From date/time"
            )

    # --------------------------------------------------------
    # Observer
    # --------------------------------------------------------

    observer = astronomy.Observer(
        latitude,
        longitude,
        0
    )

    visible_planets = []

    # ========================================================
    # LOOP PLANETS
    # ========================================================

    for body in PLANETS:

        planet_name = PLANET_NAMES[body]

        current = start_dt

        best_altitude = -90
        best_azimuth = None
        best_time = None
        best_distance = None

        # ====================================================
        # 15 minute sampling
        # ====================================================

        while current <= end_dt:

            # ------------------------------------------------
            # Convert India local time to UTC
            # ------------------------------------------------

            local_time = current.replace(
                tzinfo=timezone(
                    timedelta(
                        hours=5,
                        minutes=30
                    )
                )
            )

            utc_time = local_time.astimezone(
                timezone.utc
            )

            # ------------------------------------------------
            # Astronomy Engine Time
            # ------------------------------------------------

            astro_time = astronomy.Time(
                utc_time.strftime(
                    "%Y-%m-%dT%H:%M:%SZ"
                )
            )

            # ------------------------------------------------
            # Get equatorial coordinates
            # ------------------------------------------------

            equator = astronomy.Equator(
                body,
                astro_time,
                observer,
                True,
                True
            )

            # ------------------------------------------------
            # Convert RA/DEC -> Altitude/Azimuth
            #
            # IMPORTANT:
            # No EquatorEpoch.
            # No "normal" string.
            # ------------------------------------------------

            horizon = astronomy.Horizon(
                astro_time,
                observer,
                equator.ra,
                equator.dec,
                astronomy.Refraction.Normal
            )

            altitude = horizon.altitude
            azimuth = horizon.azimuth

            # ------------------------------------------------
            # Find maximum altitude
            # ------------------------------------------------

            if altitude > best_altitude:

                best_altitude = altitude

                best_azimuth = azimuth

                best_time = current

                # ------------------------------------------------
                # Distance from Earth
                # ------------------------------------------------

                try:

                    vector = astronomy.GeoVector(
                        body,
                        astro_time,
                        True
                    )

                    best_distance = vector.dist

                except Exception:

                    best_distance = None

            current += timedelta(
                minutes=15
            )

        # ====================================================
        # Planet never above horizon
        # ====================================================

        if best_altitude < 0:

            continue

        # ====================================================
        # Observability
        # ====================================================

        observability = get_planet_observability(
            planet_name,
            best_altitude
        )

        # ====================================================
        # Result
        # ====================================================

        visible_planets.append({

            "planet": planet_name,

            "rise_time": None,

            "set_time": None,

            "best_time": (
                best_time.strftime(
                    "%Y-%m-%d %H:%M"
                )
                if best_time
                else None
            ),

            "best_altitude": round(
                best_altitude,
                2
            ),

            "best_azimuth": (
                round(
                    best_azimuth,
                    2
                )
                if best_azimuth is not None
                else None
            ),

            "distance_au": (
                round(
                    best_distance,
                    6
                )
                if best_distance is not None
                else None
            ),

            "visible": True,

            "altitude_category":
                get_altitude_category(
                    best_altitude
                ),

            "observability":
                observability[
                    "observability"
                ],

            "naked_eye":
                observability[
                    "naked_eye"
                ],

            "difficulty":
                observability[
                    "difficulty"
                ],

            "recommendation":
                observability[
                    "recommendation"
                ]
        })

    # ========================================================
    # Sort highest altitude first
    # ========================================================

    visible_planets.sort(
        key=lambda x: x["best_altitude"],
        reverse=True
    )

    return visible_planets


# ============================================================
# API ENDPOINT
# ============================================================

@router.get("/planets")
def get_planets(

    latitude: float = Query(...),

    longitude: float = Query(...),

    from_date: str = Query(...),

    to_date: str = Query(...),

    from_time: str = Query("20:00"),

    to_time: str = Query("02:00")
):

    try:

        planets = get_planets_data(

            latitude=latitude,

            longitude=longitude,

            from_date=from_date,

            to_date=to_date,

            from_time=from_time,

            to_time=to_time
        )

        return {

            "success": True,

            "location": {
                "latitude": latitude,
                "longitude": longitude
            },

            "observation": {

                "from_date": from_date,

                "to_date": to_date,

                "from_time": from_time,

                "to_time": to_time
            },

            "count": len(planets),

            "planets": planets,

            "message": (
                "No planets are visible during the selected observation period."
                if not planets
                else None
            ),

            "source": {

                "name": "Astronomy Engine",

                "url":
                    "https://github.com/cosinekitty/astronomy"
            }
        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e),

            "type": type(e).__name__
        }