# import requests

# from fastapi import APIRouter, Query

# from datetime import datetime, timezone, timedelta


# router = APIRouter()


# # =========================================================
# # API
# # =========================================================

# BASE_URL = "https://spacecatalog.org/api/v1"

# WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


# # =========================================================
# # CONSTANTS
# # =========================================================

# INDIA_TIMEZONE = timezone(
#     timedelta(hours=5, minutes=30)
# )

# MAX_RESULTS = 10


# # =========================================================
# # DIFFICULTY
# # =========================================================

# def calculate_difficulty(
#     magnitude,
#     altitude,
#     category
# ):

#     try:

#         magnitude = float(
#             magnitude
#         )

#     except Exception:

#         magnitude = None


#     try:

#         altitude = float(
#             altitude
#         )

#     except Exception:

#         altitude = None


#     category = (
#         str(category).lower()
#         if category
#         else ""
#     )


#     # =====================================================
#     # VERY LOW ALTITUDE
#     # =====================================================

#     if altitude is not None and altitude < 20:

#         return {

#             "level":
#                 "very_hard",

#             "label":
#                 "Very Hard",

#             "recommendation":
#                 "Low altitude makes this target difficult to observe."

#         }


#     # =====================================================
#     # MAGNITUDE
#     # =====================================================

#     if magnitude is not None:

#         # -----------------------------------------------
#         # Bright
#         # -----------------------------------------------

#         if magnitude <= 6:

#             if (
#                 altitude is not None
#                 and altitude >= 40
#             ):

#                 return {

#                     "level":
#                         "easy",

#                     "label":
#                         "Easy",

#                     "recommendation":
#                         "Good target for beginner observers and small telescopes."

#                 }


#             return {

#                 "level":
#                     "moderate",

#                 "label":
#                     "Moderate",

#                 "recommendation":
#                     "Bright target, but higher altitude would improve observation."

#             }


#         # -----------------------------------------------
#         # Medium
#         # -----------------------------------------------

#         if magnitude <= 8:

#             if (
#                 altitude is not None
#                 and altitude >= 40
#             ):

#                 return {

#                     "level":
#                         "moderate",

#                     "label":
#                         "Moderate",

#                     "recommendation":
#                         "Good telescope target under reasonably dark skies."

#                 }


#             return {

#                 "level":
#                     "hard",

#                 "label":
#                     "Hard",

#                 "recommendation":
#                     "Requires a telescope and reasonably dark skies."

#             }


#         # -----------------------------------------------
#         # Faint
#         # -----------------------------------------------

#         if magnitude <= 10:

#             return {

#                 "level":
#                     "hard",

#                 "label":
#                     "Hard",

#                 "recommendation":
#                     "Faint target. Telescope and dark skies are recommended."

#             }


#         # -----------------------------------------------
#         # Very faint
#         # -----------------------------------------------

#         return {

#             "level":
#                 "very_hard",

#             "label":
#                 "Very Hard",

#             "recommendation":
#                 "Very faint target. Requires a good telescope and dark skies."

#         }


#     # =====================================================
#     # CATEGORY FALLBACK
#     # =====================================================

#     if category == "galaxy":

#         return {

#             "level":
#                 "hard",

#             "label":
#                 "Hard",

#             "recommendation":
#                 "Galaxies benefit strongly from dark skies and telescope observation."

#         }


#     if category == "nebula":

#         return {

#             "level":
#                 "moderate",

#             "label":
#                 "Moderate",

#             "recommendation":
#                 "Best observed with a telescope under dark skies."

#         }


#     if category == "cluster":

#         return {

#             "level":
#                 "easy",

#             "label":
#                 "Easy",

#             "recommendation":
#                 "Generally a good target for beginner observers."

#         }


#     return {

#         "level":
#             "moderate",

#         "label":
#             "Moderate",

#         "recommendation":
#             "Suitable for telescope observation under good sky conditions."

#     }


# # =========================================================
# # CLOUD QUALITY
# # =========================================================

# def get_cloud_quality(
#     cloud_cover
# ):

#     if cloud_cover is None:

#         return {

#             "level":
#                 "unknown",

#             "label":
#                 "Unknown",

#             "score":
#                 0,

#             "reason":
#                 "Cloud information is unavailable."

#         }


#     if cloud_cover <= 10:

#         return {

#             "level":
#                 "excellent",

#             "label":
#                 "Excellent",

#             "score":
#                 4,

#             "reason":
#                 "Very low cloud cover."

#         }


#     if cloud_cover <= 30:

#         return {

#             "level":
#                 "good",

#             "label":
#                 "Good",

#             "score":
#                 3,

#             "reason":
#                 "Low cloud cover."

#         }


#     if cloud_cover <= 60:

#         return {

#             "level":
#                 "fair",

#             "label":
#                 "Fair",

#             "score":
#                 2,

#             "reason":
#                 "Some cloud cover may interfere with observation."

#         }


#     if cloud_cover <= 80:

#         return {

#             "level":
#                 "poor",

#             "label":
#                 "Poor",

#             "score":
#                 1,

#             "reason":
#                 "High cloud cover may block the target."

#         }


#     return {

#         "level":
#             "very_poor",

#         "label":
#             "Very Poor",

#         "score":
#             0,

#         "reason":
#             "Heavy cloud cover is likely to block the sky."

#     }


# # =========================================================
# # MOON QUALITY
# # =========================================================

# def get_moon_quality(
#     separation
# ):

#     if separation is None:

#         return {

#             "level":
#                 "unknown",

#             "score":
#                 0,

