# import astronomy
# from fastapi import APIRouter, Query
# from datetime import datetime, timezone, timedelta

# router = APIRouter()

# INDIA_TZ = timezone(timedelta(hours=5, minutes=30))


# def make_astro_time(dt):
#     """
#     Convert Python datetime to Astronomy Engine Time.
#     """

#     return astronomy.Time.Make(
#         dt.year,
#         dt.month,
#         dt.day,
#         dt.hour,
#         dt.minute,
#         dt.second
#     )


# @router.get("/astronomical-events")
# def get_astronomical_events(
#     latitude: float = Query(...),
#     longitude: float = Query(...),
#     from_date: str = Query(...),
#     to_date: str = Query(...),
#     from_time: str = Query("20:00"),
#     to_time: str = Query("02:00")
# ):

#     try:

#         # -----------------------------------------
#         # 1. Validate date and time
#         # -----------------------------------------

#         start_local = datetime.strptime(
#             f"{from_date} {from_time}",
#             "%Y-%m-%d %H:%M"
#         ).replace(tzinfo=INDIA_TZ)

#         end_local = datetime.strptime(
#             f"{to_date} {to_time}",
#             "%Y-%m-%d %H:%M"
#         ).replace(tzinfo=INDIA_TZ)

#         if end_local <= start_local:
#             return {
#                 "error": "To date/time must be after From date/time"
#             }

#         # -----------------------------------------
#         # 2. Convert to UTC
#         # -----------------------------------------

#         start_utc = start_local.astimezone(timezone.utc)
#         end_utc = end_local.astimezone(timezone.utc)

#         # -----------------------------------------
#         # 3. Astronomy Engine times
#         # -----------------------------------------

#         start_time = make_astro_time(start_utc)

#         observer = astronomy.Observer(
#             latitude,
#             longitude,
#             0
#         )

#         # -----------------------------------------
#         # 4. ECLIPSES
#         # -----------------------------------------

#         eclipses = []

#         # Solar eclipse
#         try:

#             solar = astronomy.SearchGlobalSolarEclipse(
#                 start_time
#             )

#             solar_datetime = datetime.fromisoformat(
#                 solar.peak.Utc().replace("Z", "+00:00")
#             )

#             if start_utc <= solar_datetime <= end_utc:

#                 eclipses.append({
#                     "type": "Solar Eclipse",
#                     "peak": solar_datetime.astimezone(
#                         INDIA_TZ
#                     ).strftime("%Y-%m-%d %H:%M"),
#                     "kind": str(solar.kind)
#                 })

#         except Exception:
#             pass

#         # Lunar eclipse
#         try:

#             lunar = astronomy.SearchLunarEclipse(
#                 start_time
#             )

#             lunar_datetime = datetime.fromisoformat(
#                 lunar.peak.Utc().replace("Z", "+00:00")
#             )

#             if start_utc <= lunar_datetime <= end_utc:

#                 eclipses.append({
#                     "type": "Lunar Eclipse",
#                     "peak": lunar_datetime.astimezone(
#                         INDIA_TZ
#                     ).strftime("%Y-%m-%d %H:%M"),
#                     "kind": str(lunar.kind)
#                 })

#         except Exception:
#             pass

#         # -----------------------------------------
#         # 5. CONJUNCTIONS
#         # -----------------------------------------

#         conjunctions = []

#         planets = [
#             astronomy.Body.Mercury,
#             astronomy.Body.Venus,
#             astronomy.Body.Mars,
#             astronomy.Body.Jupiter,
#             astronomy.Body.Saturn
#         ]

#         current_local = start_local

#         while current_local <= end_local:

#             current_utc = current_local.astimezone(
#                 timezone.utc
#             )

#             astro_time = make_astro_time(current_utc)

#             positions = {}

#             for planet in planets:

#                 try:

#                     eq = astronomy.Equator(
#                         planet,
#                         astro_time,
#                         observer,
#                         True,
#                         True
#                     )

#                     positions[planet] = (
#                         eq.ra,
#                         eq.dec
#                     )

#                 except Exception:
#                     pass

#             planet_list = list(positions.keys())

#             for i in range(len(planet_list)):

#                 for j in range(i + 1, len(planet_list)):

#                     p1 = planet_list[i]
#                     p2 = planet_list[j]

#                     ra1, dec1 = positions[p1]
#                     ra2, dec2 = positions[p2]

#                     try:

#                         separation = astronomy.AngleFromCoords(
#                             ra1,
#                             dec1,
#                             ra2,
#                             dec2
#                         )

#                         # Conjunction threshold
#                         if separation <= 1.0:

#                             conjunctions.append({
#                                 "date_time": current_local.strftime(
#                                     "%Y-%m-%d %H:%M"
#                                 ),
#                                 "object_1": p1.name,
#                                 "object_2": p2.name,
#                                 "separation_degrees": round(
#                                     separation,
#                                     3
#                                 )
#                             })

#                     except Exception:
#                         pass

#             current_local += timedelta(hours=1)

#         # Remove duplicate conjunctions
#         unique_conjunctions = []

#         seen = set()

#         for item in conjunctions:

#             key = (
#                 item["object_1"],
#                 item["object_2"],
#                 item["date_time"][:13]
#             )

#             if key not in seen:

#                 seen.add(key)

#                 unique_conjunctions.append(item)

#         # -----------------------------------------
#         # 6. OPPOSITIONS
#         # -----------------------------------------

#         oppositions = []

#         opposition_planets = [
#             astronomy.Body.Mars,
#             astronomy.Body.Jupiter,
#             astronomy.Body.Saturn
#         ]

#         current_local = start_local

#         while current_local <= end_local:

#             current_utc = current_local.astimezone(
#                 timezone.utc
#             )

#             astro_time = make_astro_time(current_utc)

#             try:

#                 sun = astronomy.Equator(
#                     astronomy.Body.Sun,
#                     astro_time,
#                     observer,
#                     True,
#                     True
#                 )

#             except Exception:
#                 current_local += timedelta(hours=1)
#                 continue

#             for planet in opposition_planets:

#                 try:

#                     eq = astronomy.Equator(
#                         planet,
#                         astro_time,
#                         observer,
#                         True,
#                         True
#                     )

#                     separation = astronomy.AngleFromCoords(
#                         sun.ra,
#                         sun.dec,
#                         eq.ra,
#                         eq.dec
#                     )

#                     # Near opposition
#                     if separation >= 179:

#                         oppositions.append({
#                             "date_time": current_local.strftime(
#                                 "%Y-%m-%d %H:%M"
#                             ),
#                             "planet": planet.name,
#                             "sun_planet_separation_degrees": round(
#                                 separation,
#                                 2
#                             )
#                         })

#                 except Exception:
#                     pass

#             current_local += timedelta(hours=1)

#         # -----------------------------------------
#         # 7. OCCULTATIONS
#         # -----------------------------------------

#         occultations = []

#         # Moon + planets close approach.
#         # Detailed occultation validation can be added later.

#         occultation_planets = [
#             astronomy.Body.Mercury,
#             astronomy.Body.Venus,
#             astronomy.Body.Mars,
#             astronomy.Body.Jupiter,
#             astronomy.Body.Saturn
#         ]

#         current_local = start_local

#         while current_local <= end_local:

#             current_utc = current_local.astimezone(
#                 timezone.utc
#             )

#             astro_time = make_astro_time(current_utc)

#             try:

#                 moon = astronomy.Equator(
#                     astronomy.Body.Moon,
#                     astro_time,
#                     observer,
#                     True,
#                     True
#                 )

#             except Exception:

#                 current_local += timedelta(hours=1)
#                 continue

#             for planet in occultation_planets:

#                 try:

#                     eq = astronomy.Equator(
#                         planet,
#                         astro_time,
#                         observer,
#                         True,
#                         True
#                     )

#                     separation = astronomy.AngleFromCoords(
#                         moon.ra,
#                         moon.dec,
#                         eq.ra,
#                         eq.dec
#                     )