#             "reason":
#                 "Moon interference information unavailable."

#         }


#     try:

#         separation = float(
#             separation
#         )

#     except Exception:

#         return {

#             "level":
#                 "unknown",

#             "score":
#                 0,

#             "reason":
#                 "Moon separation unavailable."

#         }


#     if separation >= 90:

#         return {

#             "level":
#                 "excellent",

#             "score":
#                 2,

#             "reason":
#                 "Moon is far from the target."

#         }


#     if separation >= 60:

#         return {

#             "level":
#                 "good",

#             "score":
#                 1.5,

#             "reason":
#                 "Moon has limited interference."

#         }


#     if separation >= 30:

#         return {

#             "level":
#                 "fair",

#             "score":
#                 1,

#             "reason":
#                 "Moon may cause some interference."

#         }


#     return {

#         "level":
#             "poor",

#         "score":
#             0,

#         "reason":
#             "Moon is close to the target and may interfere."

#     }


# # =========================================================
# # WEATHER
# # =========================================================

# def get_cloud_cover(
#     latitude,
#     longitude,
#     start_local,
#     end_local
# ):

#     try:

#         response = requests.get(

#             WEATHER_URL,

#             params={

#                 "latitude":
#                     latitude,

#                 "longitude":
#                     longitude,

#                 "hourly": [

#                     "cloud_cover",

#                     "precipitation_probability",

#                     "visibility"

#                 ],

#                 "timezone":
#                     "auto",

#                 "forecast_days":
#                     7

#             },

#             timeout=20

#         )


#         response.raise_for_status()


#         data = response.json()


#         hourly = data.get(
#             "hourly",
#             {}
#         )


#         times = hourly.get(
#             "time",
#             []
#         )


#         clouds = hourly.get(
#             "cloud_cover",
#             []
#         )


#         precipitation = hourly.get(
#             "precipitation_probability",
#             []
#         )


#         visibility = hourly.get(
#             "visibility",
#             []
#         )


#         selected_clouds = []

#         selected_precipitation = []

#         selected_visibility = []


#         # =================================================
#         # SELECT WEATHER FOR OBSERVATION WINDOW
#         # =================================================

#         for index, time_string in enumerate(times):

#             try:

#                 weather_time = datetime.fromisoformat(
#                     time_string
#                 )

#                 if weather_time.tzinfo is None:

#                     weather_time = weather_time.replace(
#                         tzinfo=INDIA_TIMEZONE
#                     )

#             except Exception:

#                 continue


#             if (
#                 start_local
#                 <= weather_time
#                 <= end_local
#             ):

#                 if index < len(clouds):

#                     value = clouds[index]

#                     if value is not None:

#                         selected_clouds.append(
#                             float(value)
#                         )


#                 if index < len(precipitation):

#                     value = precipitation[index]

#                     if value is not None:

#                         selected_precipitation.append(
#                             float(value)
#                         )


#                 if index < len(visibility):

#                     value = visibility[index]

#                     if value is not None:

#                         selected_visibility.append(
#                             float(value)
#                         )


#         # =================================================
#         # NO DATA
#         # =================================================

#         if not selected_clouds:

#             return {

#                 "known":
#                     False,

#                 "cloud_cover_percent":
#                     None,

#                 "precipitation_probability_percent":
#                     None,

#                 "visibility_m":
#                     None

#             }


#         return {

#             "known":
#                 True,

#             "cloud_cover_percent":
#                 round(
#                     sum(selected_clouds)
#                     / len(selected_clouds),
#                     1
#                 ),

#             "precipitation_probability_percent":
#                 round(
#                     sum(selected_precipitation)
#                     / len(selected_precipitation),
#                     1
#                 )
#                 if selected_precipitation
#                 else None,

#             "visibility_m":
#                 round(
#                     sum(selected_visibility)
#                     / len(selected_visibility),
#                     0
#                 )
#                 if selected_visibility
#                 else None

#         }


#     except Exception:

#         return {

#             "known":
#                 False,

#             "cloud_cover_percent":
#                 None,

#             "precipitation_probability_percent":
#                 None,

#             "visibility_m":
#                 None

#         }


# # =========================================================
# # FINAL OBSERVABILITY
# # =========================================================

# def calculate_final_observability(

#     difficulty_level,

#     altitude,

#     cloud_cover,

#     moon_separation,

#     light_pollution="unknown"

# ):

#     score = 0


#     # =====================================================
#     # ALTITUDE
#     # =====================================================

#     try:

#         altitude = float(
#             altitude
#         )

#     except Exception:

#         altitude = None


#     if altitude is not None:

#         if altitude >= 60:

#             score += 3

#         elif altitude >= 40:

#             score += 2.5

#         elif altitude >= 30:

#             score += 2

#         elif altitude >= 20:

#             score += 1


#     # =====================================================
#     # CLOUD
#     # =====================================================

#     cloud_info = get_cloud_quality(
#         cloud_cover
#     )

#     score += cloud_info["score"]


#     # =====================================================
#     # MOON
#     # =====================================================

#     moon_info = get_moon_quality(
#         moon_separation
#     )

#     score += moon_info["score"]


#     # =====================================================
#     # LIGHT POLLUTION
#     # =====================================================

#     if light_pollution is None:

#         lp = "unknown"

#     else:

#         lp = str(
#             light_pollution
#         ).strip().lower()


#     if lp == "low":

#         score += 2

#     elif lp == "medium":

#         score += 1


#     # =====================================================
#     # CLOUD OVERRIDE
#     # =====================================================