#                     # Very close Moon/planet approach
#                     if separation <= 0.5:

#                         occultations.append({
#                             "date_time": current_local.strftime(
#                                 "%Y-%m-%d %H:%M"
#                             ),
#                             "object": planet.name,
#                             "moon_separation_degrees": round(
#                                 separation,
#                                 3
#                             )
#                         })

#                 except Exception:
#                     pass

#             current_local += timedelta(hours=1)

#         # -----------------------------------------
#         # 8. FINAL RESPONSE
#         # -----------------------------------------

#         return {

#             "location": {
#                 "latitude": latitude,
#                 "longitude": longitude
#             },

#             "observation": {
#                 "from_date": from_date,
#                 "to_date": to_date,
#                 "from_time": from_time,
#                 "to_time": to_time,
#                 "start_local": start_local.isoformat(),
#                 "end_local": end_local.isoformat()
#             },

#             "events": {

#                 "eclipses": eclipses,

#                 "conjunctions": unique_conjunctions,

#                 "oppositions": oppositions,

#                 "occultations": occultations
#             },

#             "source": {
#                 "name": "Astronomy Engine",
#                 "url": "https://github.com/cosinekitty/astronomy"
#             }
#         }

#     except ValueError as e:

#         return {
#             "error": "Invalid date/time format",
#             "details": str(e)
#         }

#     except Exception as e:

#         return {
#             "error": str(e),
#             "type": type(e).__name__
#         }

import astronomy

from fastapi import APIRouter, Query
from datetime import datetime, timezone, timedelta

router = APIRouter()

INDIA_TZ = timezone(timedelta(hours=5, minutes=30))

MAX_EVENTS = 10


# ============================================================
# ASTRONOMY ENGINE TIME
# ============================================================

def make_astro_time(dt):
    return astronomy.Time.Make(
        dt.year,
        dt.month,
        dt.day,
        dt.hour,
        dt.minute,
        dt.second
    )


# ============================================================
# DIFFICULTY
# ============================================================

def get_event_difficulty(event_type):

    if event_type == "Solar Eclipse":
        return {
            "level": "moderate",
            "label": "Moderate",
            "recommendation":
                "Requires a clear view of the Sun and proper solar viewing equipment."
        }

    if event_type == "Lunar Eclipse":
        return {
            "level": "easy",
            "label": "Easy",
            "recommendation":
                "Usually easy to observe with the naked eye when the Moon is above the horizon."
        }

    if event_type == "Conjunction":
        return {
            "level": "easy",
            "label": "Easy",
            "recommendation":
                "Generally easy to observe when the planets are above the horizon and the sky is clear."
        }

    if event_type == "Opposition":
        return {
            "level": "easy",
            "label": "Easy",
            "recommendation":
                "A favorable event for observing the planet because it is positioned opposite the Sun."
        }

    if event_type == "Occultation":
        return {
            "level": "hard",
            "label": "Hard",
            "recommendation":
                "Close timing and a clear sky are important because the event can be brief."
        }

    return {
        "level": "moderate",
        "label": "Moderate",
        "recommendation":
            "Suitable for observation when sky conditions are favorable."
    }


# ============================================================
# VISIBILITY / OBSERVABILITY
# ============================================================

def get_visibility(altitude, event_type):

    if altitude is None:

        return {
            "visible": False,
            "observability": "unknown",
            "label": "Unknown",
            "reason":
                "Altitude information is unavailable."
        }

    altitude = float(altitude)

    if altitude < 0:

        return {
            "visible": False,
            "observability": "not_visible",
            "label": "Not Visible",
            "reason":
                "The event's primary object is below the horizon."
        }

    if altitude < 10:

        return {
            "visible": True,
            "observability": "very_low",
            "label": "Very Low",
            "reason":
                "The event is above the horizon but very close to it."
        }

    if altitude < 20:

        return {
            "visible": True,
            "observability": "low",
            "label": "Low",
            "reason":
                "The event is visible but low above the horizon."
        }

    if altitude < 40:

        return {
            "visible": True,
            "observability": "good",
            "label": "Good",
            "reason":
                "The event is reasonably high above the horizon."
        }

    if altitude < 60:

        return {
            "visible": True,
            "observability": "very_good",
            "label": "Very Good",
            "reason":
                "The event is well positioned above the horizon."
        }

    return {
        "visible": True,
        "observability": "excellent",
        "label": "Excellent",
        "reason":
            "High altitude provides an excellent position for observation."
    }


# ============================================================
# EVENT OBSERVABILITY SCORE
# ============================================================

def get_event_score(
    altitude,
    event_type
):

    score = 0

    if altitude is not None:

        altitude = float(altitude)

        if altitude >= 60:
            score += 5

        elif altitude >= 40:
            score += 4

        elif altitude >= 20:
            score += 3

        elif altitude >= 10:
            score += 2

        elif altitude >= 0:
            score += 1

    difficulty = get_event_difficulty(event_type)

    if difficulty["level"] == "easy":
        score += 2

    elif difficulty["level"] == "moderate":
        score += 1

    return round(score, 1)


# ============================================================
# ECLIPSES
# ============================================================

def find_eclipses(
    start_time,
    start_utc,
    end_utc,
    observer
):

    events = []

    # --------------------------------------------------------
    # SOLAR ECLIPSE
    # --------------------------------------------------------

    try:

        solar = astronomy.SearchGlobalSolarEclipse(
            start_time
        )

        peak_utc = datetime.fromisoformat(
            solar.peak.Utc().replace("Z", "+00:00")
        )

        if start_utc <= peak_utc <= end_utc:

            events.append({
                "type": "Solar Eclipse",
                "peak": peak_utc.astimezone(
                    INDIA_TZ
                ).strftime("%Y-%m-%d %H:%M"),
                "kind": str(solar.kind),
                "event_time_utc": peak_utc,
                "altitude": None
            })

    except Exception:
        pass


    # --------------------------------------------------------
    # LUNAR ECLIPSE
    # --------------------------------------------------------

    try:

        lunar = astronomy.SearchLunarEclipse(
            start_time
        )

        peak_utc = datetime.fromisoformat(
            lunar.peak.Utc().replace("Z", "+00:00")
        )

        if start_utc <= peak_utc <= end_utc:

            events.append({
                "type": "Lunar Eclipse",
                "peak": peak_utc.astimezone(
                    INDIA_TZ
                ).strftime("%Y-%m-%d %H:%M"),
                "kind": str(lunar.kind),
                "event_time_utc": peak_utc,
                "altitude": None
            })

    except Exception:
        pass

    return events


# ============================================================
# CONJUNCTIONS
# ============================================================

def find_conjunctions(
    start_local,
    end_local,
    observer
):

    results = []

    planets = [
        astronomy.Body.Mercury,
        astronomy.Body.Venus,
        astronomy.Body.Mars,
        astronomy.Body.Jupiter,
        astronomy.Body.Saturn
    ]

    current_local = start_local

    while current_local <= end_local:

        current_utc = current_local.astimezone(
            timezone.utc
        )

        astro_time = make_astro_time(current_utc)

        positions = {}

        for planet in planets:

            try:

                eq = astronomy.Equator(
                    planet,
                    astro_time,
                    observer,
                    True,
                    True
                )

                positions[planet] = (
                    eq.ra,
                    eq.dec
                )

            except Exception:
                pass


        planet_list = list(positions.keys())

        for i in range(len(planet_list)):

            for j in range(i + 1, len(planet_list)):

                p1 = planet_list[i]
                p2 = planet_list[j]

                try:

                    ra1, dec1 = positions[p1]
                    ra2, dec2 = positions[p2]

                    separation = astronomy.AngleFromCoords(
                        ra1,
                        dec1,
                        ra2,
                        dec2
                    )

                    # Conjunction threshold
                    if separation <= 1.0:

                        results.append({

                            "type": "Conjunction",

                            "date_time":
                                current_local.strftime(
                                    "%Y-%m-%d %H:%M"
                                ),

                            "object_1":
                                p1.name,

                            "object_2":
                                p2.name,

                            "separation_degrees":
                                round(
                                    separation,
                                    3
                                ),

                            "altitude":
                                None
                        })

                except Exception:
                    pass

        current_local += timedelta(
            minutes=15
        )

    return results