#     if (
#         cloud_cover is not None
#         and cloud_cover >= 80
#     ):

#         return {

#             "visible":
#                 False,

#             "quality":
#                 "very_poor",

#             "label":
#                 "Very Poor",

#             "score":
#                 round(score, 1),

#             "reason":
#                 "Heavy cloud cover is likely to block the target."

#         }


#     # =====================================================
#     # DIFFICULTY PENALTY
#     # =====================================================

#     if difficulty_level == "very_hard":

#         score -= 2

#     elif difficulty_level == "hard":

#         score -= 1


#     # =====================================================
#     # FINAL QUALITY
#     # =====================================================

#     if score >= 8:

#         quality = "excellent"

#         label = "Excellent"


#     elif score >= 6:

#         quality = "good"

#         label = "Good"


#     elif score >= 4:

#         quality = "fair"

#         label = "Fair"


#     elif score >= 2:

#         quality = "poor"

#         label = "Poor"


#     else:

#         quality = "very_poor"

#         label = "Very Poor"


#     # =====================================================
#     # REASON
#     # =====================================================

#     if (
#         cloud_cover is not None
#         and cloud_cover > 60
#     ):

#         reason = (
#             "Object is astronomically observable, "
#             "but high cloud cover may interfere."
#         )

#     elif lp == "high":

#         reason = (
#             "Object is above the horizon, "
#             "but light pollution may reduce visibility."
#         )

#     elif difficulty_level in [
#         "hard",
#         "very_hard"
#     ]:

#         reason = (
#             "Object is observable but requires "
#             "better equipment and sky conditions."
#         )

#     else:

#         reason = (
#             "Object has suitable altitude and "
#             "favorable observing conditions."
#         )


#     return {

#         "visible":
#             True,

#         "quality":
#             quality,

#         "label":
#             label,

#         "score":
#             round(score, 1),

#         "reason":
#             reason

#     }


# # =========================================================
# # INTERNAL DEEP SKY DATA FUNCTION
# # =========================================================
# #
# # IMPORTANT:
# # NO FastAPI Query() HERE.
# #
# # Master observation.py must call this function.
# #
# # =========================================================

# def get_deep_sky_data(

#     latitude,

#     longitude,

#     from_date,

#     to_date,

#     from_time="20:00",

#     to_time="02:00",

#     max_magnitude=10.0,

#     min_altitude=20.0,

#     limit=20,

#     difficulty="all",

#     light_pollution="unknown"

# ):

#     # =====================================================
#     # CLEAN INPUTS
#     # =====================================================

#     from_date = str(
#         from_date
#     ).strip()

#     to_date = str(
#         to_date
#     ).strip()

#     from_time = str(
#         from_time
#     ).strip()

#     to_time = str(
#         to_time
#     ).strip()

#     difficulty = str(
#         difficulty
#     ).strip().lower()


#     if light_pollution is None:

#         light_pollution = "unknown"

#     else:

#         light_pollution = str(
#             light_pollution
#         ).strip().lower()


#     # =====================================================
#     # VALIDATE DIFFICULTY
#     # =====================================================

#     allowed_difficulties = [

#         "all",

#         "easy",

#         "moderate",

#         "hard",

#         "very_hard"

#     ]


#     if difficulty not in allowed_difficulties:

#         raise ValueError(
#             f"Invalid difficulty. Allowed values: {allowed_difficulties}"
#         )


#     # =====================================================
#     # INDIA TIMEZONE
#     # =====================================================

#     start_local = datetime.strptime(

#         f"{from_date} {from_time}",

#         "%Y-%m-%d %H:%M"

#     ).replace(

#         tzinfo=INDIA_TIMEZONE

#     )


#     end_local = datetime.strptime(

#         f"{to_date} {to_time}",

#         "%Y-%m-%d %H:%M"

#     ).replace(

#         tzinfo=INDIA_TIMEZONE

#     )


#     # =====================================================
#     # VALIDATE TIME
#     # =====================================================

#     if end_local <= start_local:

#         raise ValueError(
#             "To date/time must be after From date/time"
#         )


#     # =====================================================
#     # WEATHER
#     # =====================================================

#     weather = get_cloud_cover(

#         latitude=
#             latitude,

#         longitude=
#             longitude,

#         start_local=
#             start_local,

#         end_local=
#             end_local

#     )


#     cloud_cover = weather.get(
#         "cloud_cover_percent"
#     )


#     # =====================================================
#     # CATEGORIES
#     # =====================================================

#     categories = [

#         "galaxy",

#         "nebula",

#         "cluster"

#     ]


#     objects = []


#     # =====================================================
#     # GET OBJECTS FROM SPACE CATALOG
#     # =====================================================

#     for category in categories:

#         params = {

#             "category":
#                 category,

#             "mag_max":
#                 max_magnitude,

#             "limit":
#                 limit

#         }


#         response = requests.get(

#             f"{BASE_URL}/objects",

#             params=params,

#             timeout=20

#         )


#         response.raise_for_status()


#         data = response.json()


#         if not isinstance(
#             data,
#             dict
#         ):

#             continue


#         category_objects = data.get(
#             "objects"
#         )


#         if not isinstance(
#             category_objects,
#             list
#         ):

#             continue


#         objects.extend(
#             category_objects
#         )


#     # =====================================================
#     # REMOVE DUPLICATES
#     # =====================================================

#     unique_objects = {}


#     for obj in objects:

#         if not isinstance(
#             obj,
#             dict
#         ):

#             continue


#         slug = obj.get(
#             "slug"
#         )