# ============================================================
# OPPOSITIONS
# ============================================================

def find_oppositions(
    start_local,
    end_local,
    observer
):

    results = []

    planets = [
        astronomy.Body.Mars,
        astronomy.Body.Jupiter,
        astronomy.Body.Saturn
    ]

    current_local = start_local

    while current_local <= end_local:

        current_utc = current_local.astimezone(
            timezone.utc
        )

        astro_time = make_astro_time(
            current_utc
        )

        try:

            sun = astronomy.Equator(
                astronomy.Body.Sun,
                astro_time,
                observer,
                True,
                True
            )

        except Exception:

            current_local += timedelta(
                minutes=15
            )

            continue


        for planet in planets:

            try:

                eq = astronomy.Equator(
                    planet,
                    astro_time,
                    observer,
                    True,
                    True
                )

                separation = astronomy.AngleFromCoords(
                    sun.ra,
                    sun.dec,
                    eq.ra,
                    eq.dec
                )

                if separation >= 179:

                    results.append({

                        "type": "Opposition",

                        "date_time":
                            current_local.strftime(
                                "%Y-%m-%d %H:%M"
                            ),

                        "planet":
                            planet.name,

                        "sun_planet_separation_degrees":
                            round(
                                separation,
                                2
                            ),

                        "altitude":
                            None
                    })

            except Exception:
                pass

        current_local += timedelta(
            minutes=15
        )

    return results


# ============================================================
# OCCULTATIONS
# ============================================================

def find_occultations(
    start_local,
    end_local,
    observer
):

    results = []

    planets = [
        astronomy.Body.Mercury,
        astronomy.Body.Venus,
        astronomy.Body.Mars,
        astronomy.Body.Jupiter,
        astronomy.Body.Saturn
    ]

    current_local = start_local

    while current_local <= end_local:

        current_utc = current_local.astimezone(
            timezone.utc
        )

        astro_time = make_astro_time(
            current_utc
        )

        try:

            moon = astronomy.Equator(
                astronomy.Body.Moon,
                astro_time,
                observer,
                True,
                True
            )

        except Exception:

            current_local += timedelta(
                minutes=15
            )

            continue


        for planet in planets:

            try:

                eq = astronomy.Equator(
                    planet,
                    astro_time,
                    observer,
                    True,
                    True
                )

                separation = astronomy.AngleFromCoords(
                    moon.ra,
                    moon.dec,
                    eq.ra,
                    eq.dec
                )

                if separation <= 0.5:

                    results.append({

                        "type": "Occultation",

                        "date_time":
                            current_local.strftime(
                                "%Y-%m-%d %H:%M"
                            ),

                        "object":
                            planet.name,

                        "moon_separation_degrees":
                            round(
                                separation,
                                3
                            ),

                        "altitude":
                            None
                    })

            except Exception:
                pass

        current_local += timedelta(
            minutes=15
        )

    return results


# ============================================================
# MAIN API
# ============================================================