#         if slug:

#             unique_objects[
#                 slug
#             ] = obj


#     objects = list(
#         unique_objects.values()
#     )


#     # =====================================================
#     # CALCULATE EPHEMERIS
#     # =====================================================

#     visible_objects = []


#     for obj in objects:

#         slug = obj.get(
#             "slug"
#         )


#         if not slug:

#             continue


#         ephemeris_params = {

#             "object":
#                 slug,

#             "lat":
#                 latitude,

#             "lon":
#                 longitude,

#             "date":
#                 from_date

#         }


#         # try:

#         #     eph_response = requests.get(

#         #         f"{BASE_URL}/ephemeris",

#         #         params=ephemeris_params,

#         #         timeout=20

#         #     )

#         # except requests.exceptions.RequestException:

#         #     continue

#         try:

#     eph_response = requests.get(
#         f"{BASE_URL}/ephemeris",
#         params=ephemeris_params,
#         timeout=20
#     )

# except requests.exceptions.RequestException as e:

#     print("DEEP SKY EPHEMERIS REQUEST ERROR:", e)
#     continue

# print("========================================")
# print("DEEP SKY OBJECT:", obj.get("name"))
# print("CATEGORY:", obj.get("category"))
# print("SLUG:", slug)
# print("EPHEMERIS STATUS:", eph_response.status_code)
# print("EPHEMERIS URL:", eph_response.url)


#         if eph_response.status_code != 200:

#             continue


#         # try:

#         #     eph = eph_response.json()

#         # except Exception:

#         #     continue

# try:

#     eph = eph_response.json()

# except Exception as e:

#     print("DEEP SKY JSON ERROR:", e)
#     print("RAW RESPONSE:", eph_response.text[:2000])
#     continue

# print("EPHEMERIS RESPONSE:", eph_response.text[:2000])
#         if not isinstance(
#             eph,
#             dict
#         ):

#             continue


#         # =================================================
#         # SAFE DATA
#         # =================================================

#         observability = eph.get(
#             "observability"
#         )


#         if not isinstance(
#             observability,
#             dict
#         ):

#             observability = {}


#         best = observability.get(
#             "best"
#         )


#         if not isinstance(
#             best,
#             dict
#         ):

#             best = {}


#         events = eph.get(
#             "events"
#         )


#         if not isinstance(
#             events,
#             dict
#         ):

#             events = {}


#         moon = eph.get(
#             "moon"
#         )


#         if not isinstance(
#             moon,
#             dict
#         ):

#             moon = {}


#         # =================================================
#         # BEST ALTITUDE
#         # =================================================

#         best_altitude = best.get(
#             "altitude_deg"
#         )


#         try:

#             best_altitude = float(
#                 best_altitude
#             )

#         except Exception:

#             best_altitude = None


#         # =================================================
#         # ALTITUDE FILTER
#         # =================================================

#         # if (

#         #     best_altitude is None

#         #     or

#         #     best_altitude < float(
#         #         min_altitude
#         #     )

#         # ):

#         #     continue

# print("BEST ALTITUDE:", best_altitude)
# print("MIN ALTITUDE:", min_altitude)

# if best_altitude is None:

#     print(
#         "FILTERED: No best altitude:",
#         slug
#     )

#     continue

# if best_altitude < float(min_altitude):

#     print(
#         "FILTERED: Altitude too low:",
#         slug,
#         best_altitude
#     )

#     continue

# print(
#     "PASSED ALTITUDE FILTER:",
#     slug,
#     best_altitude
# )


#         # =================================================
#         # MAGNITUDE
#         # =================================================

#         magnitude = obj.get(
#             "magnitude"
#         )


#         if magnitude is None:

#             magnitude = obj.get(
#                 "mag"
#             )


#         # =================================================
#         # DIFFICULTY
#         # =================================================

#         difficulty_info = calculate_difficulty(

#             magnitude=
#                 magnitude,

#             altitude=
#                 best_altitude,

#             category=
#                 obj.get(
#                     "category"
#                 )

#         )


#         # =================================================
#         # DIFFICULTY FILTER
#         # =================================================

#         if (

#             difficulty != "all"

#             and

#             difficulty_info["level"]
#             != difficulty

#         ):

#             continue


#         # =================================================
#         # MOON
#         # =================================================

#         moon_separation = moon.get(
#             "separation_deg"
#         )


#         # =================================================
#         # FINAL OBSERVABILITY
#         # =================================================

#         final_visibility = (
#             calculate_final_observability(

#                 difficulty_level=
#                     difficulty_info["level"],

#                 altitude=
#                     best_altitude,

#                 cloud_cover=
#                     cloud_cover,

#                 moon_separation=
#                     moon_separation,

#                 light_pollution=
#                     light_pollution

#             )
#         )


#         # =================================================
#         # NAKED EYE
#         # =================================================
#         #
#         # Deep sky objects should generally not be marked
#         # naked-eye merely because they are bright.
#         #
#         # We therefore keep this conservative.
#         #
#         # =================================================

#         naked_eye = False


#         if (
#             magnitude is not None
#             and best_altitude is not None
#         ):

#             try:

#                 magnitude_value = float(
#                     magnitude
#                 )

#                 if (
#                     magnitude_value <= 4
#                     and best_altitude >= 40
#                     and obj.get("category") == "cluster"
#                 ):

#                     naked_eye = True

#             except Exception:

#                 naked_eye = False


#         # =================================================
#         # RECOMMENDATION
#         # =================================================

#         recommendation = (
#             difficulty_info.get(
#                 "recommendation"
#             )
#         )