@router.get("/astronomical-events")
def get_astronomical_events(

    latitude: float = Query(...),

    longitude: float = Query(...),

    from_date: str = Query(...),

    to_date: str = Query(...),

    from_time: str = Query("20:00"),

    to_time: str = Query("02:00")

):

    try:

        # ====================================================
        # DATE / TIME
        # ====================================================

        start_local = datetime.strptime(
            f"{from_date} {from_time}",
            "%Y-%m-%d %H:%M"
        ).replace(
            tzinfo=INDIA_TZ
        )

        end_local = datetime.strptime(
            f"{to_date} {to_time}",
            "%Y-%m-%d %H:%M"
        ).replace(
            tzinfo=INDIA_TZ
        )

        if end_local <= start_local:

            return {
                "success": False,
                "error":
                    "To date/time must be after From date/time"
            }


        # ====================================================
        # UTC
        # ====================================================

        start_utc = start_local.astimezone(
            timezone.utc
        )

        end_utc = end_local.astimezone(
            timezone.utc
        )


        # ====================================================
        # ASTRONOMY ENGINE
        # ====================================================

        start_time = make_astro_time(
            start_utc
        )

        observer = astronomy.Observer(
            latitude,
            longitude,
            0
        )


        # ====================================================
        # FIND EVENTS
        # ====================================================

        eclipses = find_eclipses(
            start_time,
            start_utc,
            end_utc,
            observer
        )

        conjunctions = find_conjunctions(
            start_local,
            end_local,
            observer
        )

        oppositions = find_oppositions(
            start_local,
            end_local,
            observer
        )

        occultations = find_occultations(
            start_local,
            end_local,
            observer
        )


        # ====================================================
        # COMBINE EVENTS
        # ====================================================

        all_events = []

        all_events.extend(
            eclipses
        )

        all_events.extend(
            conjunctions
        )

        all_events.extend(
            oppositions
        )

        all_events.extend(
            occultations
        )


        # ====================================================
        # ADD DIFFICULTY + OBSERVABILITY
        # ====================================================

        final_events = []

        for event in all_events:

            event_type = event.get(
                "type",
                "Astronomical Event"
            )

            altitude = event.get(
                "altitude"
            )

            difficulty = get_event_difficulty(
                event_type
            )

            visibility = get_visibility(
                altitude,
                event_type
            )

            score = get_event_score(
                altitude,
                event_type
            )

            event["difficulty"] = difficulty

            event["visibility"] = visibility

            event["observability_score"] = score

            # Remove internal value
            event.pop(
                "event_time_utc",
                None
            )

            final_events.append(
                event
            )


        # ====================================================
        # REMOVE DUPLICATES
        # ====================================================

        unique_events = []

        seen = set()

        for event in final_events:

            key = (
                event.get("type"),
                event.get("date_time"),
                event.get("object"),
                event.get("object_1"),
                event.get("object_2"),
                event.get("planet")
            )

            if key in seen:
                continue

            seen.add(key)

            unique_events.append(
                event
            )


        # ====================================================
        # SORT
        # ====================================================

        unique_events.sort(
            key=lambda x:
                x.get(
                    "observability_score",
                    0
                ),
            reverse=True
        )


        # ====================================================
        # LIMIT
        # ====================================================

        unique_events = unique_events[
            :MAX_EVENTS
        ]


        # ====================================================
        # SEPARATE BY TYPE
        # ====================================================

        eclipse_results = [
            e for e in unique_events
            if e["type"] in [
                "Solar Eclipse",
                "Lunar Eclipse"
            ]
        ]

        conjunction_results = [
            e for e in unique_events
            if e["type"] == "Conjunction"
        ]

        opposition_results = [
            e for e in unique_events
            if e["type"] == "Opposition"
        ]

        occultation_results = [
            e for e in unique_events
            if e["type"] == "Occultation"
        ]


        # ====================================================
        # FINAL RESPONSE
        # ====================================================

        return {

            "success": True,

            "location": {
                "latitude": latitude,
                "longitude": longitude
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

            "count":
                len(unique_events),

            "events": {

                "eclipses":
                    eclipse_results,

                "conjunctions":
                    conjunction_results,

                "oppositions":
                    opposition_results,

                "occultations":
                    occultation_results
            },

            "message":
                (
                    "No astronomical events occur "
                    "during the selected observation period."
                    if not unique_events
                    else None
                ),

            "source": {

                "name":
                    "Astronomy Engine",

                "url":
                    "https://github.com/cosinekitty/astronomy"
            }
        }


    except ValueError as e:

        return {

            "success": False,

            "error":
                "Invalid date/time format",

            "details":
                str(e)
        }


    except Exception as e:

        return {

            "success": False,

            "error":
                str(e),

            "type":
                type(e).__name__
        }