#         if not final_visibility["visible"]:

#             recommendation = (
#                 final_visibility.get(
#                     "reason"
#                 )
#             )


#         # =================================================
#         # OBJECT
#         # =================================================

#         visible_objects.append({

#             "name":
#                 obj.get(
#                     "name"
#                 ),

#             "slug":
#                 slug,

#             "category":
#                 obj.get(
#                     "category"
#                 ),

#             "class":
#                 obj.get(
#                     "class"
#                 ),

#             "constellation":
#                 obj.get(
#                     "constellation"
#                 ),

#             "magnitude":
#                 magnitude,

#             "designations":
#                 obj.get(
#                     "designations",
#                     []
#                 ),

#             "ra_deg":
#                 obj.get(
#                     "ra_deg"
#                 ),

#             "dec_deg":
#                 obj.get(
#                     "dec_deg"
#                 ),

#             # ---------------------------------------------
#             # EVENTS
#             # ---------------------------------------------

#             "rise":
#                 events.get(
#                     "rise"
#                 ),

#             "transit":
#                 events.get(
#                     "transit"
#                 ),

#             "set":
#                 events.get(
#                     "set"
#                 ),

#             "transit_altitude_deg":
#                 events.get(
#                     "transit_altitude_deg"
#                 ),

#             # ---------------------------------------------
#             # OBSERVABILITY
#             # ---------------------------------------------

#             "hours_observable":
#                 observability.get(
#                     "hours_observable"
#                 ),

#             "best":
#                 best,

#             # ---------------------------------------------
#             # MOON
#             # ---------------------------------------------

#             "moon": {

#                 "phase_name":
#                     moon.get(
#                         "phase_name"
#                     ),

#                 "separation_deg":
#                     moon_separation

#             },

#             # ---------------------------------------------
#             # COMMON FIELDS
#             # ---------------------------------------------

#             "visible":
#                 final_visibility["visible"],

#             "observability":
#                 final_visibility["quality"],

#             "naked_eye":
#                 naked_eye,

#             "difficulty":
#                 difficulty_info,

#             "recommendation":
#                 recommendation,

#             "final_observability":
#                 final_visibility

#         })


#     # =====================================================
#     # SORT
#     # =====================================================

#     visible_objects.sort(

#         key=lambda x: (

#             x.get(
#                 "final_observability",
#                 {}
#             ).get(
#                 "score",
#                 0
#             ),

#             x.get(
#                 "best",
#                 {}
#             ).get(
#                 "altitude_deg",
#                 0
#             )

#         ),

#         reverse=True

#     )


#     # =====================================================
#     # LIMIT RESULTS
#     # =====================================================

#     visible_objects = visible_objects[
#         :MAX_RESULTS
#     ]


#     # =====================================================
#     # RESPONSE
#     # =====================================================

#     return {

#         "success":
#             True,

#         "location": {

#             "latitude":
#                 latitude,

#             "longitude":
#                 longitude,

#             "timezone":
#                 "Asia/Kolkata"

#         },

#         "observation": {

#             "from_date":
#                 from_date,

#             "to_date":
#                 to_date,

#             "from_time":
#                 from_time,

#             "to_time":
#                 to_time,

#             "start_local":
#                 start_local.isoformat(),

#             "end_local":
#                 end_local.isoformat()

#         },

#         "conditions": {

#             "cloud_cover_percent":
#                 cloud_cover,

#             "precipitation_probability_percent":
#                 weather.get(
#                     "precipitation_probability_percent"
#                 ),

#             "visibility_m":
#                 weather.get(
#                     "visibility_m"
#                 ),

#             "light_pollution":
#                 light_pollution

#         },

#         "filters": {

#             "max_magnitude":
#                 max_magnitude,

#             "min_altitude":
#                 min_altitude,

#             "difficulty":
#                 difficulty,

#             "max_results":
#                 MAX_RESULTS

#         },

#         "count":
#             len(
#                 visible_objects
#             ),

#         "objects":
#             visible_objects,

#         "message": (

#             "No suitable deep sky targets "
#             "were found for the selected conditions."

#             if not visible_objects

#             else None

#         ),

#         "source": {

#             "name":
#                 "SpaceCatalog.org",

#             "url":
#                 "https://spacecatalog.org/api"

#         }

#     }


# # =========================================================
# # FASTAPI ROUTE
# # =========================================================
# #
# # Query() exists ONLY here.
# #
# # =========================================================

# @router.get("/deep-sky")
# def get_deep_sky(

#     latitude: float = Query(...),

#     longitude: float = Query(...),

#     from_date: str = Query(...),

#     to_date: str = Query(...),

#     from_time: str = Query("20:00"),

#     to_time: str = Query("02:00"),

#     max_magnitude: float = Query(10.0),

#     min_altitude: float = Query(20.0),

#     limit: int = Query(20),

#     difficulty: str = Query("all"),

#     light_pollution: str = Query("unknown")

# ):

#     try:

#         return get_deep_sky_data(

#             latitude=
#                 latitude,

#             longitude=
#                 longitude,

#             from_date=
#                 from_date,

#             to_date=
#                 to_date,

#             from_time=
#                 from_time,

#             to_time=
#                 to_time,

#             max_magnitude=
#                 max_magnitude,

#             min_altitude=
#                 min_altitude,

#             limit=
#                 limit,

#             difficulty=
#                 difficulty,

#             light_pollution=
#                 light_pollution

#         )


#     except requests.exceptions.RequestException as e:

#         return {

#             "success":
#                 False,

#             "error":
#                 "Unable to fetch SpaceCatalog data",

#             "details":
#                 str(e),

#             "type":
#                 type(e).__name__

#         }


#     except Exception as e:

#         return {

#             "success":
#                 False,

#             "error":
#                 str(e),

#             "type":
#                 type(e).__name__

#         }



import requests

from fastapi import APIRouter, Query

from datetime import datetime, timezone, timedelta


router = APIRouter()


# =========================================================
# API
# =========================================================

BASE_URL = "https://spacecatalog.org/api/v1"

WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


# =========================================================
# CONSTANTS
# =========================================================

INDIA_TIMEZONE = timezone(
    timedelta(hours=5, minutes=30)
)

MAX_RESULTS = 10


# =========================================================
# DIFFICULTY
# =========================================================

def calculate_difficulty(
    magnitude,
    altitude,
    category
):

    try:

        magnitude = float(
            magnitude
        )

    except Exception:

        magnitude = None


    try:

        altitude = float(
            altitude
        )

    except Exception:

        altitude = None


    category = (
        str(category).lower()
        if category
        else ""
    )


    # =====================================================
    # VERY LOW ALTITUDE
    # =====================================================

    if altitude is not None and altitude < 20:

        return {

            "level":
                "very_hard",

            "label":
                "Very Hard",

            "recommendation":
                "Low altitude makes this target difficult to observe."

        }


    # =====================================================
    # MAGNITUDE
    # =====================================================

    if magnitude is not None:

        # -----------------------------------------------
        # Bright
        # -----------------------------------------------

        if magnitude <= 6:

            if (
                altitude is not None
                and altitude >= 40
            ):

                return {

                    "level":
                        "easy",

                    "label":
                        "Easy",

                    "recommendation":
                        "Good target for beginner observers and small telescopes."

                }


            return {

                "level":
                    "moderate",

                "label":
                    "Moderate",

                "recommendation":
                    "Bright target, but higher altitude would improve observation."

            }


        # -----------------------------------------------
        # Medium
        # -----------------------------------------------

        if magnitude <= 8:

            if (
                altitude is not None
                and altitude >= 40
            ):

                return {

                    "level":
                        "moderate",

                    "label":
                        "Moderate",

                    "recommendation":
                        "Good telescope target under reasonably dark skies."

                }


            return {

                "level":
                    "hard",

                "label":
                    "Hard",

                "recommendation":
                    "Requires a telescope and reasonably dark skies."

            }


        # -----------------------------------------------
        # Faint
        # -----------------------------------------------

        if magnitude <= 10:

            return {

                "level":
                    "hard",

                "label":
                    "Hard",

                "recommendation":
                    "Faint target. Telescope and dark skies are recommended."

            }


        # -----------------------------------------------
        # Very faint
        # -----------------------------------------------

        return {

            "level":
                "very_hard",

            "label":
                "Very Hard",

            "recommendation":
                "Very faint target. Requires a good telescope and dark skies."

        }


    # =====================================================
    # CATEGORY FALLBACK
    # =====================================================

    if category == "galaxy":

        return {

            "level":
                "hard",

            "label":
                "Hard",

            "recommendation":
                "Galaxies benefit strongly from dark skies and telescope observation."

        }


    if category == "nebula":

        return {

            "level":
                "moderate",

            "label":
                "Moderate",

            "recommendation":
                "Best observed with a telescope under dark skies."

        }


    if category == "cluster":

        return {

            "level":
                "easy",

            "label":
                "Easy",

            "recommendation":
                "Generally a good target for beginner observers."

        }


    return {

        "level":
            "moderate",

        "label":
            "Moderate",

        "recommendation":
            "Suitable for telescope observation under good sky conditions."

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
                "Some cloud cover may interfere with observation."

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
                "High cloud cover may block the target."

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
# MOON QUALITY
# =========================================================

def get_moon_quality(
    separation
):

    if separation is None:

        return {

            "level":
                "unknown",

            "score":
                0,

            "reason":
                "Moon interference information unavailable."

        }


    try:

        separation = float(
            separation
        )

    except Exception:

        return {

            "level":
                "unknown",

            "score":
                0,

            "reason":
                "Moon separation unavailable."

        }


    if separation >= 90:

        return {

            "level":
                "excellent",

            "score":
                2,

            "reason":
                "Moon is far from the target."

        }


    if separation >= 60:

        return {

            "level":
                "good",

            "score":
                1.5,

            "reason":
                "Moon has limited interference."

        }


    if separation >= 30:

        return {

            "level":
                "fair",

            "score":
                1,

            "reason":
                "Moon may cause some interference."

        }


    return {

        "level":
            "poor",

        "score":
            0,

        "reason":
            "Moon is close to the target and may interfere."

    }


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
        # SELECT WEATHER FOR OBSERVATION WINDOW
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
        # NO DATA
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
# FINAL OBSERVABILITY
# =========================================================

def calculate_final_observability(

    difficulty_level,

    altitude,

    cloud_cover,

    moon_separation,

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
    # MOON
    # =====================================================

    moon_info = get_moon_quality(
        moon_separation
    )

    score += moon_info["score"]


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


    # =====================================================
    # CLOUD OVERRIDE
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
                "Heavy cloud cover is likely to block the target."

        }


    # =====================================================
    # DIFFICULTY PENALTY
    # =====================================================

    if difficulty_level == "very_hard":

        score -= 2

    elif difficulty_level == "hard":

        score -= 1


    # =====================================================
    # FINAL QUALITY
    # =====================================================

    if score >= 8:

        quality = "excellent"

        label = "Excellent"


    elif score >= 6:

        quality = "good"

        label = "Good"


    elif score >= 4:

        quality = "fair"

        label = "Fair"


    elif score >= 2:

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
            "Object is astronomically observable, "
            "but high cloud cover may interfere."
        )

    elif lp == "high":

        reason = (
            "Object is above the horizon, "
            "but light pollution may reduce visibility."
        )

    elif difficulty_level in [
        "hard",
        "very_hard"
    ]:

        reason = (
            "Object is observable but requires "
            "better equipment and sky conditions."
        )

    else:

        reason = (
            "Object has suitable altitude and "
            "favorable observing conditions."
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
# INTERNAL DEEP SKY DATA FUNCTION
# =========================================================
#
# IMPORTANT:
# NO FastAPI Query() HERE.
#
# Master observation.py must call this function.
#
# =========================================================

def get_deep_sky_data(

    latitude,

    longitude,

    from_date,

    to_date,

    from_time="20:00",

    to_time="02:00",

    max_magnitude=10.0,

    min_altitude=20.0,

    limit=20,

    difficulty="all",

    light_pollution="unknown"

):

    # =====================================================
    # CLEAN INPUTS
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

    difficulty = str(
        difficulty
    ).strip().lower()


    if light_pollution is None:

        light_pollution = "unknown"

    else:

        light_pollution = str(
            light_pollution
        ).strip().lower()


    # =====================================================
    # VALIDATE DIFFICULTY
    # =====================================================

    allowed_difficulties = [

        "all",

        "easy",

        "moderate",

        "hard",

        "very_hard"

    ]


    if difficulty not in allowed_difficulties:

        raise ValueError(
            f"Invalid difficulty. Allowed values: {allowed_difficulties}"
        )


    # =====================================================
    # INDIA TIMEZONE
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
    # VALIDATE TIME
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
    # CATEGORIES
    # =====================================================

    categories = [

        "galaxy",

        "nebula",

        "cluster"

    ]


    objects = []


    # =====================================================
    # GET OBJECTS FROM SPACE CATALOG
    # =====================================================

    for category in categories:

        params = {

            "category":
                category,

            "mag_max":
                max_magnitude,

            "limit":
                limit

        }


        response = requests.get(

            f"{BASE_URL}/objects",

            params=params,

            timeout=20

        )


        response.raise_for_status()


        data = response.json()


        if not isinstance(
            data,
            dict
        ):

            continue


        category_objects = data.get(
            "objects"
        )


        if not isinstance(
            category_objects,
            list
        ):

            continue


        objects.extend(
            category_objects
        )


    # =====================================================
    # REMOVE DUPLICATES
    # =====================================================

    unique_objects = {}


    for obj in objects:

        if not isinstance(
            obj,
            dict
        ):

            continue


        slug = obj.get(
            "slug"
        )


        if slug:

            unique_objects[
                slug
            ] = obj


    objects = list(
        unique_objects.values()
    )


    # =====================================================
    # CALCULATE EPHEMERIS
    # =====================================================

    visible_objects = []


    for obj in objects:

        slug = obj.get(
            "slug"
        )


        if not slug:

            continue


        ephemeris_params = {

            "object":
                slug,

            "lat":
                latitude,

            "lon":
                longitude,

            "date":
                from_date

        }


        try:

            eph_response = requests.get(

                f"{BASE_URL}/ephemeris",

                params=ephemeris_params,

                timeout=20

            )

            print("========================================")
            print("DEEP SKY OBJECT:", obj.get("name"))
            print("CATEGORY:", obj.get("category"))
            print("SLUG:", slug)
            print("EPHEMERIS PARAMS:", ephemeris_params)
            print("EPHEMERIS STATUS:", eph_response.status_code)
            print("EPHEMERIS URL:", eph_response.url)
            print("EPHEMERIS RESPONSE:", eph_response.text[:2000])
            print("========================================")

        except requests.exceptions.RequestException as e:

            print("EPHEMERIS REQUEST ERROR:", e)
            continue


        if eph_response.status_code != 200:

            print("FILTERED: Ephemeris HTTP status:", eph_response.status_code, slug)
            continue


        try:

            eph = eph_response.json()

        except Exception as e:

            print("DEEP SKY JSON ERROR:", e)
            print("RAW RESPONSE:", eph_response.text[:2000])
            continue


        if not isinstance(
            eph,
            dict
        ):

            continue


        # =================================================
        # SAFE DATA
        # =================================================

        observability = eph.get(
            "observability"
        )


        if not isinstance(
            observability,
            dict
        ):

            observability = {}


        best = observability.get(
            "best"
        )


        if not isinstance(
            best,
            dict
        ):

            best = {}


        events = eph.get(
            "events"
        )


        if not isinstance(
            events,
            dict
        ):

            events = {}


        moon = eph.get(
            "moon"
        )


        if not isinstance(
            moon,
            dict
        ):

            moon = {}


        # =================================================
        # BEST ALTITUDE
        # =================================================

        best_altitude = best.get(
            "altitude_deg"
        )


        try:

            best_altitude = float(

                best_altitude

            )

        except Exception:

            best_altitude = None


        print("BEST ALTITUDE:", best_altitude)
        print("MIN ALTITUDE:", min_altitude)


        # =================================================
        # ALTITUDE FILTER
        # =================================================

        if best_altitude is None:

            print("FILTERED: No best altitude:", slug)
            continue

        if best_altitude < float(min_altitude):

            print("FILTERED: Altitude too low:", slug, best_altitude)
            continue

        print("PASSED ALTITUDE FILTER:", slug, best_altitude)


        # =================================================
        # MAGNITUDE
        # =================================================

        magnitude = obj.get(
            "magnitude"
        )


        if magnitude is None:

            magnitude = obj.get(
                "mag"
            )


        # =================================================
        # DIFFICULTY
        # =================================================

        difficulty_info = calculate_difficulty(

            magnitude=
                magnitude,

            altitude=
                best_altitude,

            category=
                obj.get(
                    "category"
                )

        )


        # =================================================
        # DIFFICULTY FILTER
        # =================================================

        if (

            difficulty != "all"

            and

            difficulty_info["level"]
            != difficulty

        ):

            continue


        # =================================================
        # MOON
        # =================================================

        moon_separation = moon.get(
            "separation_deg"
        )


        # =================================================
        # FINAL OBSERVABILITY
        # =================================================

        final_visibility = (
            calculate_final_observability(

                difficulty_level=
                    difficulty_info["level"],

                altitude=
                    best_altitude,

                cloud_cover=
                    cloud_cover,

                moon_separation=
                    moon_separation,

                light_pollution=
                    light_pollution

            )
        )


        # =================================================
        # NAKED EYE
        # =================================================
        #
        # Deep sky objects should generally not be marked
        # naked-eye merely because they are bright.
        #
        # We therefore keep this conservative.
        #
        # =================================================

        naked_eye = False


        if (
            magnitude is not None
            and best_altitude is not None
        ):

            try:

                magnitude_value = float(
                    magnitude
                )

                if (
                    magnitude_value <= 4
                    and best_altitude >= 40
                    and obj.get("category") == "cluster"
                ):

                    naked_eye = True

            except Exception:

                naked_eye = False


        # =================================================
        # RECOMMENDATION
        # =================================================

        recommendation = (
            difficulty_info.get(
                "recommendation"
            )
        )


        if not final_visibility["visible"]:

            recommendation = (
                final_visibility.get(
                    "reason"
                )
            )


        # =================================================
        # OBJECT
        # =================================================

        visible_objects.append({

            "name":
                obj.get(
                    "name"
                ),

            "slug":
                slug,

            "category":
                obj.get(
                    "category"
                ),

            "class":
                obj.get(
                    "class"
                ),

            "constellation":
                obj.get(
                    "constellation"
                ),

            "magnitude":
                magnitude,

            "designations":
                obj.get(
                    "designations",
                    []
                ),

            "ra_deg":
                obj.get(
                    "ra_deg"
                ),

            "dec_deg":
                obj.get(
                    "dec_deg"
                ),

            # ---------------------------------------------
            # EVENTS
            # ---------------------------------------------

            "rise":
                events.get(
                    "rise"
                ),

            "transit":
                events.get(
                    "transit"
                ),

            "set":
                events.get(
                    "set"
                ),

            "transit_altitude_deg":
                events.get(
                    "transit_altitude_deg"
                ),

            # ---------------------------------------------
            # OBSERVABILITY
            # ---------------------------------------------

            "hours_observable":
                observability.get(
                    "hours_observable"
                ),

            "best":
                best,

            # ---------------------------------------------
            # MOON
            # ---------------------------------------------

            "moon": {

                "phase_name":
                    moon.get(
                        "phase_name"
                    ),

                "separation_deg":
                    moon_separation

            },

            # ---------------------------------------------
            # COMMON FIELDS
            # ---------------------------------------------

            "visible":
                final_visibility["visible"],

            "observability":
                final_visibility["quality"],

            "naked_eye":
                naked_eye,

            "difficulty":
                difficulty_info,

            "recommendation":
                recommendation,

            "final_observability":
                final_visibility

        })


    # =====================================================
    # SORT
    # =====================================================

    visible_objects.sort(

        key=lambda x: (

            x.get(
                "final_observability",
                {}
            ).get(
                "score",
                0
            ),

            x.get(
                "best",
                {}
            ).get(
                "altitude_deg",
                0
            )

        ),

        reverse=True

    )


    # =====================================================
    # LIMIT RESULTS
    # =====================================================

    visible_objects = visible_objects[
        :MAX_RESULTS
    ]


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

            "max_magnitude":
                max_magnitude,

            "min_altitude":
                min_altitude,

            "difficulty":
                difficulty,

            "max_results":
                MAX_RESULTS

        },

        "count":
            len(
                visible_objects
            ),

        "objects":
            visible_objects,

        "message": (

            "No suitable deep sky targets "
            "were found for the selected conditions."

            if not visible_objects

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
# Query() exists ONLY here.
#
# =========================================================

@router.get("/deep-sky")
def get_deep_sky(

    latitude: float = Query(...),

    longitude: float = Query(...),

    from_date: str = Query(...),

    to_date: str = Query(...),

    from_time: str = Query("20:00"),

    to_time: str = Query("02:00"),

    max_magnitude: float = Query(10.0),

    min_altitude: float = Query(20.0),

    limit: int = Query(20),

    difficulty: str = Query("all"),

    light_pollution: str = Query("unknown")

):

    try:

        return get_deep_sky_data(

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

            max_magnitude=
                max_magnitude,

            min_altitude=
                min_altitude,

            limit=
                limit,

            difficulty=
                difficulty,

            light_pollution=
                light_pollution

        )


    except requests.exceptions.RequestException as e:

        return {

            "success":
                False,

            "error":
                "Unable to fetch SpaceCatalog data",

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
