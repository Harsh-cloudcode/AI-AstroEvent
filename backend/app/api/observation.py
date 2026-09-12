# import requests
# from fastapi import APIRouter, Query

# from app.api.weather import get_weather
# from app.api.sun import get_sun

# from app.api.planets import get_planets
# from app.api.deep_objects import get_deep_sky
# from app.api.meteor_showers import get_meteor_showers
# from app.api.weather import get_weather
# from app.api.atronomical_events import get_astronomical_events
# from app.services.ai_recommendation import generate_recommendation


# router = APIRouter()


# @router.post("/observation/analyze")
# def analyze_observation(
#     latitude: float = Query(...),
#     longitude: float = Query(...),
#     date: str = Query(...),
#     start_time: str = Query("20:00"),
#     end_time: str = Query("02:00")
# ):

#     try:

#         # --------------------------------------------------
#         # 1. WEATHER
#         # --------------------------------------------------

#         weather = get_weather(
#             latitude=latitude,
#             longitude=longitude
#         )


#         # --------------------------------------------------
#         # 2. SUN
#         # --------------------------------------------------

#         sun = get_sun(
#             latitude=latitude,
#             longitude=longitude,
#             date=date
#         )


#         # --------------------------------------------------
#         # 3. PLANETS
#         # --------------------------------------------------

#         planets = get_planets(
#             latitude=latitude,
#             longitude=longitude,
#             from_date=date,
#             to_date=date,
#             from_time=start_time,
#             to_time=end_time
#         )


#         # --------------------------------------------------
#         # 4. DEEP SKY
#         # --------------------------------------------------

#         deep_sky = get_deep_sky(
#             latitude=latitude,
#             longitude=longitude,
#             from_date=date,
#             to_date=date,
#             from_time=start_time,
#             to_time=end_time
#         )


#         # --------------------------------------------------
#         # 5. METEOR SHOWERS
#         # --------------------------------------------------

#         meteor_showers = get_meteor_showers(
#             latitude=latitude,
#             longitude=longitude,
#             from_date=date,
#             to_date=date,
#             from_time=start_time,
#             to_time=end_time
#         )


#         # --------------------------------------------------
#         # 6. ASTRONOMICAL WEATHER
#         # --------------------------------------------------

#         astro_weather = get_astro_weather(
#             latitude=latitude,
#             longitude=longitude,
#             from_date=date,
#             to_date=date,
#             from_time=start_time,
#             to_time=end_time
#         )


#         # --------------------------------------------------
#         # 7. ASTRONOMICAL EVENTS
#         # --------------------------------------------------

#         events = get_astronomical_events(
#             latitude=latitude,
#             longitude=longitude,
#             from_date=date,
#             to_date=date,
#             from_time=start_time,
#             to_time=end_time
#         )


#         # --------------------------------------------------
#         # COMBINED ASTRONOMY DATA
#         # --------------------------------------------------

#         astronomy_data = {

#             "location": {
#                 "latitude": latitude,
#                 "longitude": longitude
#             },

#             "observation": {
#                 "date": date,
#                 "start_time": start_time,
#                 "end_time": end_time
#             },

#             "weather": weather,

#             "sun": sun,

#             "planets": planets,

#             "deep_sky": deep_sky,

#             "meteor_showers": meteor_showers,

#             "astro_weather": astro_weather,

#             "events": events
#         }


#         # --------------------------------------------------
#         # GEMINI AI RECOMMENDATION
#         # --------------------------------------------------

#         ai_recommendation = generate_recommendation(
#             astronomy_data
#         )


#         # --------------------------------------------------
#         # FINAL RESPONSE
#         # --------------------------------------------------

#         return {

#             "success": True,

#             "observation": {
#                 "latitude": latitude,
#                 "longitude": longitude,
#                 "date": date,
#                 "start_time": start_time,
#                 "end_time": end_time
#             },

#             "weather": weather,

#             "sun": sun,

#             "planets": planets,

#             "deep_sky": deep_sky,

#             "meteor_showers": meteor_showers,

#             "astro_weather": astro_weather,

#             "events": events,

#             "ai_recommendation": ai_recommendation
#         }


#     except requests.exceptions.RequestException as e:

#         return {
#             "success": False,
#             "error": "External astronomy API request failed",
#             "details": str(e),
#             "type": type(e).__name__
#         }


#     except Exception as e:

#         return {
#             "success": False,
#             "error": str(e),
#             "type": type(e).__name__
#         }




# import requests
# from fastapi import APIRouter, Query

# from app.api.weather import get_weather
# from app.api.sun import get_sun

# from app.api.planets import get_planets
# from app.api.deep_objects import get_deep_sky
# from app.api.meteor_showers import get_meteor_showers
# from app.api.weather import get_weather
# from app.api.atronomical_events import get_astronomical_events
# from app.services.ai_recommendation import generate_recommendation
# from app.api.constellations import get_constellations


# router = APIRouter()


# @router.post("/observation/analyze")
# def analyze_observation(
#     latitude: float = Query(...),
#     longitude: float = Query(...),

#     from_date: str = Query(...),
#     to_date: str = Query(...),

#     from_time: str = Query("20:00"),
#     to_time: str = Query("02:00")
# ):

#     try:

#         # --------------------------------------------------
#         # 1. WEATHER
#         # --------------------------------------------------

#         weather = get_weather(
#             latitude=latitude,
#             longitude=longitude
#         )


#         # --------------------------------------------------
#         # 2. SUN
#         # --------------------------------------------------

#         sun = get_sun(
#             latitude=latitude,
#             longitude=longitude,
#             date=from_date
#         )


#         # --------------------------------------------------
#         # 3. PLANETS
#         # --------------------------------------------------

#         planets = get_planets(
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )


#         # --------------------------------------------------
#         # 4. DEEP SKY
#         # --------------------------------------------------

#         deep_sky = get_deep_sky(
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )


#         # --------------------------------------------------
#         # 5. METEOR SHOWERS
#         # --------------------------------------------------

#         meteor_showers = get_meteor_showers(
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )


#         # --------------------------------------------------
#         # 6. ASTRONOMICAL WEATHER
#         # --------------------------------------------------

#         astro_weather = get_weather(
#             latitude=latitude,
#             longitude=longitude,
#             # from_date=from_date,
#             # to_date=to_date,
#             # from_time=from_time,
#             # to_time=to_time
#         )


#         # --------------------------------------------------
#         # 7. ASTRONOMICAL EVENTS
#         # --------------------------------------------------

#         events = get_astronomical_events(
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )


#         # --------------------------------------------------
#         # COMBINED ASTRONOMY DATA
#         # --------------------------------------------------

#         astronomy_data = {

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

#             "weather": weather,

#             "sun": sun,

#             "planets": planets,

#             "deep_sky": deep_sky,

#             "meteor_showers": meteor_showers,

#             "astro_weather": astro_weather,

#             "events": events
#         }


#         # --------------------------------------------------
#         # GEMINI AI RECOMMENDATION
#         # --------------------------------------------------

#         ai_recommendation = generate_recommendation(
#             astronomy_data
#         )

    
#         # --------------------------------------------------
#         # Constallations
#         # --------------------------------------------------
              
#         constellations = get_constellations(
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )

#         # --------------------------------------------------
#         # FINAL RESPONSE
#         # --------------------------------------------------

#         return {

#             "success": True,

#             "observation": {
#                 "latitude": latitude,
#                 "longitude": longitude,
#                 "from_date": from_date,
#                 "to_date": to_date,
#                 "from_time": from_time,
#                 "to_time": to_time
#             },

#             "weather": weather,

#             "sun": sun,

#             "planets": planets,

#             "deep_sky": deep_sky,
            
#             "constellations": constellations,

#             "meteor_showers": meteor_showers,

#             "astro_weather": astro_weather,

#             "events": events,

#             "ai_recommendation": ai_recommendation
#         }


#     except requests.exceptions.RequestException as e:

#         return {
#             "success": False,
#             "error": "External astronomy API request failed",
#             "details": str(e),
#             "type": type(e).__name__
#         }


#     except Exception as e:

#         return {
#             "success": False,
#             "error": str(e),
#             "type": type(e).__name__
#         }

# import requests

# from fastapi import APIRouter, Query

# from app.api.weather import get_weather
# from app.api.sun import get_sun
# from app.api.planets import get_planets
# from app.api.deep_objects import get_deep_sky
# from app.api.constellations import get_constellations
# from app.api.meteor_showers import get_meteor_showers
# from app.api.weather import get_weather
# from app.api.atronomical_events import get_astronomical_events

# from app.services.ai_recommendation import generate_recommendation


# router = APIRouter()


# # ============================================================
# # HELPER: SAFE MODULE CALL
# # ============================================================

# def safe_call(function, **kwargs):

#     try:

#         result = function(**kwargs)

#         return {
#             "success": True,
#             "data": result
#         }

#     except Exception as e:

#         return {
#             "success": False,
#             "data": None,
#             "error": str(e),
#             "type": type(e).__name__
#         }


# # ============================================================
# # VISIBILITY SUMMARY
# # ============================================================

# def build_visibility_summary(
#     planets,
#     deep_sky,
#     constellations,
#     meteor_showers,
#     events
# ):

#     summary = {

#         "planets": {
#             "visible": 0,
#             "not_visible": 0
#         },

#         "deep_sky": {
#             "visible": 0,
#             "not_visible": 0
#         },

#         "constellations": {
#             "visible": 0,
#             "not_visible": 0
#         },

#         "meteor_showers": {
#             "visible": 0,
#             "not_visible": 0
#         },

#         "astronomical_events": {
#             "visible": 0,
#             "not_visible": 0
#         }
#     }


#     # --------------------------------------------------------
#     # PLANETS
#     # --------------------------------------------------------

#     if isinstance(planets, dict):

#         planet_items = planets.get(
#             "planets",
#             []
#         )

#     elif isinstance(planets, list):

#         planet_items = planets

#     else:

#         planet_items = []


#     for planet in planet_items:

#         if not isinstance(planet, dict):
#             continue

#         if planet.get("visible") is True:

#             summary["planets"]["visible"] += 1

#         elif planet.get("visible") is False:

#             summary["planets"]["not_visible"] += 1


#     # --------------------------------------------------------
#     # DEEP SKY
#     # --------------------------------------------------------

#     if isinstance(deep_sky, dict):

#         deep_items = deep_sky.get(
#             "objects",
#             deep_sky.get(
#                 "deep_sky",
#                 []
#             )
#         )

#     elif isinstance(deep_sky, list):

#         deep_items = deep_sky

#     else:

#         deep_items = []


#     for obj in deep_items:

#         if not isinstance(obj, dict):
#             continue

#         final_obs = obj.get(
#             "final_observability",
#             {}
#         )

#         if final_obs.get("visible") is True:

#             summary["deep_sky"]["visible"] += 1

#         elif final_obs.get("visible") is False:

#             summary["deep_sky"]["not_visible"] += 1


#     # --------------------------------------------------------
#     # CONSTELLATIONS
#     # --------------------------------------------------------

#     if isinstance(constellations, dict):

#         constellation_items = constellations.get(
#             "constellations",
#             []
#         )

#     elif isinstance(constellations, list):

#         constellation_items = constellations

#     else:

#         constellation_items = []


#     for constellation in constellation_items:

#         if not isinstance(constellation, dict):
#             continue

#         final_obs = constellation.get(
#             "final_observability",
#             {}
#         )

#         if final_obs.get("visible") is True:

#             summary["constellations"]["visible"] += 1

#         elif final_obs.get("visible") is False:

#             summary["constellations"]["not_visible"] += 1


#     # --------------------------------------------------------
#     # METEOR SHOWERS
#     # --------------------------------------------------------

#     if isinstance(meteor_showers, dict):

#         meteor_items = meteor_showers.get(
#             "showers",
#             []
#         )

#     elif isinstance(meteor_showers, list):

#         meteor_items = meteor_showers

#     else:

#         meteor_items = []


#     for shower in meteor_items:

#         if not isinstance(shower, dict):
#             continue

#         if shower.get("visible") is True:

#             summary["meteor_showers"]["visible"] += 1

#         elif shower.get("visible") is False:

#             summary["meteor_showers"]["not_visible"] += 1


#     # --------------------------------------------------------
#     # ASTRONOMICAL EVENTS
#     # --------------------------------------------------------

#     if isinstance(events, dict):

#         event_data = events.get(
#             "events",
#             {}
#         )

#         event_items = []

#         if isinstance(event_data, dict):

#             for key in [
#                 "eclipses",
#                 "conjunctions",
#                 "oppositions",
#                 "occultations"
#             ]:

#                 items = event_data.get(
#                     key,
#                     []
#                 )

#                 if isinstance(items, list):

#                     event_items.extend(items)

#     elif isinstance(events, list):

#         event_items = events

#     else:

#         event_items = []


#     for event in event_items:

#         if not isinstance(event, dict):
#             continue

#         visibility = event.get(
#             "visibility",
#             {}
#         )

#         if visibility.get("visible") is True:

#             summary["astronomical_events"]["visible"] += 1

#         elif visibility.get("visible") is False:

#             summary["astronomical_events"]["not_visible"] += 1


#     return summary


# # ============================================================
# # DIFFICULTY SUMMARY
# # ============================================================

# def build_difficulty_summary(
#     planets,
#     deep_sky,
#     constellations,
#     meteor_showers,
#     events
# ):

#     summary = {

#         "easy": 0,
#         "moderate": 0,
#         "hard": 0,
#         "very_hard": 0,
#         "unknown": 0
#     }


#     def add_difficulty(item):

#         if not isinstance(item, dict):
#             return

#         difficulty = item.get(
#             "difficulty"
#         )

#         if isinstance(difficulty, dict):

#             level = difficulty.get(
#                 "level",
#                 "unknown"
#             )

#             if level in summary:

#                 summary[level] += 1

#             else:

#                 summary["unknown"] += 1

#             return

#         # Some modules may use a simple difficulty value
#         level = item.get(
#             "difficulty_level"
#         )

#         if level in summary:

#             summary[level] += 1

#         else:

#             summary["unknown"] += 1


#     # --------------------------------------------------------
#     # PLANETS
#     # --------------------------------------------------------

#     if isinstance(planets, dict):

#         items = planets.get(
#             "planets",
#             []
#         )

#     elif isinstance(planets, list):

#         items = planets

#     else:

#         items = []


#     for item in items:
#         add_difficulty(item)


#     # --------------------------------------------------------
#     # DEEP SKY
#     # --------------------------------------------------------

#     if isinstance(deep_sky, dict):

#         items = deep_sky.get(
#             "objects",
#             deep_sky.get(
#                 "deep_sky",
#                 []
#             )
#         )

#     elif isinstance(deep_sky, list):

#         items = deep_sky

#     else:

#         items = []


#     for item in items:
#         add_difficulty(item)


#     # --------------------------------------------------------
#     # CONSTELLATIONS
#     # --------------------------------------------------------

#     if isinstance(constellations, dict):

#         items = constellations.get(
#             "constellations",
#             []
#         )

#     elif isinstance(constellations, list):

#         items = constellations

#     else:

#         items = []


#     for item in items:
#         add_difficulty(item)


#     # --------------------------------------------------------
#     # METEOR SHOWERS
#     # --------------------------------------------------------

#     if isinstance(meteor_showers, dict):

#         items = meteor_showers.get(
#             "showers",
#             []
#         )

#     elif isinstance(meteor_showers, list):

#         items = meteor_showers

#     else:

#         items = []


#     for item in items:
#         add_difficulty(item)


#     # --------------------------------------------------------
#     # EVENTS
#     # --------------------------------------------------------

#     if isinstance(events, dict):

#         event_data = events.get(
#             "events",
#             {}
#         )

#         items = []

#         if isinstance(event_data, dict):

#             for key in [
#                 "eclipses",
#                 "conjunctions",
#                 "oppositions",
#                 "occultations"
#             ]:

#                 event_items = event_data.get(
#                     key,
#                     []
#                 )

#                 if isinstance(event_items, list):

#                     items.extend(
#                         event_items
#                     )

#     elif isinstance(events, list):

#         items = events

#     else:

#         items = []


#     for item in items:
#         add_difficulty(item)


#     return summary


# # ============================================================
# # OBSERVATION QUALITY
# # ============================================================

# def calculate_observation_quality(
#     weather,
#     astro_weather,
#     visibility_summary
# ):

#     score = 5.0

#     reasons = []


#     # --------------------------------------------------------
#     # WEATHER
#     # --------------------------------------------------------

#     cloud_cover = None

#     try:

#         if isinstance(weather, dict):

#             hourly = weather.get(
#                 "hourly",
#                 {}
#             )

#             clouds = hourly.get(
#                 "cloud_cover",
#                 []
#             )

#             if clouds:

#                 valid_clouds = [
#                     float(c)
#                     for c in clouds
#                     if c is not None
#                 ]

#                 if valid_clouds:

#                     cloud_cover = (
#                         sum(valid_clouds)
#                         / len(valid_clouds)
#                     )

#     except Exception:
#         cloud_cover = None


#     if cloud_cover is not None:

#         if cloud_cover <= 10:

#             score += 4

#             reasons.append(
#                 "Very low cloud cover."
#             )

#         elif cloud_cover <= 30:

#             score += 3

#             reasons.append(
#                 "Low cloud cover."
#             )

#         elif cloud_cover <= 60:

#             score += 1

#             reasons.append(
#                 "Some cloud cover may interfere."
#             )

#         elif cloud_cover <= 80:

#             score -= 2

#             reasons.append(
#                 "High cloud cover may interfere."
#             )

#         else:

#             score -= 4

#             reasons.append(
#                 "Heavy cloud cover is likely."
#             )


#     # --------------------------------------------------------
#     # VISIBLE TARGETS
#     # --------------------------------------------------------

#     visible_count = 0

#     for category in visibility_summary.values():

#         if isinstance(category, dict):

#             visible_count += category.get(
#                 "visible",
#                 0
#             )


#     if visible_count >= 8:

#         score += 1

#         reasons.append(
#             "Many astronomical targets are available."
#         )

#     elif visible_count >= 4:

#         score += 0.5

#         reasons.append(
#             "Several astronomical targets are available."
#         )

#     elif visible_count == 0:

#         score -= 2

#         reasons.append(
#             "No clearly visible targets were returned."
#         )


#     # --------------------------------------------------------
#     # LIMIT SCORE
#     # --------------------------------------------------------

#     score = max(
#         0,
#         min(
#             10,
#             score
#         )
#     )


#     # --------------------------------------------------------
#     # LABEL
#     # --------------------------------------------------------

#     if score >= 8.5:

#         quality = "excellent"

#         label = "Excellent"

#     elif score >= 7:

#         quality = "very_good"

#         label = "Very Good"

#     elif score >= 5:

#         quality = "good"

#         label = "Good"

#     elif score >= 3:

#         quality = "fair"

#         label = "Fair"

#     else:

#         quality = "poor"

#         label = "Poor"


#     return {

#         "score": round(
#             score,
#             1
#         ),

#         "quality":
#             quality,

#         "label":
#             label,

#         "reasons":
#             reasons,

#         "cloud_cover_percent":
#             round(
#                 cloud_cover,
#                 1
#             )
#             if cloud_cover is not None
#             else None
#     }


# # ============================================================
# # MASTER OBSERVATION API
# # ============================================================

# @router.post("/observation/analyze")
# def analyze_observation(

#     latitude: float = Query(...),

#     longitude: float = Query(...),

#     from_date: str = Query(...),

#     to_date: str = Query(...),

#     from_time: str = Query("20:00"),

#     to_time: str = Query("02:00")

# ):

#     try:

#         # ====================================================
#         # 1. WEATHER
#         # ====================================================

#         weather_result = safe_call(
#             get_weather,
#             latitude=latitude,
#             longitude=longitude
#         )

#         weather = weather_result["data"]


#         # ====================================================
#         # 2. SUN
#         # ====================================================

#         sun_result = safe_call(
#             get_sun,
#             latitude=latitude,
#             longitude=longitude,
#             date=from_date
#         )

#         sun = sun_result["data"]


#         # ====================================================
#         # 3. PLANETS
#         # ====================================================

#         planets_result = safe_call(
#             get_planets,
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )

#         planets = planets_result["data"]


#         # ====================================================
#         # 4. DEEP SKY
#         # ====================================================

#         deep_sky_result = safe_call(
#             get_deep_sky,
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )

#         deep_sky = deep_sky_result["data"]


#         # ====================================================
#         # 5. CONSTELLATIONS
#         # ====================================================

#         constellations_result = safe_call(
#             get_constellations,
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )

#         constellations = constellations_result["data"]


#         # ====================================================
#         # 6. METEOR SHOWERS
#         # ====================================================

#         meteor_result = safe_call(
#             get_meteor_showers,
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )

#         meteor_showers = meteor_result["data"]


#         # ====================================================
#         # 7. ASTRONOMICAL WEATHER — 7TIMER
#         # ====================================================

#         astro_weather_result = safe_call(
#             get_astro_weather,
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )

#         astro_weather = astro_weather_result["data"]


#         # ====================================================
#         # 8. ASTRONOMICAL EVENTS
#         # ====================================================

#         events_result = safe_call(
#             get_astronomical_events,
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )

#         events = events_result["data"]


#         # ====================================================
#         # 9. VISIBILITY SUMMARY
#         # ====================================================

#         visibility_summary = build_visibility_summary(

#             planets=planets,

#             deep_sky=deep_sky,

#             constellations=constellations,

#             meteor_showers=meteor_showers,

#             events=events
#         )


#         # ====================================================
#         # 10. DIFFICULTY SUMMARY
#         # ====================================================

#         difficulty_summary = build_difficulty_summary(

#             planets=planets,

#             deep_sky=deep_sky,

#             constellations=constellations,

#             meteor_showers=meteor_showers,

#             events=events
#         )


#         # ====================================================
#         # 11. OVERALL OBSERVATION QUALITY
#         # ====================================================

#         observation_quality = calculate_observation_quality(

#             weather=weather,

#             astro_weather=astro_weather,

#             visibility_summary=visibility_summary
#         )


#         # ====================================================
#         # 12. COMBINED DATA FOR GEMINI
#         # ====================================================

#         astronomy_data = {

#             "location": {

#                 "latitude":
#                     latitude,

#                 "longitude":
#                     longitude
#             },

#             "observation": {

#                 "from_date":
#                     from_date,

#                 "to_date":
#                     to_date,

#                 "from_time":
#                     from_time,

#                 "to_time":
#                     to_time
#             },

#             "weather":
#                 weather,

#             "sun":
#                 sun,

#             "planets":
#                 planets,

#             "deep_sky":
#                 deep_sky,

#             "constellations":
#                 constellations,

#             "meteor_showers":
#                 meteor_showers,

#             "astro_weather":
#                 astro_weather,

#             "events":
#                 events,

#             "visibility_summary":
#                 visibility_summary,

#             "difficulty_summary":
#                 difficulty_summary,

#             "observation_quality":
#                 observation_quality
#         }


#         # ====================================================
#         # 13. GEMINI
#         # ====================================================

#         ai_recommendation = generate_recommendation(
#             astronomy_data
#         )


#         # ====================================================
#         # 14. MODULE STATUS
#         # ====================================================

#         module_status = {

#             "weather":
#                 weather_result["success"],

#             "sun":
#                 sun_result["success"],

#             "planets":
#                 planets_result["success"],

#             "deep_sky":
#                 deep_sky_result["success"],

#             "constellations":
#                 constellations_result["success"],

#             "meteor_showers":
#                 meteor_result["success"],

#             "astro_weather":
#                 astro_weather_result["success"],

#             "astronomical_events":
#                 events_result["success"],

#             "gemini":
#                 True
#         }


#         # ====================================================
#         # 15. FINAL RESPONSE
#         # ====================================================

#         return {

#             "success":
#                 True,

#             "observation": {

#                 "latitude":
#                     latitude,

#                 "longitude":
#                     longitude,

#                 "from_date":
#                     from_date,

#                 "to_date":
#                     to_date,

#                 "from_time":
#                     from_time,

#                 "to_time":
#                     to_time
#             },


#             # ------------------------------------------------
#             # MASTER QUALITY
#             # ------------------------------------------------

#             "observation_quality":
#                 observation_quality,


#             # ------------------------------------------------
#             # VISIBILITY
#             # ------------------------------------------------

#             "visibility_summary":
#                 visibility_summary,


#             # ------------------------------------------------
#             # DIFFICULTY
#             # ------------------------------------------------

#             "difficulty_summary":
#                 difficulty_summary,


#             # ------------------------------------------------
#             # ASTRONOMY DATA
#             # ------------------------------------------------

#             "weather":
#                 weather,

#             "sun":
#                 sun,

#             "planets":
#                 planets,

#             "deep_sky":
#                 deep_sky,

#             "constellations":
#                 constellations,

#             "meteor_showers":
#                 meteor_showers,

#             "astro_weather":
#                 astro_weather,

#             "events":
#                 events,


#             # ------------------------------------------------
#             # AI
#             # ------------------------------------------------

#             "ai_recommendation":
#                 ai_recommendation,


#             # ------------------------------------------------
#             # MODULE STATUS
#             # ------------------------------------------------

#             "module_status":
#                 module_status
#         }


#     # ========================================================
#     # REQUEST ERROR
#     # ========================================================

#     except requests.exceptions.RequestException as e:

#         return {

#             "success":
#                 False,

#             "error":
#                 "External astronomy API request failed",

#             "details":
#                 str(e),

#             "type":
#                 type(e).__name__
#         }


#     # ========================================================
#     # GENERAL ERROR
#     # ========================================================

#     except Exception as e:

#         return {

#             "success":
#                 False,

#             "error":
#                 str(e),

#             "type":
#                 type(e).__name__
#         }


# second code start here 

# import requests

# from fastapi import APIRouter, Query

# from app.api.weather import get_weather
# from app.api.sun import get_sun
# from app.api.planets import get_planets
# from app.api.deep_objects import get_deep_sky
# from app.api.constellations import get_constellations
# from app.api.meteor_showers import get_meteor_showers
# from app.api.weather import get_weather
# from app.api.atronomical_events import get_astronomical_events

# from app.services.ai_recommendation import generate_recommendation


# router = APIRouter()


# # ============================================================
# # HELPER: SAFE MODULE CALL
# # ============================================================

# def safe_call(function, **kwargs):

#     try:

#         result = function(**kwargs)

#         return {
#             "success": True,
#             "data": result
#         }

#     except Exception as e:

#         return {
#             "success": False,
#             "data": None,
#             "error": str(e),
#             "type": type(e).__name__
#         }


# # ============================================================
# # VISIBILITY SUMMARY
# # ============================================================

# def build_visibility_summary(
#     planets,
#     deep_sky,
#     constellations,
#     meteor_showers,
#     events
# ):

#     summary = {

#         "planets": {
#             "visible": 0,
#             "not_visible": 0
#         },

#         "deep_sky": {
#             "visible": 0,
#             "not_visible": 0
#         },

#         "constellations": {
#             "visible": 0,
#             "not_visible": 0
#         },

#         "meteor_showers": {
#             "visible": 0,
#             "not_visible": 0
#         },

#         "astronomical_events": {
#             "visible": 0,
#             "not_visible": 0
#         }
#     }


#     # --------------------------------------------------------
#     # PLANETS
#     # --------------------------------------------------------

#     if isinstance(planets, dict):

#         planet_items = planets.get(
#             "planets",
#             []
#         )

#     elif isinstance(planets, list):

#         planet_items = planets

#     else:

#         planet_items = []


#     for planet in planet_items:

#         if not isinstance(planet, dict):
#             continue

#         if planet.get("visible") is True:

#             summary["planets"]["visible"] += 1

#         elif planet.get("visible") is False:

#             summary["planets"]["not_visible"] += 1


#     # --------------------------------------------------------
#     # DEEP SKY
#     # --------------------------------------------------------

#     if isinstance(deep_sky, dict):

#         deep_items = deep_sky.get(
#             "objects",
#             deep_sky.get(
#                 "deep_sky",
#                 []
#             )
#         )

#     elif isinstance(deep_sky, list):

#         deep_items = deep_sky

#     else:

#         deep_items = []


#     for obj in deep_items:

#         if not isinstance(obj, dict):
#             continue

#         final_obs = obj.get(
#             "final_observability",
#             {}
#         )

#         if final_obs.get("visible") is True:

#             summary["deep_sky"]["visible"] += 1

#         elif final_obs.get("visible") is False:

#             summary["deep_sky"]["not_visible"] += 1


#     # --------------------------------------------------------
#     # CONSTELLATIONS
#     # --------------------------------------------------------

#     if isinstance(constellations, dict):

#         constellation_items = constellations.get(
#             "constellations",
#             []
#         )

#     elif isinstance(constellations, list):

#         constellation_items = constellations

#     else:

#         constellation_items = []


#     for constellation in constellation_items:

#         if not isinstance(constellation, dict):
#             continue

#         final_obs = constellation.get(
#             "final_observability",
#             {}
#         )

#         if final_obs.get("visible") is True:

#             summary["constellations"]["visible"] += 1

#         elif final_obs.get("visible") is False:

#             summary["constellations"]["not_visible"] += 1


#     # --------------------------------------------------------
#     # METEOR SHOWERS
#     # --------------------------------------------------------

#     if isinstance(meteor_showers, dict):

#         meteor_items = meteor_showers.get(
#             "showers",
#             []
#         )

#     elif isinstance(meteor_showers, list):

#         meteor_items = meteor_showers

#     else:

#         meteor_items = []


#     for shower in meteor_items:

#         if not isinstance(shower, dict):
#             continue

#         if shower.get("visible") is True:

#             summary["meteor_showers"]["visible"] += 1

#         elif shower.get("visible") is False:

#             summary["meteor_showers"]["not_visible"] += 1


#     # --------------------------------------------------------
#     # ASTRONOMICAL EVENTS
#     # --------------------------------------------------------

#     if isinstance(events, dict):

#         event_data = events.get(
#             "events",
#             {}
#         )

#         event_items = []

#         if isinstance(event_data, dict):

#             for key in [
#                 "eclipses",
#                 "conjunctions",
#                 "oppositions",
#                 "occultations"
#             ]:

#                 items = event_data.get(
#                     key,
#                     []
#                 )

#                 if isinstance(items, list):

#                     event_items.extend(items)

#     elif isinstance(events, list):

#         event_items = events

#     else:

#         event_items = []


#     for event in event_items:

#         if not isinstance(event, dict):
#             continue

#         visibility = event.get(
#             "visibility",
#             {}
#         )

#         if visibility.get("visible") is True:

#             summary["astronomical_events"]["visible"] += 1

#         elif visibility.get("visible") is False:

#             summary["astronomical_events"]["not_visible"] += 1


#     return summary


# # ============================================================
# # DIFFICULTY SUMMARY
# # ============================================================

# def build_difficulty_summary(
#     planets,
#     deep_sky,
#     constellations,
#     meteor_showers,
#     events
# ):

#     summary = {

#         "easy": 0,
#         "moderate": 0,
#         "hard": 0,
#         "very_hard": 0,
#         "unknown": 0
#     }


#     def add_difficulty(item):

#         if not isinstance(item, dict):
#             return

#         difficulty = item.get(
#             "difficulty"
#         )

#         if isinstance(difficulty, dict):

#             level = difficulty.get(
#                 "level",
#                 "unknown"
#             )

#             if level in summary:

#                 summary[level] += 1

#             else:

#                 summary["unknown"] += 1

#             return

#         # Some modules may use a simple difficulty value
#         level = item.get(
#             "difficulty_level"
#         )

#         if level in summary:

#             summary[level] += 1

#         else:

#             summary["unknown"] += 1


#     # --------------------------------------------------------
#     # PLANETS
#     # --------------------------------------------------------

#     if isinstance(planets, dict):

#         items = planets.get(
#             "planets",
#             []
#         )

#     elif isinstance(planets, list):

#         items = planets

#     else:

#         items = []


#     for item in items:
#         add_difficulty(item)


#     # --------------------------------------------------------
#     # DEEP SKY
#     # --------------------------------------------------------

#     if isinstance(deep_sky, dict):

#         items = deep_sky.get(
#             "objects",
#             deep_sky.get(
#                 "deep_sky",
#                 []
#             )
#         )

#     elif isinstance(deep_sky, list):

#         items = deep_sky

#     else:

#         items = []


#     for item in items:
#         add_difficulty(item)


#     # --------------------------------------------------------
#     # CONSTELLATIONS
#     # --------------------------------------------------------

#     if isinstance(constellations, dict):

#         items = constellations.get(
#             "constellations",
#             []
#         )

#     elif isinstance(constellations, list):

#         items = constellations

#     else:

#         items = []


#     for item in items:
#         add_difficulty(item)


#     # --------------------------------------------------------
#     # METEOR SHOWERS
#     # --------------------------------------------------------

#     if isinstance(meteor_showers, dict):

#         items = meteor_showers.get(
#             "showers",
#             []
#         )

#     elif isinstance(meteor_showers, list):

#         items = meteor_showers

#     else:

#         items = []


#     for item in items:
#         add_difficulty(item)


#     # --------------------------------------------------------
#     # EVENTS
#     # --------------------------------------------------------

#     if isinstance(events, dict):

#         event_data = events.get(
#             "events",
#             {}
#         )

#         items = []

#         if isinstance(event_data, dict):

#             for key in [
#                 "eclipses",
#                 "conjunctions",
#                 "oppositions",
#                 "occultations"
#             ]:

#                 event_items = event_data.get(
#                     key,
#                     []
#                 )

#                 if isinstance(event_items, list):

#                     items.extend(
#                         event_items
#                     )

#     elif isinstance(events, list):

#         items = events

#     else:

#         items = []


#     for item in items:
#         add_difficulty(item)


#     return summary


# # ============================================================
# # OBSERVATION QUALITY
# # ============================================================

# def calculate_observation_quality(
#     weather,
#     astro_weather,
#     visibility_summary
# ):

#     score = 5.0

#     reasons = []


#     # --------------------------------------------------------
#     # WEATHER
#     # --------------------------------------------------------

#     cloud_cover = None

#     try:

#         if isinstance(weather, dict):

#             hourly = weather.get(
#                 "hourly",
#                 {}
#             )

#             clouds = hourly.get(
#                 "cloud_cover",
#                 []
#             )

#             if clouds:

#                 valid_clouds = [
#                     float(c)
#                     for c in clouds
#                     if c is not None
#                 ]

#                 if valid_clouds:

#                     cloud_cover = (
#                         sum(valid_clouds)
#                         / len(valid_clouds)
#                     )

#     except Exception:
#         cloud_cover = None


#     if cloud_cover is not None:

#         if cloud_cover <= 10:

#             score += 4

#             reasons.append(
#                 "Very low cloud cover."
#             )

#         elif cloud_cover <= 30:

#             score += 3

#             reasons.append(
#                 "Low cloud cover."
#             )

#         elif cloud_cover <= 60:

#             score += 1

#             reasons.append(
#                 "Some cloud cover may interfere."
#             )

#         elif cloud_cover <= 80:

#             score -= 2

#             reasons.append(
#                 "High cloud cover may interfere."
#             )

#         else:

#             score -= 4

#             reasons.append(
#                 "Heavy cloud cover is likely."
#             )


#     # --------------------------------------------------------
#     # VISIBLE TARGETS
#     # --------------------------------------------------------

#     visible_count = 0

#     for category in visibility_summary.values():

#         if isinstance(category, dict):

#             visible_count += category.get(
#                 "visible",
#                 0
#             )


#     if visible_count >= 8:

#         score += 1

#         reasons.append(
#             "Many astronomical targets are available."
#         )

#     elif visible_count >= 4:

#         score += 0.5

#         reasons.append(
#             "Several astronomical targets are available."
#         )

#     elif visible_count == 0:

#         score -= 2

#         reasons.append(
#             "No clearly visible targets were returned."
#         )


#     # --------------------------------------------------------
#     # LIMIT SCORE
#     # --------------------------------------------------------

#     score = max(
#         0,
#         min(
#             10,
#             score
#         )
#     )


#     # --------------------------------------------------------
#     # LABEL
#     # --------------------------------------------------------

#     if score >= 8.5:

#         quality = "excellent"

#         label = "Excellent"

#     elif score >= 7:

#         quality = "very_good"

#         label = "Very Good"

#     elif score >= 5:

#         quality = "good"

#         label = "Good"

#     elif score >= 3:

#         quality = "fair"

#         label = "Fair"

#     else:

#         quality = "poor"

#         label = "Poor"


#     return {

#         "score": round(
#             score,
#             1
#         ),

#         "quality":
#             quality,

#         "label":
#             label,

#         "reasons":
#             reasons,

#         "cloud_cover_percent":
#             round(
#                 cloud_cover,
#                 1
#             )
#             if cloud_cover is not None
#             else None
#     }


# # ============================================================
# # MASTER OBSERVATION API
# # ============================================================

# @router.post("/observation/analyze")
# def analyze_observation(

#     latitude: float = Query(...),

#     longitude: float = Query(...),

#     from_date: str = Query(...),

#     to_date: str = Query(...),

#     from_time: str = Query("20:00"),

#     to_time: str = Query("02:00")

# ):

#     try:

#         # ====================================================
#         # 1. WEATHER
#         # ====================================================

#         weather_result = safe_call(
#             get_weather,
#             latitude=latitude,
#             longitude=longitude
#         )

#         weather = weather_result["data"]


#         # ====================================================
#         # 2. SUN
#         # ====================================================

#         sun_result = safe_call(
#             get_sun,
#             latitude=latitude,
#             longitude=longitude,
#             date=from_date
#         )

#         sun = sun_result["data"]


#         # ====================================================
#         # 3. PLANETS
#         # ====================================================

#         planets_result = safe_call(
#             get_planets,
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )

#         planets = planets_result["data"]


#         # ====================================================
#         # 4. DEEP SKY
#         # ====================================================

#         deep_sky_result = safe_call(
#             get_deep_sky,
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )

#         deep_sky = deep_sky_result["data"]


#         # ====================================================
#         # 5. CONSTELLATIONS
#         # ====================================================

#         constellations_result = safe_call(
#             get_constellations,
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )

#         constellations = constellations_result["data"]


#         # ====================================================
#         # 6. METEOR SHOWERS
#         # ====================================================

#         meteor_result = safe_call(
#             get_meteor_showers,
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )

#         meteor_showers = meteor_result["data"]


#         # ====================================================
#         # 7. ASTRONOMICAL WEATHER — 7TIMER
#         # ====================================================

#         astro_weather_result = safe_call(
#             get_weather,
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )

#         astro_weather = astro_weather_result["data"]


#         # ====================================================
#         # 8. ASTRONOMICAL EVENTS
#         # ====================================================

#         events_result = safe_call(
#             get_astronomical_events,
#             latitude=latitude,
#             longitude=longitude,
#             from_date=from_date,
#             to_date=to_date,
#             from_time=from_time,
#             to_time=to_time
#         )

#         events = events_result["data"]


#         # ====================================================
#         # 9. VISIBILITY SUMMARY
#         # ====================================================

#         visibility_summary = build_visibility_summary(

#             planets=planets,

#             deep_sky=deep_sky,

#             constellations=constellations,

#             meteor_showers=meteor_showers,

#             events=events
#         )


#         # ====================================================
#         # 10. DIFFICULTY SUMMARY
#         # ====================================================

#         difficulty_summary = build_difficulty_summary(

#             planets=planets,

#             deep_sky=deep_sky,

#             constellations=constellations,

#             meteor_showers=meteor_showers,

#             events=events
#         )


#         # ====================================================
#         # 11. OVERALL OBSERVATION QUALITY
#         # ====================================================

#         observation_quality = calculate_observation_quality(

#             weather=weather,

#             astro_weather=astro_weather,

#             visibility_summary=visibility_summary
#         )


#         # ====================================================
#         # 12. COMBINED DATA FOR GEMINI
#         # ====================================================

#         astronomy_data = {

#             "location": {

#                 "latitude":
#                     latitude,

#                 "longitude":
#                     longitude
#             },

#             "observation": {

#                 "from_date":
#                     from_date,

#                 "to_date":
#                     to_date,

#                 "from_time":
#                     from_time,

#                 "to_time":
#                     to_time
#             },

#             "weather":
#                 weather,

#             "sun":
#                 sun,

#             "planets":
#                 planets,

#             "deep_sky":
#                 deep_sky,

#             "constellations":
#                 constellations,

#             "meteor_showers":
#                 meteor_showers,

#             "astro_weather":
#                 astro_weather,

#             "events":
#                 events,

#             "visibility_summary":
#                 visibility_summary,

#             "difficulty_summary":
#                 difficulty_summary,

#             "observation_quality":
#                 observation_quality
#         }


#         # ====================================================
#         # 13. GEMINI
#         # ====================================================

#         ai_recommendation = generate_recommendation(
#             astronomy_data
#         )


#         # ====================================================
#         # 14. MODULE STATUS
#         # ====================================================

#         module_status = {

#             "weather":
#                 weather_result["success"],

#             "sun":
#                 sun_result["success"],

#             "planets":
#                 planets_result["success"],

#             "deep_sky":
#                 deep_sky_result["success"],

#             "constellations":
#                 constellations_result["success"],

#             "meteor_showers":
#                 meteor_result["success"],

#             "astro_weather":
#                 astro_weather_result["success"],

#             "astronomical_events":
#                 events_result["success"],

#             "gemini":
#                 True
#         }


#         # ====================================================
#         # 15. FINAL RESPONSE
#         # ====================================================

#         return {

#             "success":
#                 True,

#             "observation": {

#                 "latitude":
#                     latitude,

#                 "longitude":
#                     longitude,

#                 "from_date":
#                     from_date,

#                 "to_date":
#                     to_date,

#                 "from_time":
#                     from_time,

#                 "to_time":
#                     to_time
#             },


#             # ------------------------------------------------
#             # MASTER QUALITY
#             # ------------------------------------------------

#             "observation_quality":
#                 observation_quality,


#             # ------------------------------------------------
#             # VISIBILITY
#             # ------------------------------------------------

#             "visibility_summary":
#                 visibility_summary,


#             # ------------------------------------------------
#             # DIFFICULTY
#             # ------------------------------------------------

#             "difficulty_summary":
#                 difficulty_summary,


#             # ------------------------------------------------
#             # ASTRONOMY DATA
#             # ------------------------------------------------

#             "weather":
#                 weather,

#             "sun":
#                 sun,

#             "planets":
#                 planets,

#             "deep_sky":
#                 deep_sky,

#             "constellations":
#                 constellations,

#             "meteor_showers":
#                 meteor_showers,

#             "astro_weather":
#                 astro_weather,

#             "events":
#                 events,


#             # ------------------------------------------------
#             # AI
#             # ------------------------------------------------

#             "ai_recommendation":
#                 ai_recommendation,


#             # ------------------------------------------------
#             # MODULE STATUS
#             # ------------------------------------------------

#             "module_status":
#                 module_status
#         }


#     # ========================================================
#     # REQUEST ERROR
#     # ========================================================

#     except requests.exceptions.RequestException as e:

#         return {

#             "success":
#                 False,

#             "error":
#                 "External astronomy API request failed",

#             "details":
#                 str(e),

#             "type":
#                 type(e).__name__
#         }


#     # ========================================================
#     # GENERAL ERROR
#     # ========================================================

#     except Exception as e:

#         return {

#             "success":
#                 False,

#             "error":
#                 str(e),

#             "type":
#                 type(e).__name__
#         }


# import requests

# from fastapi import APIRouter, Query

# from app.api.weather import get_weather
# from app.api.sun import get_sun
# from app.api.planets import get_planets
# from app.api.deep_objects import get_deep_sky
# from app.api.constellations import get_constellations
# from app.api.meteor_showers import get_meteor_showers
# from app.api.weather import get_weather
# from app.api.atronomical_events import get_astronomical_events

# from app.services.ai_recommendation import generate_recommendation


# router = APIRouter()


# # ============================================================
# # SAFE MODULE CALL
# # ============================================================

# def safe_call(function, **kwargs):

#     try:

#         result = function(**kwargs)

#         return {
#             "success": True,
#             "data": result,
#             "error": None,
#             "type": None
#         }

#     except Exception as e:

#         return {
#             "success": False,
#             "data": None,
#             "error": str(e),
#             "type": type(e).__name__
#         }


# # ============================================================
# # NORMALIZE ONE OBJECT
# #
# # Every astronomy object should expose:
# #
# # visible
# # observability
# # naked_eye
# # difficulty
# # recommendation
# # ============================================================

# def normalize_object(item):

#     if not isinstance(item, dict):
#         return item

#     # --------------------------------------------------------
#     # VISIBLE
#     # --------------------------------------------------------

#     if "visible" not in item:
#         item["visible"] = None


#     # --------------------------------------------------------
#     # OBSERVABILITY
#     # --------------------------------------------------------

#     if "observability" not in item:

#         final_obs = item.get(
#             "final_observability"
#         )

#         if isinstance(final_obs, dict):

#             item["observability"] = final_obs.get(
#                 "quality"
#             )

#         else:

#             item["observability"] = None


#     # --------------------------------------------------------
#     # NAKED EYE
#     # --------------------------------------------------------

#     if "naked_eye" not in item:

#         item["naked_eye"] = None


#     # --------------------------------------------------------
#     # DIFFICULTY
#     # --------------------------------------------------------

#     difficulty = item.get(
#         "difficulty"
#     )

#     if isinstance(difficulty, dict):

#         item["difficulty"] = difficulty

#     elif difficulty is not None:

#         item["difficulty"] = {
#             "level": str(difficulty),
#             "label": str(difficulty)
#         }

#     else:

#         item["difficulty"] = {
#             "level": "unknown",
#             "label": "Unknown",
#             "recommendation": None
#         }


#     # --------------------------------------------------------
#     # RECOMMENDATION
#     # --------------------------------------------------------

#     if "recommendation" not in item:

#         difficulty_data = item.get(
#             "difficulty",
#             {}
#         )

#         if isinstance(difficulty_data, dict):

#             item["recommendation"] = difficulty_data.get(
#                 "recommendation"
#             )

#         else:

#             item["recommendation"] = None


#     return item


# # ============================================================
# # NORMALIZE LIST
# # ============================================================

# def normalize_list(items):

#     if not isinstance(items, list):
#         return items

#     return [
#         normalize_object(item)
#         for item in items
#         if isinstance(item, dict)
#     ]


# # ============================================================
# # NORMALIZE MODULE DATA
# # ============================================================

# def normalize_module_data(data, possible_keys):

#     if not isinstance(data, dict):
#         return data

#     for key in possible_keys:

#         if key in data and isinstance(
#             data[key],
#             list
#         ):

#             data[key] = normalize_list(
#                 data[key]
#             )

#             return data

#     return data


# # ============================================================
# # NORMALIZE ASTRONOMICAL EVENTS
# # ============================================================

# def normalize_events(events):

#     if not isinstance(events, dict):
#         return events

#     event_data = events.get(
#         "events"
#     )

#     if not isinstance(event_data, dict):
#         return events

#     event_types = [
#         "eclipses",
#         "conjunctions",
#         "oppositions",
#         "occultations"
#     ]

#     for event_type in event_types:

#         items = event_data.get(
#             event_type
#         )

#         if isinstance(items, list):

#             event_data[event_type] = normalize_list(
#                 items
#             )

#     events["events"] = event_data

#     return events


# # ============================================================
# # VISIBILITY SUMMARY
# # ============================================================

# def build_visibility_summary(
#     planets,
#     deep_sky,
#     constellations,
#     meteor_showers,
#     events
# ):

#     summary = {

#         "planets": {
#             "visible": 0,
#             "not_visible": 0,
#             "unknown": 0
#         },

#         "deep_sky": {
#             "visible": 0,
#             "not_visible": 0,
#             "unknown": 0
#         },

#         "constellations": {
#             "visible": 0,
#             "not_visible": 0,
#             "unknown": 0
#         },

#         "meteor_showers": {
#             "visible": 0,
#             "not_visible": 0,
#             "unknown": 0
#         },

#         "astronomical_events": {
#             "visible": 0,
#             "not_visible": 0,
#             "unknown": 0
#         }
#     }


#     # ========================================================
#     # PLANETS
#     # ========================================================

#     if isinstance(planets, dict):

#         items = planets.get(
#             "planets",
#             []
#         )

#     elif isinstance(planets, list):

#         items = planets

#     else:

#         items = []


#     for item in items:

#         if not isinstance(item, dict):
#             continue

#         visible = item.get(
#             "visible"
#         )

#         if visible is True:

#             summary["planets"]["visible"] += 1

#         elif visible is False:

#             summary["planets"]["not_visible"] += 1

#         else:

#             summary["planets"]["unknown"] += 1


#     # ========================================================
#     # DEEP SKY
#     # ========================================================

#     if isinstance(deep_sky, dict):

#         items = deep_sky.get(
#             "objects",
#             deep_sky.get(
#                 "deep_sky",
#                 []
#             )
#         )

#     elif isinstance(deep_sky, list):

#         items = deep_sky

#     else:

#         items = []


#     for item in items:

#         if not isinstance(item, dict):
#             continue

#         final_obs = item.get(
#             "final_observability",
#             {}
#         )

#         if isinstance(final_obs, dict):

#             visible = final_obs.get(
#                 "visible"
#             )

#         else:

#             visible = item.get(
#                 "visible"
#             )

#         if visible is True:

#             summary["deep_sky"]["visible"] += 1

#         elif visible is False:

#             summary["deep_sky"]["not_visible"] += 1

#         else:

#             summary["deep_sky"]["unknown"] += 1


#     # ========================================================
#     # CONSTELLATIONS
#     # ========================================================

#     if isinstance(constellations, dict):

#         items = constellations.get(
#             "constellations",
#             []
#         )

#     elif isinstance(constellations, list):

#         items = constellations

#     else:

#         items = []


#     for item in items:

#         if not isinstance(item, dict):
#             continue

#         final_obs = item.get(
#             "final_observability",
#             {}
#         )

#         if isinstance(final_obs, dict):

#             visible = final_obs.get(
#                 "visible"
#             )

#         else:

#             visible = item.get(
#                 "visible"
#             )

#         if visible is True:

#             summary["constellations"]["visible"] += 1

#         elif visible is False:

#             summary["constellations"]["not_visible"] += 1

#         else:

#             summary["constellations"]["unknown"] += 1


#     # ========================================================
#     # METEOR SHOWERS
#     # ========================================================

#     if isinstance(meteor_showers, dict):

#         items = meteor_showers.get(
#             "showers",
#             []
#         )

#     elif isinstance(meteor_showers, list):

#         items = meteor_showers

#     else:

#         items = []


#     for item in items:

#         if not isinstance(item, dict):
#             continue

#         visible = item.get(
#             "visible"
#         )

#         if visible is True:

#             summary["meteor_showers"]["visible"] += 1

#         elif visible is False:

#             summary["meteor_showers"]["not_visible"] += 1

#         else:

#             summary["meteor_showers"]["unknown"] += 1


#     # ========================================================
#     # ASTRONOMICAL EVENTS
#     # ========================================================

#     event_items = []

#     if isinstance(events, dict):

#         event_data = events.get(
#             "events",
#             {}
#         )

#         if isinstance(event_data, dict):

#             for event_type in [
#                 "eclipses",
#                 "conjunctions",
#                 "oppositions",
#                 "occultations"
#             ]:

#                 items = event_data.get(
#                     event_type,
#                     []
#                 )

#                 if isinstance(items, list):

#                     event_items.extend(
#                         items
#                     )


#     elif isinstance(events, list):

#         event_items = events


#     for item in event_items:

#         if not isinstance(item, dict):
#             continue

#         visibility = item.get(
#             "visibility",
#             {}
#         )

#         if isinstance(visibility, dict):

#             visible = visibility.get(
#                 "visible"
#             )

#         else:

#             visible = item.get(
#                 "visible"
#             )

#         if visible is True:

#             summary[
#                 "astronomical_events"
#             ]["visible"] += 1

#         elif visible is False:

#             summary[
#                 "astronomical_events"
#             ]["not_visible"] += 1

#         else:

#             summary[
#                 "astronomical_events"
#             ]["unknown"] += 1


#     return summary


# # ============================================================
# # DIFFICULTY SUMMARY
# # ============================================================

# def build_difficulty_summary(
#     planets,
#     deep_sky,
#     constellations,
#     meteor_showers,
#     events
# ):

#     summary = {

#         "easy": 0,
#         "moderate": 0,
#         "hard": 0,
#         "very_hard": 0,
#         "unknown": 0
#     }


#     def add_item(item):

#         if not isinstance(item, dict):
#             return


#         difficulty = item.get(
#             "difficulty"
#         )


#         # ----------------------------------------------------
#         # DICTIONARY
#         # ----------------------------------------------------

#         if isinstance(
#             difficulty,
#             dict
#         ):

#             level = difficulty.get(
#                 "level",
#                 "unknown"
#             )

#         else:

#             level = item.get(
#                 "difficulty_level",
#                 "unknown"
#             )


#         if level in summary:

#             summary[level] += 1

#         else:

#             summary["unknown"] += 1


#     # ========================================================
#     # PLANETS
#     # ========================================================

#     if isinstance(planets, dict):

#         items = planets.get(
#             "planets",
#             []
#         )

#     elif isinstance(planets, list):

#         items = planets

#     else:

#         items = []


#     for item in items:
#         add_item(item)


#     # ========================================================
#     # DEEP SKY
#     # ========================================================

#     if isinstance(deep_sky, dict):

#         items = deep_sky.get(
#             "objects",
#             deep_sky.get(
#                 "deep_sky",
#                 []
#             )
#         )

#     elif isinstance(deep_sky, list):

#         items = deep_sky

#     else:

#         items = []


#     for item in items:
#         add_item(item)


#     # ========================================================
#     # CONSTELLATIONS
#     # ========================================================

#     if isinstance(constellations, dict):

#         items = constellations.get(
#             "constellations",
#             []
#         )

#     elif isinstance(constellations, list):

#         items = constellations

#     else:

#         items = []


#     for item in items:
#         add_item(item)


#     # ========================================================
#     # METEOR SHOWERS
#     # ========================================================

#     if isinstance(meteor_showers, dict):

#         items = meteor_showers.get(
#             "showers",
#             []
#         )

#     elif isinstance(meteor_showers, list):

#         items = meteor_showers

#     else:

#         items = []


#     for item in items:
#         add_item(item)


#     # ========================================================
#     # EVENTS
#     # ========================================================

#     event_items = []

#     if isinstance(events, dict):

#         event_data = events.get(
#             "events",
#             {}
#         )

#         if isinstance(event_data, dict):

#             for event_type in [
#                 "eclipses",
#                 "conjunctions",
#                 "oppositions",
#                 "occultations"
#             ]:

#                 items = event_data.get(
#                     event_type,
#                     []
#                 )

#                 if isinstance(items, list):

#                     event_items.extend(
#                         items
#                     )

#     elif isinstance(events, list):

#         event_items = events


#     for item in event_items:
#         add_item(item)


#     return summary


# # ============================================================
# # OVERALL OBSERVATION QUALITY
# # ============================================================

# def calculate_observation_quality(
#     weather,
#     astro_weather,
#     visibility_summary
# ):

#     score = 5.0

#     reasons = []


#     # ========================================================
#     # CLOUD COVER
#     # ========================================================

#     cloud_cover = None


#     try:

#         if isinstance(weather, dict):

#             hourly = weather.get(
#                 "hourly",
#                 {}
#             )

#             clouds = hourly.get(
#                 "cloud_cover",
#                 []
#             )

#             if isinstance(
#                 clouds,
#                 list
#             ):

#                 valid_clouds = []

#                 for cloud in clouds:

#                     if cloud is None:
#                         continue

#                     try:

#                         valid_clouds.append(
#                             float(cloud)
#                         )

#                     except (
#                         ValueError,
#                         TypeError
#                     ):

#                         continue


#                 if valid_clouds:

#                     cloud_cover = (
#                         sum(valid_clouds)
#                         /
#                         len(valid_clouds)
#                     )


#     except Exception:

#         cloud_cover = None


#     # ========================================================
#     # CLOUD SCORE
#     # ========================================================

#     if cloud_cover is not None:

#         if cloud_cover <= 10:

#             score += 4

#             reasons.append(
#                 "Very low cloud cover."
#             )

#         elif cloud_cover <= 30:

#             score += 3

#             reasons.append(
#                 "Low cloud cover."
#             )

#         elif cloud_cover <= 60:

#             score += 1

#             reasons.append(
#                 "Some cloud cover may interfere."
#             )

#         elif cloud_cover <= 80:

#             score -= 2

#             reasons.append(
#                 "High cloud cover may interfere."
#             )

#         else:

#             score -= 4

#             reasons.append(
#                 "Heavy cloud cover is likely."
#             )


#     # ========================================================
#     # VISIBLE TARGET COUNT
#     # ========================================================

#     visible_count = 0


#     for category in visibility_summary.values():

#         if isinstance(category, dict):

#             visible_count += category.get(
#                 "visible",
#                 0
#             )


#     if visible_count >= 8:

#         score += 1

#         reasons.append(
#             "Many astronomical targets are available."
#         )

#     elif visible_count >= 4:

#         score += 0.5

#         reasons.append(
#             "Several astronomical targets are available."
#         )

#     elif visible_count == 0:

#         score -= 2

#         reasons.append(
#             "No clearly visible targets were returned."
#         )


#     # ========================================================
#     # LIMIT SCORE
#     # ========================================================

#     score = max(
#         0,
#         min(
#             10,
#             score
#         )
#     )


#     # ========================================================
#     # QUALITY LABEL
#     # ========================================================

#     if score >= 8.5:

#         quality = "excellent"
#         label = "Excellent"

#     elif score >= 7:

#         quality = "very_good"
#         label = "Very Good"

#     elif score >= 5:

#         quality = "good"
#         label = "Good"

#     elif score >= 3:

#         quality = "fair"
#         label = "Fair"

#     else:

#         quality = "poor"
#         label = "Poor"


#     return {

#         "score": round(
#             score,
#             1
#         ),

#         "quality": quality,

#         "label": label,

#         "reasons": reasons,

#         "cloud_cover_percent":
#             round(
#                 cloud_cover,
#                 1
#             )
#             if cloud_cover is not None
#             else None
#     }


# # ============================================================
# # MASTER OBSERVATION API
# # ============================================================

# @router.post(
#     "/observation/analyze"
# )
# def analyze_observation(

#     latitude: float = Query(...),

#     longitude: float = Query(...),

#     from_date: str = Query(...),

#     to_date: str = Query(...),

#     from_time: str = Query(
#         "20:00"
#     ),

#     to_time: str = Query(
#         "02:00"
#     )

# ):

#     try:

#         # ====================================================
#         # 1. WEATHER
#         # ====================================================

#         weather_result = safe_call(

#             get_weather,

#             latitude=latitude,

#             longitude=longitude
#         )

#         weather = weather_result[
#             "data"
#         ]


#         # ====================================================
#         # 2. SUN
#         # ====================================================

#         sun_result = safe_call(

#             get_sun,

#             latitude=latitude,

#             longitude=longitude,

#             date=from_date
#         )

#         sun = sun_result[
#             "data"
#         ]


#         # ====================================================
#         # 3. PLANETS
#         # ====================================================

#         planets_result = safe_call(

#             get_planets,

#             latitude=latitude,

#             longitude=longitude,

#             from_date=from_date,

#             to_date=to_date,

#             from_time=from_time,

#             to_time=to_time
#         )

#         planets = planets_result[
#             "data"
#         ]


#         # ====================================================
#         # 4. DEEP SKY
#         # ====================================================

#         deep_sky_result = safe_call(

#             get_deep_sky,

#             latitude=latitude,

#             longitude=longitude,

#             from_date=from_date,

#             to_date=to_date,

#             from_time=from_time,

#             to_time=to_time
#         )

#         deep_sky = deep_sky_result[
#             "data"
#         ]


#         # ====================================================
#         # 5. CONSTELLATIONS
#         # ====================================================

#         constellations_result = safe_call(

#             get_constellations,

#             latitude=latitude,

#             longitude=longitude,

#             from_date=from_date,

#             to_date=to_date,

#             from_time=from_time,

#             to_time=to_time
#         )

#         constellations = constellations_result[
#             "data"
#         ]


#         # ====================================================
#         # 6. METEOR SHOWERS
#         # ====================================================

#         meteor_result = safe_call(

#             get_meteor_showers,

#             latitude=latitude,

#             longitude=longitude,

#             from_date=from_date,

#             to_date=to_date,

#             from_time=from_time,

#             to_time=to_time
#         )

#         meteor_showers = meteor_result[
#             "data"
#         ]


#         # ====================================================
#         # 7. ASTRONOMICAL WEATHER
#         # ====================================================

#         astro_weather_result = safe_call(

#             get_weather,

#             latitude=latitude,

#             longitude=longitude,

#             from_date=from_date,

#             to_date=to_date,

#             from_time=from_time,

#             to_time=to_time
#         )

#         astro_weather = astro_weather_result[
#             "data"
#         ]


#         # ====================================================
#         # 8. ASTRONOMICAL EVENTS
#         # ====================================================

#         events_result = safe_call(

#             get_astronomical_events,

#             latitude=latitude,

#             longitude=longitude,

#             from_date=from_date,

#             to_date=to_date,

#             from_time=from_time,

#             to_time=to_time
#         )

#         events = events_result[
#             "data"
#         ]


#         # ====================================================
#         # 9. NORMALIZE ALL OBJECTS
#         # ====================================================

#         planets = normalize_module_data(
#             planets,
#             ["planets"]
#         )


#         deep_sky = normalize_module_data(
#             deep_sky,
#             [
#                 "objects",
#                 "deep_sky"
#             ]
#         )


#         constellations = normalize_module_data(
#             constellations,
#             [
#                 "constellations"
#             ]
#         )


#         meteor_showers = normalize_module_data(
#             meteor_showers,
#             [
#                 "showers"
#             ]
#         )


#         events = normalize_events(
#             events
#         )


#         # ====================================================
#         # 10. VISIBILITY SUMMARY
#         # ====================================================

#         visibility_summary = build_visibility_summary(

#             planets=planets,

#             deep_sky=deep_sky,

#             constellations=constellations,

#             meteor_showers=meteor_showers,

#             events=events
#         )


#         # ====================================================
#         # 11. DIFFICULTY SUMMARY
#         # ====================================================

#         difficulty_summary = build_difficulty_summary(

#             planets=planets,

#             deep_sky=deep_sky,

#             constellations=constellations,

#             meteor_showers=meteor_showers,

#             events=events
#         )


#         # ====================================================
#         # 12. OVERALL OBSERVATION QUALITY
#         # ====================================================

#         observation_quality = calculate_observation_quality(

#             weather=weather,

#             astro_weather=astro_weather,

#             visibility_summary=visibility_summary
#         )


#         # ====================================================
#         # 13. ALL DATA FOR GEMINI
#         # ====================================================

#         astronomy_data = {

#             "location": {

#                 "latitude":
#                     latitude,

#                 "longitude":
#                     longitude
#             },


#             "observation": {

#                 "from_date":
#                     from_date,

#                 "to_date":
#                     to_date,

#                 "from_time":
#                     from_time,

#                 "to_time":
#                     to_time
#             },


#             "weather":
#                 weather,


#             "sun":
#                 sun,


#             "planets":
#                 planets,


#             "deep_sky":
#                 deep_sky,


#             "constellations":
#                 constellations,


#             "meteor_showers":
#                 meteor_showers,


#             "astro_weather":
#                 astro_weather,


#             "events":
#                 events,


#             "visibility_summary":
#                 visibility_summary,


#             "difficulty_summary":
#                 difficulty_summary,


#             "observation_quality":
#                 observation_quality
#         }


#         # ====================================================
#         # 14. GEMINI
#         # ====================================================

#         ai_recommendation = None

#         gemini_success = False

#         gemini_error = None


#         try:

#             ai_recommendation = generate_recommendation(
#                 astronomy_data
#             )

#             gemini_success = True


#         except Exception as e:

#             gemini_error = str(e)

#             ai_recommendation = {

#                 "score": None,

#                 "recommendation":
#                     "AI recommendation is temporarily unavailable.",

#                 "best_time": None,

#                 "best_targets": [],

#                 "weather_summary": "",

#                 "astronomy_summary": "",

#                 "tips": []
#             }


#         # ====================================================
#         # 15. MODULE STATUS
#         # ====================================================

#         module_status = {

#             "weather":
#                 weather_result[
#                     "success"
#                 ],

#             "sun":
#                 sun_result[
#                     "success"
#                 ],

#             "planets":
#                 planets_result[
#                     "success"
#                 ],

#             "deep_sky":
#                 deep_sky_result[
#                     "success"
#                 ],

#             "constellations":
#                 constellations_result[
#                     "success"
#                 ],

#             "meteor_showers":
#                 meteor_result[
#                     "success"
#                 ],

#             "astro_weather":
#                 astro_weather_result[
#                     "success"
#                 ],

#             "astronomical_events":
#                 events_result[
#                     "success"
#                 ],

#             "gemini":
#                 gemini_success
#         }


#         if gemini_error:

#             module_status[
#                 "gemini_error"
#             ] = gemini_error


#         # ====================================================
#         # 16. FINAL RESPONSE
#         # ====================================================

#         return {

#             "success":
#                 True,


#             # =================================================
#             # OBSERVATION
#             # =================================================

#             "observation": {

#                 "latitude":
#                     latitude,

#                 "longitude":
#                     longitude,

#                 "from_date":
#                     from_date,

#                 "to_date":
#                     to_date,

#                 "from_time":
#                     from_time,

#                 "to_time":
#                     to_time
#             },


#             # =================================================
#             # OVERALL QUALITY
#             # =================================================

#             "observation_quality":
#                 observation_quality,


#             # =================================================
#             # VISIBILITY SUMMARY
#             # =================================================

#             "visibility_summary":
#                 visibility_summary,


#             # =================================================
#             # DIFFICULTY SUMMARY
#             # =================================================

#             "difficulty_summary":
#                 difficulty_summary,


#             # =================================================
#             # WEATHER
#             # =================================================

#             "weather":
#                 weather,


#             # =================================================
#             # SUN
#             # =================================================

#             "sun":
#                 sun,


#             # =================================================
#             # PLANETS
#             #
#             # Every planet object contains:
#             #
#             # visible
#             # observability
#             # naked_eye
#             # difficulty
#             # recommendation
#             # =================================================

#             "planets":
#                 planets,


#             # =================================================
#             # DEEP SKY
#             #
#             # Every object contains:
#             #
#             # visible
#             # observability
#             # naked_eye
#             # difficulty
#             # recommendation
#             # =================================================

#             "deep_sky":
#                 deep_sky,


#             # =================================================
#             # CONSTELLATIONS
#             #
#             # Every constellation contains:
#             #
#             # visible
#             # observability
#             # naked_eye
#             # difficulty
#             # recommendation
#             # =================================================

#             "constellations":
#                 constellations,


#             # =================================================
#             # METEOR SHOWERS
#             #
#             # Every shower contains:
#             #
#             # visible
#             # observability
#             # naked_eye
#             # difficulty
#             # recommendation
#             # =================================================

#             "meteor_showers":
#                 meteor_showers,


#             # =================================================
#             # ASTRONOMICAL WEATHER
#             # =================================================

#             "astro_weather":
#                 astro_weather,


#             # =================================================
#             # ASTRONOMICAL EVENTS
#             #
#             # Every event contains:
#             #
#             # visible
#             # observability
#             # naked_eye
#             # difficulty
#             # recommendation
#             # =================================================

#             "events":
#                 events,


#             # =================================================
#             # GEMINI AI
#             # =================================================

#             "ai_recommendation":
#                 ai_recommendation,


#             # =================================================
#             # MODULE STATUS
#             # =================================================

#             "module_status":
#                 module_status
#         }


#     # ========================================================
#     # EXTERNAL REQUEST ERROR
#     # ========================================================

#     except requests.exceptions.RequestException as e:

#         return {

#             "success":
#                 False,

#             "error":
#                 "External astronomy API request failed",

#             "details":
#                 str(e),

#             "type":
#                 type(e).__name__
#         }


#     # ========================================================
#     # GENERAL ERROR
#     # ========================================================

#     except Exception as e:

#         return {

#             "success":
#                 False,

#             "error":
#                 str(e),

#             "details":
#                 str(e),

#             "type":
#                 type(e).__name__
#         }






## third code 


# import requests

# from fastapi import APIRouter, Query

# from app.api.weather import get_weather
# from app.api.sun import get_sun
# from app.api.planets import get_planets
# from app.api.deep_objects import get_deep_sky
# from app.api.constellations import get_constellations
# from app.api.meteor_showers import get_meteor_showers
# from app.api.atronomical_events import get_astronomical_events

# from app.services.ai_recommendation import generate_recommendation


# router = APIRouter()


# # ============================================================
# # SAFE MODULE CALL
# # ============================================================

# def safe_call(function, **kwargs):

#     try:

#         result = function(**kwargs)

#         return {
#             "success": True,
#             "data": result,
#             "error": None,
#             "type": None
#         }

#     except Exception as e:

#         return {
#             "success": False,
#             "data": None,
#             "error": str(e),
#             "type": type(e).__name__
#         }


# # ============================================================
# # HELPERS
# # ============================================================

# def first_not_none(*values):

#     for value in values:

#         if value is not None:
#             return value

#     return None


# def get_list(data, keys):

#     if isinstance(data, list):
#         return data

#     if not isinstance(data, dict):
#         return []

#     for key in keys:

#         value = data.get(key)

#         if isinstance(value, list):
#             return value

#     return []


# # ============================================================
# # NORMALIZE ONE OBJECT
# # ============================================================

# def normalize_object(item):

#     if not isinstance(item, dict):
#         return item

#     if "visible" not in item:
#         item["visible"] = None

#     if "observability" not in item:

#         final_obs = item.get("final_observability")

#         if isinstance(final_obs, dict):

#             item["observability"] = first_not_none(
#                 final_obs.get("quality"),
#                 final_obs.get("observability")
#             )

#         else:

#             item["observability"] = None

#     if "naked_eye" not in item:
#         item["naked_eye"] = None

#     difficulty = item.get("difficulty")

#     if isinstance(difficulty, dict):

#         item["difficulty"] = difficulty

#     elif difficulty is not None:

#         item["difficulty"] = {
#             "level": str(difficulty).lower().replace(" ", "_"),
#             "label": str(difficulty)
#         }

#     else:

#         difficulty_level = item.get(
#             "difficulty_level"
#         )

#         if difficulty_level:

#             item["difficulty"] = {
#                 "level": str(difficulty_level).lower().replace(" ", "_"),
#                 "label": str(difficulty_level)
#             }

#         else:

#             item["difficulty"] = {
#                 "level": "unknown",
#                 "label": "Unknown"
#             }

#     if "recommendation" not in item:

#         difficulty_data = item.get("difficulty")

#         if isinstance(difficulty_data, dict):

#             item["recommendation"] = difficulty_data.get(
#                 "recommendation"
#             )

#         else:

#             item["recommendation"] = None

#     return item


# # ============================================================
# # NORMALIZE LIST
# # ============================================================

# def normalize_list(items):

#     if not isinstance(items, list):
#         return items

#     return [
#         normalize_object(item)
#         for item in items
#         if isinstance(item, dict)
#     ]


# # ============================================================
# # NORMALIZE MODULE
# # ============================================================

# def normalize_module_data(data, possible_keys):

#     if not isinstance(data, dict):
#         return data

#     for key in possible_keys:

#         if key in data and isinstance(
#             data[key],
#             list
#         ):

#             data[key] = normalize_list(
#                 data[key]
#             )

#             return data

#     return data


# # ============================================================
# # EVENT NORMALIZATION
# # ============================================================

# def normalize_events(events):

#     if not isinstance(events, dict):
#         return events

#     event_data = events.get("events")

#     if not isinstance(event_data, dict):
#         return events

#     event_types = [
#         "eclipses",
#         "conjunctions",
#         "oppositions",
#         "occultations"
#     ]

#     for event_type in event_types:

#         items = event_data.get(
#             event_type
#         )

#         if isinstance(items, list):

#             event_data[event_type] = normalize_list(
#                 items
#             )

#     events["events"] = event_data

#     return events


# # ============================================================
# # EXTRACT OBJECT NAME
# # ============================================================

# def get_object_name(item):

#     if not isinstance(item, dict):
#         return None

#     return first_not_none(

#         item.get("name"),

#         item.get("object_name"),

#         item.get("planet"),

#         item.get("planet_name"),

#         item.get("target"),

#         item.get("target_name"),

#         item.get("designation"),

#         item.get("id")
#     )


# # ============================================================
# # NORMALIZE PLANETS
# # ============================================================

# def normalize_planets(planets):

#     items = get_list(
#         planets,
#         [
#             "planets",
#             "objects",
#             "targets"
#         ]
#     )

#     normalized = []

#     for item in items:

#         if not isinstance(item, dict):
#             continue

#         item = normalize_object(item)

#         name = get_object_name(item)

#         if name:
#             item["name"] = name

#         item.setdefault(
#             "type",
#             "Planet"
#         )

#         normalized.append(item)

#     return normalized


# # ============================================================
# # NORMALIZE DEEP SKY
# # ============================================================

# def normalize_deep_sky(deep_sky):

#     items = get_list(
#         deep_sky,
#         [
#             "objects",
#             "deep_sky",
#             "targets"
#         ]
#     )

#     return [
#         normalize_object(item)
#         for item in items
#         if isinstance(item, dict)
#     ]


# # ============================================================
# # NORMALIZE CONSTELLATIONS
# # ============================================================

# def normalize_constellations(constellations):

#     items = get_list(
#         constellations,
#         [
#             "constellations",
#             "objects",
#             "targets"
#         ]
#     )

#     return [
#         normalize_object(item)
#         for item in items
#         if isinstance(item, dict)
#     ]


# # ============================================================
# # NORMALIZE METEOR SHOWERS
# # ============================================================

# def normalize_meteor_showers(meteor_showers):

#     items = get_list(
#         meteor_showers,
#         [
#             "showers",
#             "objects"
#         ]
#     )

#     return [
#         normalize_object(item)
#         for item in items
#         if isinstance(item, dict)
#     ]


# # ============================================================
# # VISIBILITY SUMMARY
# # ============================================================

# def count_visibility(items):

#     visible = 0
#     not_visible = 0
#     unknown = 0

#     for item in items:

#         if not isinstance(item, dict):
#             continue

#         value = item.get("visible")

#         if value is True:

#             visible += 1

#         elif value is False:

#             not_visible += 1

#         else:

#             unknown += 1

#     return {
#         "visible": visible,
#         "not_visible": not_visible,
#         "unknown": unknown,
#         "total": len(items)
#     }


# # ============================================================
# # VISIBILITY SUMMARY
# # ============================================================

# def build_visibility_summary(
#     planets,
#     deep_sky,
#     constellations,
#     meteor_showers,
#     events
# ):

#     summary = {

#         "planets": count_visibility(
#             planets
#         ),

#         "deep_sky": count_visibility(
#             deep_sky
#         ),

#         "constellations": count_visibility(
#             constellations
#         ),

#         "meteor_showers": count_visibility(
#             meteor_showers
#         ),

#         "astronomical_events": {
#             "visible": 0,
#             "not_visible": 0,
#             "unknown": 0,
#             "total": 0
#         }
#     }

#     event_items = []

#     if isinstance(events, dict):

#         event_data = events.get(
#             "events",
#             {}
#         )

#         if isinstance(event_data, dict):

#             for event_type in [
#                 "eclipses",
#                 "conjunctions",
#                 "oppositions",
#                 "occultations"
#             ]:

#                 items = event_data.get(
#                     event_type,
#                     []
#                 )

#                 if isinstance(items, list):

#                     event_items.extend(
#                         items
#                     )

#     event_summary = count_visibility(
#         event_items
#     )

#     summary["astronomical_events"] = event_summary

#     return summary


# # ============================================================
# # DIFFICULTY SUMMARY
# # ============================================================

# def build_difficulty_summary(
#     planets,
#     deep_sky,
#     constellations,
#     meteor_showers
# ):

#     summary = {
#         "easy": 0,
#         "moderate": 0,
#         "medium": 0,
#         "hard": 0,
#         "very_hard": 0,
#         "unknown": 0
#     }

#     all_items = (
#         planets
#         + deep_sky
#         + constellations
#         + meteor_showers
#     )

#     for item in all_items:

#         if not isinstance(item, dict):
#             continue

#         difficulty = item.get(
#             "difficulty"
#         )

#         if isinstance(difficulty, dict):

#             level = str(
#                 difficulty.get(
#                     "level",
#                     "unknown"
#                 )
#             ).lower()

#         else:

#             level = str(
#                 difficulty or "unknown"
#             ).lower()

#         level = (
#             level
#             .replace(" ", "_")
#             .replace("-", "_")
#         )

#         if level in summary:

#             summary[level] += 1

#         elif level == "moderate":

#             summary["moderate"] += 1

#         elif level == "medium":

#             summary["medium"] += 1

#         elif level in [
#             "veryhard",
#             "very_hard"
#         ]:

#             summary["very_hard"] += 1

#         elif "easy" in level:

#             summary["easy"] += 1

#         elif "hard" in level:

#             summary["hard"] += 1

#         else:

#             summary["unknown"] += 1

#     return summary


# # ============================================================
# # WEATHER SUMMARY
# # ============================================================

# def build_weather_summary(weather):

#     result = {

#         "cloud_cover": None,
#         "humidity": None,
#         "visibility": None,
#         "wind_speed": None,
#         "temperature": None,
#         "dew_point": None
#     }

#     if not isinstance(weather, dict):
#         return result

#     hourly = weather.get(
#         "hourly",
#         {}
#     )

#     if not isinstance(hourly, dict):
#         return result

#     def average_value(key):

#         values = hourly.get(
#             key,
#             []
#         )

#         if not isinstance(values, list):
#             return None

#         valid = []

#         for value in values:

#             if value is None:
#                 continue

#             try:
#                 valid.append(
#                     float(value)
#                 )
#             except (
#                 ValueError,
#                 TypeError
#             ):
#                 continue

#         if not valid:
#             return None

#         return round(
#             sum(valid) / len(valid),
#             1
#         )

#     result["cloud_cover"] = average_value(
#         "cloud_cover"
#     )

#     result["humidity"] = average_value(
#         "relative_humidity_2m"
#     )

#     result["visibility"] = average_value(
#         "visibility"
#     )

#     result["wind_speed"] = average_value(
#         "wind_speed_10m"
#     )

#     result["temperature"] = average_value(
#         "temperature_2m"
#     )

#     result["dew_point"] = average_value(
#         "dew_point_2m"
#     )

#     return result


# # ============================================================
# # SUN SUMMARY
# # ============================================================

# def build_sun_summary(sun):

#     result = {

#         "sunrise": None,
#         "sunset": None,
#         "astronomical_dawn": None,
#         "astronomical_dusk": None
#     }

#     if not isinstance(sun, dict):
#         return result

#     data = sun.get(
#         "results",
#         sun
#     )

#     if not isinstance(data, dict):
#         return result

#     result["sunrise"] = first_not_none(
#         data.get("sunrise"),
#         data.get("sunrise_time")
#     )

#     result["sunset"] = first_not_none(
#         data.get("sunset"),
#         data.get("sunset_time")
#     )

#     result["astronomical_dawn"] = first_not_none(
#         data.get("astronomical_twilight_begin"),
#         data.get("astronomical_dawn")
#     )

#     result["astronomical_dusk"] = first_not_none(
#         data.get("astronomical_twilight_end"),
#         data.get("astronomical_dusk")
#     )

#     return result


# # ============================================================
# # MOON SUMMARY
# # ============================================================

# def build_moon_summary(planets):

#     result = {

#         "phase": None,
#         "illumination": None,
#         "moonrise": None,
#         "moonset": None
#     }

#     items = planets

#     for item in items:

#         if not isinstance(item, dict):
#             continue

#         name = str(
#             get_object_name(item) or ""
#         ).lower()

#         if name != "moon":
#             continue

#         result["phase"] = first_not_none(
#             item.get("phase"),
#             item.get("moon_phase")
#         )

#         result["illumination"] = first_not_none(
#             item.get("illumination"),
#             item.get("moon_illumination")
#         )

#         result["moonrise"] = first_not_none(
#             item.get("rise"),
#             item.get("moonrise")
#         )

#         result["moonset"] = first_not_none(
#             item.get("set"),
#             item.get("moonset")
#         )

#         break

#     return result


# # ============================================================
# # OBSERVATION QUALITY
# # ============================================================

# def calculate_observation_quality(
#     weather,
#     visibility_summary
# ):

#     score = 5.0

#     reasons = []

#     weather_summary = build_weather_summary(
#         weather
#     )

#     cloud_cover = weather_summary.get(
#         "cloud_cover"
#     )

#     if cloud_cover is not None:

#         if cloud_cover <= 10:

#             score += 4

#             reasons.append(
#                 "Very low cloud cover."
#             )

#         elif cloud_cover <= 30:

#             score += 3

#             reasons.append(
#                 "Low cloud cover."
#             )

#         elif cloud_cover <= 60:

#             score += 1

#             reasons.append(
#                 "Some cloud cover may interfere."
#             )

#         elif cloud_cover <= 80:

#             score -= 2

#             reasons.append(
#                 "High cloud cover may interfere."
#             )

#         else:

#             score -= 4

#             reasons.append(
#                 "Heavy cloud cover is likely."
#             )

#     visible_count = 0

#     for category in visibility_summary.values():

#         if isinstance(category, dict):

#             visible_count += category.get(
#                 "visible",
#                 0
#             )

#     if visible_count >= 8:

#         score += 1

#         reasons.append(
#             "Many astronomical targets are available."
#         )

#     elif visible_count >= 4:

#         score += 0.5

#         reasons.append(
#             "Several astronomical targets are available."
#         )

#     elif visible_count == 0:

#         score -= 2

#         reasons.append(
#             "No clearly visible targets were returned."
#         )

#     score = max(
#         0,
#         min(
#             10,
#             score
#         )
#     )

#     if score >= 8.5:

#         quality = "excellent"
#         label = "Excellent"

#     elif score >= 7:

#         quality = "very_good"
#         label = "Very Good"

#     elif score >= 5:

#         quality = "good"
#         label = "Good"

#     elif score >= 3:

#         quality = "fair"
#         label = "Fair"

#     else:

#         quality = "poor"
#         label = "Poor"

#     return {

#         "score": round(
#             score,
#             1
#         ),

#         "quality": quality,

#         "label": label,

#         "reasons": reasons,

#         "cloud_cover_percent":
#             cloud_cover
#     }


# # ============================================================
# # MASTER OBSERVATION API
# # ============================================================

# @router.post(
#     "/observation/analyze"
# )
# def analyze_observation(

#     latitude: float = Query(...),

#     longitude: float = Query(...),

#     from_date: str = Query(...),

#     to_date: str = Query(...),

#     from_time: str = Query(
#         "20:00"
#     ),

#     to_time: str = Query(
#         "02:00"
#     )

# ):

#     # ========================================================
#     # 1. WEATHER
#     # ========================================================

#     weather_result = safe_call(

#         get_weather,

#         latitude=latitude,

#         longitude=longitude
#     )

#     weather = weather_result["data"]


#     # ========================================================
#     # 2. SUN
#     # ========================================================

#     sun_result = safe_call(

#         get_sun,

#         latitude=latitude,

#         longitude=longitude,

#         date=from_date
#     )

#     sun = sun_result["data"]


#     # ========================================================
#     # 3. PLANETS
#     # ========================================================

#     planets_result = safe_call(

#         get_planets,

#         latitude=latitude,

#         longitude=longitude,

#         from_date=from_date,

#         to_date=to_date,

#         from_time=from_time,

#         to_time=to_time
#     )

#     planets_raw = planets_result["data"]

#     planets = normalize_planets(
#         planets_raw
#     )


#     # ========================================================
#     # 4. DEEP SKY
#     # ========================================================

#     deep_sky_result = safe_call(

#         get_deep_sky,

#         latitude=latitude,

#         longitude=longitude,

#         from_date=from_date,

#         to_date=to_date,

#         from_time=from_time,

#         to_time=to_time
#     )

#     deep_sky_raw = deep_sky_result["data"]

#     deep_sky = normalize_deep_sky(
#         deep_sky_raw
#     )


#     # ========================================================
#     # 5. CONSTELLATIONS
#     # ========================================================

#     constellations_result = safe_call(

#         get_constellations,

#         latitude=latitude,

#         longitude=longitude,

#         from_date=from_date,

#         to_date=to_date,

#         from_time=from_time,

#         to_time=to_time
#     )

#     constellations_raw = constellations_result["data"]

#     constellations = normalize_constellations(
#         constellations_raw
#     )


#     # ========================================================
#     # 6. METEOR SHOWERS
#     # ========================================================

#     meteor_result = safe_call(

#         get_meteor_showers,

#         latitude=latitude,

#         longitude=longitude,

#         from_date=from_date,

#         to_date=to_date,

#         from_time=from_time,

#         to_time=to_time
#     )

#     meteor_raw = meteor_result["data"]

#     meteor_showers = normalize_meteor_showers(
#         meteor_raw
#     )


#     # ========================================================
#     # 7. ASTRONOMICAL EVENTS
#     # ========================================================

#     events_result = safe_call(

#         get_astronomical_events,

#         latitude=latitude,

#         longitude=longitude,

#         from_date=from_date,

#         to_date=to_date,

#         from_time=from_time,

#         to_time=to_time
#     )

#     events = normalize_events(
#         events_result["data"]
#     )


#     # ========================================================
#     # 8. WEATHER SUMMARY
#     # ========================================================

#     weather_summary = build_weather_summary(
#         weather
#     )


#     # ========================================================
#     # 9. SUN SUMMARY
#     # ========================================================

#     sun_summary = build_sun_summary(
#         sun
#     )


#     # ========================================================
#     # 10. MOON SUMMARY
#     # ========================================================

#     moon_summary = build_moon_summary(
#         planets
#     )


#     # ========================================================
#     # 11. VISIBILITY
#     # ========================================================

#     visibility_summary = build_visibility_summary(

#         planets=planets,

#         deep_sky=deep_sky,

#         constellations=constellations,

#         meteor_showers=meteor_showers,

#         events=events
#     )


#     # ========================================================
#     # 12. DIFFICULTY
#     # ========================================================

#     difficulty_summary = build_difficulty_summary(

#         planets,

#         deep_sky,

#         constellations,

#         meteor_showers
#     )


#     # ========================================================
#     # 13. OBSERVATION QUALITY
#     # ========================================================

#     observation_quality = calculate_observation_quality(

#         weather,

#         visibility_summary
#     )


#     # ========================================================
#     # 14. FRONTEND OVERVIEW
#     # ========================================================

#     total_visible = sum(

#         category.get(
#             "visible",
#             0
#         )

#         for category in visibility_summary.values()

#         if isinstance(category, dict)
#     )

#     total_not_visible = sum(

#         category.get(
#             "not_visible",
#             0
#         )

#         for category in visibility_summary.values()

#         if isinstance(category, dict)
#     )

#     total_targets = (

#         total_visible
#         +
#         total_not_visible
#     )


#     overview = {

#         "cloud_cover":
#             weather_summary["cloud_cover"],

#         "moon_illumination":
#             moon_summary["illumination"],

#         "visible_targets":
#             total_visible,

#         "overall_score":
#             observation_quality["score"]
#     }


#     # ========================================================
#     # 15. GEMINI DATA
#     # ========================================================

#     astronomy_data = {

#         "location": {

#             "latitude":
#                 latitude,

#             "longitude":
#                 longitude
#         },

#         "observation": {

#             "from_date":
#                 from_date,

#             "to_date":
#                 to_date,

#             "from_time":
#                 from_time,

#             "to_time":
#                 to_time
#         },

#         "weather":
#             weather,

#         "weather_summary":
#             weather_summary,

#         "sun":
#             sun,

#         "sun_summary":
#             sun_summary,

#         "moon":
#             moon_summary,

#         "planets":
#             planets,

#         "deep_sky":
#             deep_sky,

#         "constellations":
#             constellations,

#         "meteor_showers":
#             meteor_showers,

#         "events":
#             events,

#         "visibility_summary":
#             visibility_summary,

#         "difficulty_summary":
#             difficulty_summary,

#         "observation_quality":
#             observation_quality
#     }


#     # ========================================================
#     # 16. GEMINI
#     # ========================================================

#     ai_recommendation = None

#     gemini_success = False

#     gemini_error = None

#     try:

#         ai_recommendation = generate_recommendation(
#             astronomy_data
#         )

#         gemini_success = True

#     except Exception as e:

#         gemini_error = str(e)

#         ai_recommendation = {

#             "score": None,

#             "recommendation":
#                 "AI recommendation is temporarily unavailable.",

#             "best_time": None,

#             "best_targets": [],

#             "weather_summary": "",

#             "astronomy_summary": "",

#             "tips": []
#         }


#     # ========================================================
#     # 17. MODULE STATUS
#     # ========================================================

#     module_status = {

#         "weather":
#             weather_result["success"],

#         "sun":
#             sun_result["success"],

#         "planets":
#             planets_result["success"],

#         "deep_sky":
#             deep_sky_result["success"],

#         "constellations":
#             constellations_result["success"],

#         "meteor_showers":
#             meteor_result["success"],

#         "astronomical_events":
#             events_result["success"],

#         "gemini":
#             gemini_success
#     }


#     if gemini_error:

#         module_status[
#             "gemini_error"
#         ] = gemini_error


#     # ========================================================
#     # 18. FINAL RESPONSE
#     # ========================================================

#     return {

#         "success": True,

#         # ----------------------------------------------------
#         # OBSERVATION
#         # ----------------------------------------------------

#         "observation": {

#             "latitude":
#                 latitude,

#             "longitude":
#                 longitude,

#             "from_date":
#                 from_date,

#             "to_date":
#                 to_date,

#             "from_time":
#                 from_time,

#             "to_time":
#                 to_time
#         },

#         # ----------------------------------------------------
#         # NEW FRONTEND SUMMARY
#         # ----------------------------------------------------

#         "overview":
#             overview,

#         # ----------------------------------------------------
#         # WEATHER
#         # ----------------------------------------------------

#         "weather":
#             weather,

#         "weather_summary":
#             weather_summary,

#         # ----------------------------------------------------
#         # SUN
#         # ----------------------------------------------------

#         "sun":
#             sun,

#         "sun_summary":
#             sun_summary,

#         # ----------------------------------------------------
#         # MOON
#         # ----------------------------------------------------

#         "moon":
#             moon_summary,

#         # ----------------------------------------------------
#         # PLANETS
#         # ----------------------------------------------------

#         "planets":
#             planets,

#         # ----------------------------------------------------
#         # DEEP SKY
#         # ----------------------------------------------------

#         "deep_sky":
#             deep_sky,

#         # ----------------------------------------------------
#         # CONSTELLATIONS
#         # ----------------------------------------------------

#         "constellations":
#             constellations,

#         # ----------------------------------------------------
#         # METEOR SHOWERS
#         # ----------------------------------------------------

#         "meteor_showers":
#             meteor_showers,

#         # ----------------------------------------------------
#         # EVENTS
#         # ----------------------------------------------------

#         "events":
#             events,

#         # ----------------------------------------------------
#         # VISIBILITY
#         # ----------------------------------------------------

#         "visibility_summary":
#             visibility_summary,

#         "visibility_overview": {

#             "visible":
#                 total_visible,

#             "not_visible":
#                 total_not_visible,

#             "total":
#                 total_targets
#         },

#         # ----------------------------------------------------
#         # DIFFICULTY
#         # ----------------------------------------------------

#         "difficulty_summary":
#             difficulty_summary,

#         # ----------------------------------------------------
#         # OBSERVATION QUALITY
#         # ----------------------------------------------------

#         "observation_quality":
#             observation_quality,

#         # ----------------------------------------------------
#         # GEMINI
#         # ----------------------------------------------------

#         "ai_recommendation":
#             ai_recommendation,

#         # ----------------------------------------------------
#         # MODULE STATUS
#         # ----------------------------------------------------

#         "module_status":
#             module_status
#     }

# Forth code

# from fastapi import APIRouter, Query

# from app.api.weather import get_weather
# from app.api.sun import get_sun
# from app.api.planets import get_planets
# from app.api.deep_objects import get_deep_sky
# from app.api.constellations import get_constellations
# from app.api.meteor_showers import get_meteor_showers
# from app.api.atronomical_events import get_astronomical_events

# from app.services.ai_recommendation import generate_recommendation


# router = APIRouter()


# # ============================================================
# # SAFE MODULE CALL
# # ============================================================

# def safe_call(function, **kwargs):
#     try:
#         result = function(**kwargs)

#         return {
#             "success": True,
#             "data": result,
#             "error": None,
#             "type": None
#         }

#     except Exception as e:
#         return {
#             "success": False,
#             "data": None,
#             "error": str(e),
#             "type": type(e).__name__
#         }


# # ============================================================
# # BASIC HELPERS
# # ============================================================

# def first_not_none(*values):
#     for value in values:
#         if value is not None:
#             return value

#     return None


# def get_list(data, keys):
#     if isinstance(data, list):
#         return data

#     if not isinstance(data, dict):
#         return []

#     for key in keys:
#         value = data.get(key)

#         if isinstance(value, list):
#             return value

#     return []


# def clean_name(value):
#     if value is None:
#         return None

#     if isinstance(value, str):
#         value = value.strip()

#         if not value:
#             return None

#         return value

#     return str(value)


# # ============================================================
# # OBJECT NAME
# # ============================================================

# def get_object_name(item):
#     if not isinstance(item, dict):
#         return None

#     # Normal astronomy object names
#     name = first_not_none(
#         item.get("name"),
#         item.get("object_name"),
#         item.get("planet"),
#         item.get("planet_name"),
#         item.get("target"),
#         item.get("target_name"),
#         item.get("designation"),
#         item.get("object"),
#         item.get("objectName"),
#         item.get("shower_name"),
#         item.get("meteor_shower"),
#         item.get("meteor_shower_name"),
#         item.get("shower"),
#         item.get("code")
#     )

#     return clean_name(name)


# # ============================================================
# # NORMALIZE ONE OBJECT
# # ============================================================

# def normalize_object(item):

#     if not isinstance(item, dict):
#         return item

#     item = dict(item)

#     # --------------------------------------------------------
#     # NAME
#     # --------------------------------------------------------

#     name = get_object_name(item)

#     if name:
#         item["name"] = name

#     # --------------------------------------------------------
#     # VISIBILITY
#     # --------------------------------------------------------

#     if "visible" not in item:
#         item["visible"] = None

#     # --------------------------------------------------------
#     # OBSERVABILITY
#     # --------------------------------------------------------

#     if "observability" not in item:

#         final_obs = item.get("final_observability")

#         if isinstance(final_obs, dict):

#             item["observability"] = first_not_none(
#                 final_obs.get("quality"),
#                 final_obs.get("observability"),
#                 final_obs.get("status")
#             )

#         else:
#             item["observability"] = first_not_none(
#                 item.get("visibility_status"),
#                 item.get("status")
#             )

#     # --------------------------------------------------------
#     # NAKED EYE
#     # --------------------------------------------------------

#     if "naked_eye" not in item:

#         item["naked_eye"] = first_not_none(
#             item.get("nakedEye"),
#             item.get("naked_eye_visible")
#         )

#     # --------------------------------------------------------
#     # DIFFICULTY
#     # --------------------------------------------------------

#     difficulty = item.get("difficulty")

#     if isinstance(difficulty, dict):

#         difficulty_data = dict(difficulty)

#         level = first_not_none(
#             difficulty_data.get("level"),
#             difficulty_data.get("difficulty"),
#             difficulty_data.get("label")
#         )

#         if level:
#             difficulty_data["level"] = (
#                 str(level)
#                 .lower()
#                 .replace(" ", "_")
#                 .replace("-", "_")
#             )

#         item["difficulty"] = difficulty_data

#     elif difficulty is not None:

#         label = str(difficulty)

#         item["difficulty"] = {
#             "level": (
#                 label
#                 .lower()
#                 .replace(" ", "_")
#                 .replace("-", "_")
#             ),
#             "label": label
#         }

#     else:

#         difficulty_level = first_not_none(
#             item.get("difficulty_level"),
#             item.get("difficultyLevel")
#         )

#         if difficulty_level:

#             label = str(difficulty_level)

#             item["difficulty"] = {
#                 "level": (
#                     label
#                     .lower()
#                     .replace(" ", "_")
#                     .replace("-", "_")
#                 ),
#                 "label": label
#             }

#         else:

#             item["difficulty"] = {
#                 "level": "unknown",
#                 "label": "Unknown"
#             }

#     # --------------------------------------------------------
#     # RECOMMENDATION
#     # --------------------------------------------------------

#     if "recommendation" not in item:

#         difficulty_data = item.get("difficulty")

#         recommendation = None

#         if isinstance(difficulty_data, dict):
#             recommendation = difficulty_data.get(
#                 "recommendation"
#             )

#         item["recommendation"] = recommendation

#     return item


# # ============================================================
# # NORMALIZE LIST
# # ============================================================

# def normalize_list(items):

#     if not isinstance(items, list):
#         return []

#     return [
#         normalize_object(item)
#         for item in items
#         if isinstance(item, dict)
#     ]


# # ============================================================
# # PLANETS
# # ============================================================

# def normalize_planets(planets):

#     items = get_list(
#         planets,
#         [
#             "planets",
#             "objects",
#             "targets"
#         ]
#     )

#     normalized = []

#     for item in items:

#         item = normalize_object(item)

#         if not item.get("name"):
#             continue

#         item.setdefault(
#             "type",
#             "Planet"
#         )

#         normalized.append(item)

#     return normalized


# # ============================================================
# # DEEP SKY
# # ============================================================

# def normalize_deep_sky(deep_sky):

#     items = get_list(
#         deep_sky,
#         [
#             "objects",
#             "deep_sky",
#             "targets"
#         ]
#     )

#     normalized = []

#     for item in items:

#         item = normalize_object(item)

#         if not item.get("name"):
#             continue

#         normalized.append(item)

#     return normalized


# # ============================================================
# # CONSTELLATIONS
# # ============================================================

# def normalize_constellations(constellations):

#     items = get_list(
#         constellations,
#         [
#             "constellations",
#             "objects",
#             "targets"
#         ]
#     )

#     normalized = []

#     for item in items:

#         item = normalize_object(item)

#         if not item.get("name"):
#             continue

#         item.setdefault(
#             "type",
#             "Constellation"
#         )

#         normalized.append(item)

#     return normalized


# # ============================================================
# # METEOR SHOWERS
# # ============================================================

# def normalize_meteor_showers(meteor_showers):

#     items = get_list(
#         meteor_showers,
#         [
#             "showers",
#             "objects",
#             "meteor_showers",
#             "targets"
#         ]
#     )

#     normalized = []

#     for item in items:

#         item = normalize_object(item)

#         # ----------------------------------------------------
#         # MeteorShowerCal can use different name fields
#         # ----------------------------------------------------

#         if not item.get("name"):

#             name = first_not_none(
#                 item.get("active", {}).get("name")
#                 if isinstance(item.get("active"), dict)
#                 else None,

#                 item.get("details", {}).get("name")
#                 if isinstance(item.get("details"), dict)
#                 else None,

#                 item.get("full_name"),

#                 item.get("display_name"),

#                 item.get("code")
#             )

#             if name:
#                 item["name"] = clean_name(name)

#         if not item.get("name"):
#             continue

#         item.setdefault(
#             "type",
#             "Meteor Shower"
#         )

#         normalized.append(item)

#     return normalized


# # ============================================================
# # EVENTS
# # ============================================================

# def normalize_events(events):

#     if not isinstance(events, dict):
#         return events

#     event_data = events.get("events")

#     if not isinstance(event_data, dict):
#         return events

#     event_types = [
#         "eclipses",
#         "conjunctions",
#         "oppositions",
#         "occultations"
#     ]

#     for event_type in event_types:

#         items = event_data.get(
#             event_type
#         )

#         if isinstance(items, list):

#             event_data[event_type] = normalize_list(
#                 items
#             )

#     events["events"] = event_data

#     return events


# # ============================================================
# # SELECTED WEATHER VALUES
# # ============================================================

# def build_weather_summary(
#     weather,
#     from_date,
#     to_date,
#     from_time,
#     to_time
# ):

#     result = {
#         "cloud_cover": None,
#         "humidity": None,
#         "visibility": None,
#         "wind_speed": None,
#         "temperature": None,
#         "dew_point": None,

#         "cloud_cover_min": None,
#         "cloud_cover_max": None,

#         "humidity_min": None,
#         "humidity_max": None,

#         "selected_points": 0
#     }

#     if not isinstance(weather, dict):
#         return result

#     hourly = weather.get("hourly")

#     if not isinstance(hourly, dict):
#         return result

#     times = hourly.get("time", [])

#     if not isinstance(times, list):
#         return result

#     # --------------------------------------------------------
#     # Parse selected start/end
#     # --------------------------------------------------------

#     try:

#         from datetime import datetime, timedelta

#         start = datetime.fromisoformat(
#             f"{from_date}T{from_time}"
#         )

#         end = datetime.fromisoformat(
#             f"{to_date}T{to_time}"
#         )

#         # Overnight session
#         if end <= start:
#             end += timedelta(days=1)

#     except Exception:
#         return result

#     selected_indexes = []

#     for index, time_value in enumerate(times):

#         if not isinstance(time_value, str):
#             continue

#         try:

#             weather_time = datetime.fromisoformat(
#                 time_value.replace("Z", "+00:00")
#             )

#             # Open-Meteo timezone=auto usually returns
#             # local time without offset.
#             if weather_time.tzinfo is not None:
#                 weather_time = weather_time.replace(
#                     tzinfo=None
#                 )

#             # Forecast values are local-time based here.
#             # Handle overnight second date.
#             if weather_time < start:
#                 continue

#             if weather_time > end:
#                 continue

#             selected_indexes.append(index)

#         except Exception:
#             continue

#     # --------------------------------------------------------
#     # If exact selection fails, use available values
#     # --------------------------------------------------------

#     if not selected_indexes:

#         selected_indexes = list(
#             range(
#                 min(
#                     len(times),
#                     len(
#                         hourly.get(
#                             "cloud_cover",
#                             []
#                         )
#                     )
#                 )
#             )
#         )

#     result["selected_points"] = len(
#         selected_indexes
#     )

#     # --------------------------------------------------------
#     # Average selected values
#     # --------------------------------------------------------

#     def selected_values(key):

#         values = hourly.get(
#             key,
#             []
#         )

#         if not isinstance(values, list):
#             return []

#         selected = []

#         for index in selected_indexes:

#             if index >= len(values):
#                 continue

#             value = values[index]

#             if value is None:
#                 continue

#             try:
#                 selected.append(
#                     float(value)
#                 )
#             except (
#                 ValueError,
#                 TypeError
#             ):
#                 continue

#         return selected

#     def average(key):

#         values = selected_values(key)

#         if not values:
#             return None

#         return round(
#             sum(values) / len(values),
#             1
#         )

#     def minimum(key):

#         values = selected_values(key)

#         if not values:
#             return None

#         return round(
#             min(values),
#             1
#         )

#     def maximum(key):

#         values = selected_values(key)

#         if not values:
#             return None

#         return round(
#             max(values),
#             1
#         )

#     # --------------------------------------------------------
#     # Values
#     # --------------------------------------------------------

#     result["cloud_cover"] = average(
#         "cloud_cover"
#     )

#     result["humidity"] = average(
#         "relative_humidity_2m"
#     )

#     result["visibility"] = average(
#         "visibility"
#     )

#     result["wind_speed"] = average(
#         "wind_speed_10m"
#     )

#     result["temperature"] = average(
#         "temperature_2m"
#     )

#     result["dew_point"] = average(
#         "dew_point_2m"
#     )

#     result["cloud_cover_min"] = minimum(
#         "cloud_cover"
#     )

#     result["cloud_cover_max"] = maximum(
#         "cloud_cover"
#     )

#     result["humidity_min"] = minimum(
#         "relative_humidity_2m"
#     )

#     result["humidity_max"] = maximum(
#         "relative_humidity_2m"
#     )

#     return result


# # ============================================================
# # SUN SUMMARY
# # ============================================================

# def build_sun_summary(sun):

#     result = {
#         "sunrise": None,
#         "sunset": None,
#         "astronomical_dawn": None,
#         "astronomical_dusk": None
#     }

#     if not isinstance(sun, dict):
#         return result

#     data = sun.get(
#         "results",
#         sun
#     )

#     if not isinstance(data, dict):
#         return result

#     result["sunrise"] = first_not_none(
#         data.get("sunrise"),
#         data.get("sunrise_time")
#     )

#     result["sunset"] = first_not_none(
#         data.get("sunset"),
#         data.get("sunset_time")
#     )

#     result["astronomical_dawn"] = first_not_none(
#         data.get(
#             "astronomical_twilight_begin"
#         ),
#         data.get(
#             "astronomical_dawn"
#         )
#     )

#     result["astronomical_dusk"] = first_not_none(
#         data.get(
#             "astronomical_twilight_end"
#         ),
#         data.get(
#             "astronomical_dusk"
#         )
#     )

#     return result


# # ============================================================
# # MOON SUMMARY
# # ============================================================

# def build_moon_summary(planets):

#     result = {
#         "phase": None,
#         "illumination": None,
#         "moonrise": None,
#         "moonset": None,
#         "available": False
#     }

#     if not isinstance(planets, list):
#         return result

#     for item in planets:

#         if not isinstance(item, dict):
#             continue

#         name = str(
#             get_object_name(item) or ""
#         ).lower().strip()

#         if name != "moon":
#             continue

#         result["available"] = True

#         result["phase"] = first_not_none(
#             item.get("phase"),
#             item.get("moon_phase")
#         )

#         result["illumination"] = first_not_none(
#             item.get("illumination"),
#             item.get("moon_illumination"),
#             item.get("illumination_percent")
#         )

#         result["moonrise"] = first_not_none(
#             item.get("rise"),
#             item.get("moonrise"),
#             item.get("rise_time")
#         )

#         result["moonset"] = first_not_none(
#             item.get("set"),
#             item.get("moonset"),
#             item.get("set_time")
#         )

#         break

#     return result


# # ============================================================
# # VISIBILITY
# # ============================================================

# def count_visibility(items):

#     visible = 0
#     not_visible = 0
#     unknown = 0

#     if not isinstance(items, list):
#         items = []

#     for item in items:

#         if not isinstance(item, dict):
#             continue

#         value = item.get("visible")

#         if value is True:
#             visible += 1

#         elif value is False:
#             not_visible += 1

#         else:
#             unknown += 1

#     return {
#         "visible": visible,
#         "not_visible": not_visible,
#         "unknown": unknown,
#         "total": len(items)
#     }


# def build_visibility_summary(
#     planets,
#     deep_sky,
#     constellations,
#     meteor_showers,
#     events
# ):

#     summary = {

#         "planets": count_visibility(
#             planets
#         ),

#         "deep_sky": count_visibility(
#             deep_sky
#         ),

#         "constellations": count_visibility(
#             constellations
#         ),

#         "meteor_showers": count_visibility(
#             meteor_showers
#         ),

#         "astronomical_events": {
#             "visible": 0,
#             "not_visible": 0,
#             "unknown": 0,
#             "total": 0
#         }
#     }

#     event_items = []

#     if isinstance(events, dict):

#         event_data = events.get(
#             "events",
#             {}
#         )

#         if isinstance(event_data, dict):

#             for event_type in [
#                 "eclipses",
#                 "conjunctions",
#                 "oppositions",
#                 "occultations"
#             ]:

#                 items = event_data.get(
#                     event_type,
#                     []
#                 )

#                 if isinstance(items, list):

#                     event_items.extend(
#                         items
#                     )

#     summary[
#         "astronomical_events"
#     ] = count_visibility(
#         event_items
#     )

#     return summary


# # ============================================================
# # DIFFICULTY
# # ============================================================

# def build_difficulty_summary(
#     planets,
#     deep_sky,
#     constellations,
#     meteor_showers
# ):

#     summary = {
#         "easy": 0,
#         "moderate": 0,
#         "medium": 0,
#         "hard": 0,
#         "very_hard": 0,
#         "unknown": 0
#     }

#     all_items = (
#         planets
#         + deep_sky
#         + constellations
#         + meteor_showers
#     )

#     for item in all_items:

#         if not isinstance(item, dict):
#             continue

#         difficulty = item.get(
#             "difficulty"
#         )

#         if isinstance(
#             difficulty,
#             dict
#         ):

#             level = str(
#                 difficulty.get(
#                     "level",
#                     "unknown"
#                 )
#             ).lower()

#         else:

#             level = str(
#                 difficulty or "unknown"
#             ).lower()

#         level = (
#             level
#             .replace(" ", "_")
#             .replace("-", "_")
#         )

#         if level == "veryhard":
#             level = "very_hard"

#         if level == "moderate":
#             summary["moderate"] += 1

#         elif level == "medium":
#             summary["medium"] += 1

#         elif level == "very_hard":
#             summary["very_hard"] += 1

#         elif level == "hard":
#             summary["hard"] += 1

#         elif level == "easy":
#             summary["easy"] += 1

#         elif "easy" in level:
#             summary["easy"] += 1

#         elif "very_hard" in level:
#             summary["very_hard"] += 1

#         elif "hard" in level:
#             summary["hard"] += 1

#         else:
#             summary["unknown"] += 1

#     return summary


# # ============================================================
# # OBSERVATION QUALITY
# # ============================================================

# def calculate_observation_quality(
#     weather_summary,
#     visibility_summary
# ):

#     score = 5.0

#     reasons = []

#     cloud_cover = weather_summary.get(
#         "cloud_cover"
#     )

#     if cloud_cover is not None:

#         if cloud_cover <= 10:

#             score += 4

#             reasons.append(
#                 "Very low cloud cover."
#             )

#         elif cloud_cover <= 30:

#             score += 3

#             reasons.append(
#                 "Low cloud cover."
#             )

#         elif cloud_cover <= 60:

#             score += 1

#             reasons.append(
#                 "Some cloud cover may interfere."
#             )

#         elif cloud_cover <= 80:

#             score -= 2

#             reasons.append(
#                 "High cloud cover may interfere."
#             )

#         else:

#             score -= 4

#             reasons.append(
#                 "Heavy cloud cover is likely."
#             )

#     visible_count = 0

#     for category in visibility_summary.values():

#         if isinstance(category, dict):

#             visible_count += category.get(
#                 "visible",
#                 0
#             )

#     if visible_count >= 8:

#         score += 1

#         reasons.append(
#             "Many astronomical targets are available."
#         )

#     elif visible_count >= 4:

#         score += 0.5

#         reasons.append(
#             "Several astronomical targets are available."
#         )

#     elif visible_count == 0:

#         score -= 2

#         reasons.append(
#             "No clearly visible targets were returned."
#         )

#     score = max(
#         0,
#         min(
#             10,
#             score
#         )
#     )

#     if score >= 8.5:

#         quality = "excellent"
#         label = "Excellent"

#     elif score >= 7:

#         quality = "very_good"
#         label = "Very Good"

#     elif score >= 5:

#         quality = "good"
#         label = "Good"

#     elif score >= 3:

#         quality = "fair"
#         label = "Fair"

#     else:

#         quality = "poor"
#         label = "Poor"

#     return {

#         "score": round(
#             score,
#             1
#         ),

#         "quality": quality,

#         "label": label,

#         "reasons": reasons,

#         "cloud_cover_percent":
#             cloud_cover
#     }


# # ============================================================
# # MASTER OBSERVATION API
# # ============================================================

# @router.post(
#     "/observation/analyze"
# )
# def analyze_observation(

#     latitude: float = Query(...),

#     longitude: float = Query(...),

#     from_date: str = Query(...),

#     to_date: str = Query(...),

#     from_time: str = Query(
#         "20:00"
#     ),

#     to_time: str = Query(
#         "02:00"
#     )

# ):

#     # ========================================================
#     # WEATHER
#     # ========================================================

#     weather_result = safe_call(
#         get_weather,
#         latitude=latitude,
#         longitude=longitude
#     )

#     weather = weather_result["data"]


#     # ========================================================
#     # SUN
#     # ========================================================

#     sun_result = safe_call(
#         get_sun,
#         latitude=latitude,
#         longitude=longitude,
#         date=from_date
#     )

#     sun = sun_result["data"]


#     # ========================================================
#     # PLANETS
#     # ========================================================

#     planets_result = safe_call(

#         get_planets,

#         latitude=latitude,
#         longitude=longitude,

#         from_date=from_date,
#         to_date=to_date,

#         from_time=from_time,
#         to_time=to_time
#     )

#     planets = normalize_planets(
#         planets_result["data"]
#     )


#     # ========================================================
#     # DEEP SKY
#     # ========================================================

#     deep_sky_result = safe_call(

#         get_deep_sky,

#         latitude=latitude,
#         longitude=longitude,

#         from_date=from_date,
#         to_date=to_date,

#         from_time=from_time,
#         to_time=to_time
#     )

#     deep_sky = normalize_deep_sky(
#         deep_sky_result["data"]
#     )


#     # ========================================================
#     # CONSTELLATIONS
#     # ========================================================

#     constellations_result = safe_call(

#         get_constellations,

#         latitude=latitude,
#         longitude=longitude,

#         from_date=from_date,
#         to_date=to_date,

#         from_time=from_time,
#         to_time=to_time
#     )

#     constellations = normalize_constellations(
#         constellations_result["data"]
#     )


#     # ========================================================
#     # METEOR SHOWERS
#     # ========================================================

#     meteor_result = safe_call(

#         get_meteor_showers,

#         latitude=latitude,
#         longitude=longitude,

#         from_date=from_date,
#         to_date=to_date,

#         from_time=from_time,
#         to_time=to_time
#     )

#     meteor_showers = normalize_meteor_showers(
#         meteor_result["data"]
#     )


#     # ========================================================
#     # ASTRONOMICAL EVENTS
#     # ========================================================

#     events_result = safe_call(

#         get_astronomical_events,

#         latitude=latitude,
#         longitude=longitude,

#         from_date=from_date,
#         to_date=to_date,

#         from_time=from_time,
#         to_time=to_time
#     )

#     events = normalize_events(
#         events_result["data"]
#     )


#     # ========================================================
#     # WEATHER SUMMARY
#     # ========================================================

#     weather_summary = build_weather_summary(

#         weather,

#         from_date,
#         to_date,

#         from_time,
#         to_time
#     )


#     # ========================================================
#     # SUN
#     # ========================================================

#     sun_summary = build_sun_summary(
#         sun
#     )


#     # ========================================================
#     # MOON
#     # ========================================================

#     moon_summary = build_moon_summary(
#         planets
#     )


#     # ========================================================
#     # VISIBILITY
#     # ========================================================

#     visibility_summary = build_visibility_summary(

#         planets=planets,

#         deep_sky=deep_sky,

#         constellations=constellations,

#         meteor_showers=meteor_showers,

#         events=events
#     )


#     # ========================================================
#     # DIFFICULTY
#     # ========================================================

#     difficulty_summary = build_difficulty_summary(

#         planets,

#         deep_sky,

#         constellations,

#         meteor_showers
#     )


#     # ========================================================
#     # QUALITY
#     # ========================================================

#     observation_quality = calculate_observation_quality(

#         weather_summary,

#         visibility_summary
#     )


#     # ========================================================
#     # TOTAL VISIBILITY
#     # ========================================================

#     total_visible = sum(

#         category.get(
#             "visible",
#             0
#         )

#         for category in visibility_summary.values()

#         if isinstance(category, dict)
#     )


#     total_not_visible = sum(

#         category.get(
#             "not_visible",
#             0
#         )

#         for category in visibility_summary.values()

#         if isinstance(category, dict)
#     )


#     total_unknown = sum(

#         category.get(
#             "unknown",
#             0
#         )

#         for category in visibility_summary.values()

#         if isinstance(category, dict)
#     )


#     total_targets = (

#         total_visible
#         +
#         total_not_visible
#         +
#         total_unknown
#     )


#     # ========================================================
#     # OVERVIEW
#     # ========================================================

#     overview = {

#         "cloud_cover":
#             weather_summary.get(
#                 "cloud_cover"
#             ),

#         "moon_illumination":
#             moon_summary.get(
#                 "illumination"
#             ),

#         "visible_targets":
#             total_visible,

#         "overall_score":
#             observation_quality.get(
#                 "score"
#             )
#     }


#     # ========================================================
#     # GEMINI DATA
#     # ========================================================

#     astronomy_data = {

#         "location": {

#             "latitude":
#                 latitude,

#             "longitude":
#                 longitude
#         },

#         "observation": {

#             "from_date":
#                 from_date,

#             "to_date":
#                 to_date,

#             "from_time":
#                 from_time,

#             "to_time":
#                 to_time
#         },

#         "weather_summary":
#             weather_summary,

#         "sun_summary":
#             sun_summary,

#         "moon":
#             moon_summary,

#         "planets":
#             planets,

#         "deep_sky":
#             deep_sky,

#         "constellations":
#             constellations,

#         "meteor_showers":
#             meteor_showers,

#         "events":
#             events,

#         "visibility_summary":
#             visibility_summary,

#         "difficulty_summary":
#             difficulty_summary,

#         "observation_quality":
#             observation_quality
#     }


#     # ========================================================
#     # GEMINI
#     # ========================================================

#     ai_recommendation = None

#     gemini_success = False

#     gemini_error = None

#     try:

#         ai_recommendation = generate_recommendation(
#             astronomy_data
#         )

#         gemini_success = True

#     except Exception as e:

#         gemini_error = str(e)

#         ai_recommendation = {

#             "score": None,

#             "recommendation":
#                 "AI recommendation is temporarily unavailable.",

#             "best_time": None,

#             "best_targets": [],

#             "weather_summary": "",

#             "astronomy_summary": "",

#             "tips": []
#         }


#     # ========================================================
#     # MODULE STATUS
#     # ========================================================

#     module_status = {

#         "weather":
#             weather_result["success"],

#         "sun":
#             sun_result["success"],

#         "planets":
#             planets_result["success"],

#         "deep_sky":
#             deep_sky_result["success"],

#         "constellations":
#             constellations_result["success"],

#         "meteor_showers":
#             meteor_result["success"],

#         "astronomical_events":
#             events_result["success"],

#         "gemini":
#             gemini_success
#     }


#     if gemini_error:

#         module_status[
#             "gemini_error"
#         ] = gemini_error


#     # ========================================================
#     # FINAL RESPONSE
#     # ========================================================

#     return {

#         "success": True,

#         # ----------------------------------------------------
#         # OBSERVATION
#         # ----------------------------------------------------

#         "observation": {

#             "latitude":
#                 latitude,

#             "longitude":
#                 longitude,

#             "from_date":
#                 from_date,

#             "to_date":
#                 to_date,

#             "from_time":
#                 from_time,

#             "to_time":
#                 to_time
#         },

#         # ----------------------------------------------------
#         # OVERVIEW
#         # ----------------------------------------------------

#         "overview":
#             overview,

#         # ----------------------------------------------------
#         # WEATHER
#         # ----------------------------------------------------

#         "weather":
#             weather,

#         "weather_summary":
#             weather_summary,

#         # ----------------------------------------------------
#         # SUN
#         # ----------------------------------------------------

#         "sun":
#             sun,

#         "sun_summary":
#             sun_summary,

#         # ----------------------------------------------------
#         # MOON
#         # ----------------------------------------------------

#         "moon":
#             moon_summary,

#         # ----------------------------------------------------
#         # PLANETS
#         # ----------------------------------------------------

#         "planets":
#             planets,

#         # ----------------------------------------------------
#         # DEEP SKY
#         # ----------------------------------------------------

#         "deep_sky":
#             deep_sky,

#         # ----------------------------------------------------
#         # CONSTELLATIONS
#         # ----------------------------------------------------

#         "constellations":
#             constellations,

#         # ----------------------------------------------------
#         # METEOR SHOWERS
#         # ----------------------------------------------------

#         "meteor_showers":
#             meteor_showers,

#         # ----------------------------------------------------
#         # EVENTS
#         # ----------------------------------------------------

#         "events":
#             events,

#         # ----------------------------------------------------
#         # VISIBILITY
#         # ----------------------------------------------------

#         "visibility_summary":
#             visibility_summary,

#         "visibility_overview": {

#             "visible":
#                 total_visible,

#             "not_visible":
#                 total_not_visible,

#             "unknown":
#                 total_unknown,

#             "total":
#                 total_targets
#         },

#         # ----------------------------------------------------
#         # DIFFICULTY
#         # ----------------------------------------------------

#         "difficulty_summary":
#             difficulty_summary,

#         # ----------------------------------------------------
#         # QUALITY
#         # ----------------------------------------------------

#         "observation_quality":
#             observation_quality,

#         # ----------------------------------------------------
#         # GEMINI
#         # ----------------------------------------------------

#         "ai_recommendation":
#             ai_recommendation,

#         # ----------------------------------------------------
#         # STATUS
#         # ----------------------------------------------------

#         "module_status":
#             module_status
#     }

# import math
# from datetime import datetime, timedelta

# from fastapi import APIRouter, Query

# from app.api.weather import get_weather
# from app.api.sun import get_sun
# from app.api.planets import get_planets
# from app.api.deep_objects import get_deep_sky
# from app.api.constellations import get_constellations
# from app.api.meteor_showers import get_meteor_showers
# from app.api.atronomical_events import get_astronomical_events

# # 7Timer astronomical weather
# try:
#     from app.api.astro_weather import get_astro_weather
# except Exception:
#     get_astro_weather = None

# from app.services.ai_recommendation import generate_recommendation


# router = APIRouter()


# # ============================================================
# # BASIC HELPERS
# # ============================================================

# def safe_call(function, *args, **kwargs):
#     """
#     Safely execute an API/module function.

#     A failed module should not stop the complete observation analysis.
#     """
#     try:
#         return function(*args, **kwargs)
#     except Exception as e:
#         return {
#             "success": False,
#             "error": str(e),
#             "type": type(e).__name__,
#         }


# def first_not_none(*values):
#     for value in values:
#         if value is not None:
#             return value

#     return None


# def get_list(data, keys=None):
#     """
#     Extract a list from different possible API response structures.
#     """
#     if data is None:
#         return []

#     if isinstance(data, list):
#         return data

#     if not isinstance(data, dict):
#         return []

#     if keys:
#         for key in keys:
#             value = data.get(key)

#             if isinstance(value, list):
#                 return value

#     for key in [
#         "objects",
#         "targets",
#         "items",
#         "results",
#         "showers",
#         "events",
#         "data",
#     ]:
#         value = data.get(key)

#         if isinstance(value, list):
#             return value

#     return []


# def normalize_object(item):
#     """
#     Convert arbitrary astronomy object data into a safe dictionary.
#     """
#     if isinstance(item, dict):
#         return item

#     return {
#         "name": str(item)
#     }


# def normalize_list(items):
#     return [
#         normalize_object(item)
#         for item in items
#         if item is not None
#     ]


# # ============================================================
# # OBJECT NAME
# # ============================================================

# def get_object_name(item):
#     """
#     Safely extract object name.

#     Important:
#     MeteorShowerCal can return:

#         "name": {
#             "name": "Southern Taurids",
#             "code": "STA"
#         }

#     We must NOT display the entire dictionary.
#     """

#     if not isinstance(item, dict):
#         return str(item)

#     name = item.get("name")

#     # Normal string
#     if isinstance(name, str) and name.strip():
#         return name.strip()

#     # Nested dictionary
#     if isinstance(name, dict):
#         nested_name = name.get("name")

#         if isinstance(nested_name, str) and nested_name.strip():
#             return nested_name.strip()

#         nested_code = name.get("code")

#         if isinstance(nested_code, str) and nested_code.strip():
#             return nested_code.strip()

#     # Other common fields
#     for key in [
#         "object_name",
#         "target_name",
#         "display_name",
#         "title",
#         "label",
#         "code",
#         "id",
#     ]:
#         value = item.get(key)

#         if isinstance(value, str) and value.strip():
#             return value.strip()

#     return "Unknown object"


# # ============================================================
# # NORMALIZE MODULE DATA
# # ============================================================

# def normalize_module_data(data, object_keys=None):
#     """
#     Normalizes an individual module response.
#     """

#     if data is None:
#         return {
#             "success": False,
#             "objects": [],
#         }

#     if isinstance(data, list):
#         return {
#             "success": True,
#             "objects": normalize_list(data),
#         }

#     if not isinstance(data, dict):
#         return {
#             "success": True,
#             "objects": [],
#             "data": data,
#         }

#     objects = get_list(
#         data,
#         object_keys or [
#             "objects",
#             "targets",
#             "items",
#             "results",
#         ],
#     )

#     result = dict(data)

#     result["objects"] = normalize_list(objects)

#     return result


# # ============================================================
# # EVENT NORMALIZATION
# # ============================================================

# def normalize_events(data):
#     if not data:
#         return {
#             "eclipses": [],
#             "conjunctions": [],
#             "oppositions": [],
#             "occultations": [],
#         }

#     if not isinstance(data, dict):
#         return {
#             "eclipses": [],
#             "conjunctions": [],
#             "oppositions": [],
#             "occultations": [],
#         }

#     events = data.get("events")

#     if isinstance(events, dict):
#         return {
#             "eclipses": events.get("eclipses", []) or [],
#             "conjunctions": events.get("conjunctions", []) or [],
#             "oppositions": events.get("oppositions", []) or [],
#             "occultations": events.get("occultations", []) or [],
#         }

#     return {
#         "eclipses": data.get("eclipses", []) or [],
#         "conjunctions": data.get("conjunctions", []) or [],
#         "oppositions": data.get("oppositions", []) or [],
#         "occultations": data.get("occultations", []) or [],
#     }


# # ============================================================
# # PLANETS
# # ============================================================

# def normalize_planets(data):
#     objects = get_list(
#         data,
#         [
#             "objects",
#             "planets",
#         ],
#     )

#     normalized = []

#     for item in objects:
#         item = normalize_object(item)

#         name = get_object_name(item)

#         normalized.append(
#             {
#                 **item,
#                 "name": name,
#             }
#         )

#     return normalized


# # ============================================================
# # DEEP SKY
# # ============================================================

# def normalize_deep_sky(data):
#     objects = get_list(
#         data,
#         [
#             "objects",
#             "targets",
#         ],
#     )

#     normalized = []

#     for item in objects:
#         item = normalize_object(item)

#         normalized.append(
#             {
#                 **item,
#                 "name": get_object_name(item),
#             }
#         )

#     return normalized


# # ============================================================
# # CONSTELLATIONS
# # ============================================================

# def normalize_constellations(data):
#     objects = get_list(
#         data,
#         [
#             "objects",
#             "targets",
#         ],
#     )

#     normalized = []

#     for item in objects:
#         item = normalize_object(item)

#         normalized.append(
#             {
#                 **item,
#                 "name": get_object_name(item),
#             }
#         )

#     return normalized


# # ============================================================
# # METEOR SHOWERS
# # ============================================================

# def normalize_meteor_showers(data):
#     objects = get_list(
#         data,
#         [
#             "showers",
#             "objects",
#             "targets",
#         ],
#     )

#     normalized = []

#     for item in objects:
#         item = normalize_object(item)

#         shower_name = get_object_name(item)

#         normalized.append(
#             {
#                 **item,
#                 "name": shower_name,
#             }
#         )

#     return normalized


# # ============================================================
# # DATE / TIME HELPERS
# # ============================================================

# def parse_local_datetime(date_string, time_string):
#     """
#     Create a local-naive datetime.

#     The astronomy modules already handle timezone conversion where
#     required. The master uses this only for selecting weather data.
#     """

#     return datetime.strptime(
#         f"{date_string} {time_string}",
#         "%Y-%m-%d %H:%M",
#     )


# def build_observation_range(
#     from_date,
#     to_date,
#     from_time,
#     to_time,
# ):
#     """
#     Build the actual selected observation range.

#     Example:

#     2026-09-12 20:00
#     →
#     2026-09-13 02:00

#     If to_date is the same date and end time is earlier than
#     start time, automatically treat the end as next day.
#     """

#     start = parse_local_datetime(
#         from_date,
#         from_time,
#     )

#     end = parse_local_datetime(
#         to_date,
#         to_time,
#     )

#     # Overnight session
#     if end <= start:
#         end += timedelta(days=1)

#     return start, end


# # ============================================================
# # WEATHER FILTERING
# # ============================================================

# def parse_weather_hour(value):
#     """
#     Parse Open-Meteo hourly timestamp.

#     Open-Meteo with timezone=auto normally returns:
#         2026-09-12T20:00

#     Some APIs may return:
#         2026-09-12T20:00:00
#     """

#     if not isinstance(value, str):
#         return None

#     value = value.strip()

#     try:
#         return datetime.fromisoformat(
#             value.replace("Z", "+00:00")
#         ).replace(tzinfo=None)

#     except Exception:
#         return None


# def filter_weather_to_session(
#     weather_data,
#     from_date,
#     to_date,
#     from_time,
#     to_time,
# ):
#     """
#     Extract ONLY Open-Meteo hourly values belonging to the
#     selected observation session.

#     This prevents a 7-day forecast from destroying the score.
#     """

#     if not isinstance(weather_data, dict):
#         return {
#             "times": [],
#             "temperature": [],
#             "humidity": [],
#             "dew_point": [],
#             "cloud_cover": [],
#             "precipitation_probability": [],
#             "visibility": [],
#             "wind_speed": [],
#             "wind_direction": [],
#             "wind_gusts": [],
#         }

#     hourly = weather_data.get("hourly")

#     if not isinstance(hourly, dict):
#         return {
#             "times": [],
#             "temperature": [],
#             "humidity": [],
#             "dew_point": [],
#             "cloud_cover": [],
#             "precipitation_probability": [],
#             "visibility": [],
#             "wind_speed": [],
#             "wind_direction": [],
#             "wind_gusts": [],
#         }

#     raw_times = hourly.get("time", [])

#     if not isinstance(raw_times, list):
#         raw_times = []

#     try:
#         session_start, session_end = build_observation_range(
#             from_date,
#             to_date,
#             from_time,
#             to_time,
#         )
#     except Exception:
#         return {
#             "times": [],
#             "temperature": [],
#             "humidity": [],
#             "dew_point": [],
#             "cloud_cover": [],
#             "precipitation_probability": [],
#             "visibility": [],
#             "wind_speed": [],
#             "wind_direction": [],
#             "wind_gusts": [],
#         }

#     selected_indexes = []

#     for index, raw_time in enumerate(raw_times):

#         parsed_time = parse_weather_hour(raw_time)

#         if parsed_time is None:
#             continue

#         if session_start <= parsed_time <= session_end:
#             selected_indexes.append(index)

#     fields = {
#         "temperature": "temperature_2m",
#         "humidity": "relative_humidity_2m",
#         "dew_point": "dew_point_2m",
#         "cloud_cover": "cloud_cover",
#         "precipitation_probability": "precipitation_probability",
#         "visibility": "visibility",
#         "wind_speed": "wind_speed_10m",
#         "wind_direction": "wind_direction_10m",
#         "wind_gusts": "wind_gusts_10m",
#     }

#     result = {
#         "times": [],
#     }

#     for output_key in fields:
#         result[output_key] = []

#     for index in selected_indexes:

#         result["times"].append(
#             raw_times[index]
#         )

#         for output_key, source_key in fields.items():

#             values = hourly.get(source_key, [])

#             if (
#                 isinstance(values, list)
#                 and index < len(values)
#             ):
#                 result[output_key].append(
#                     values[index]
#                 )

#     return result


# # ============================================================
# # NUMERIC HELPERS
# # ============================================================

# def numeric_values(values):
#     if not isinstance(values, list):
#         return []

#     result = []

#     for value in values:

#         if isinstance(value, bool):
#             continue

#         if isinstance(value, (int, float)):

#             if math.isfinite(float(value)):
#                 result.append(float(value))

#     return result


# def average(values):
#     values = numeric_values(values)

#     if not values:
#         return None

#     return sum(values) / len(values)


# def minimum(values):
#     values = numeric_values(values)

#     if not values:
#         return None

#     return min(values)


# def maximum(values):
#     values = numeric_values(values)

#     if not values:
#         return None

#     return max(values)


# def round_value(value, digits=1):
#     if value is None:
#         return None

#     try:
#         return round(float(value), digits)
#     except Exception:
#         return value


# # ============================================================
# # WEATHER SUMMARY
# # ============================================================

# def build_weather_summary(
#     weather_data,
#     from_date,
#     to_date,
#     from_time,
#     to_time,
# ):
#     """
#     Build a clean weather summary using ONLY the selected
#     observation period.
#     """

#     selected = filter_weather_to_session(
#         weather_data,
#         from_date,
#         to_date,
#         from_time,
#         to_time,
#     )

#     cloud = numeric_values(
#         selected.get("cloud_cover", [])
#     )

#     humidity = numeric_values(
#         selected.get("humidity", [])
#     )

#     visibility = numeric_values(
#         selected.get("visibility", [])
#     )

#     wind = numeric_values(
#         selected.get("wind_speed", [])
#     )

#     temperature = numeric_values(
#         selected.get("temperature", [])
#     )

#     dew_point = numeric_values(
#         selected.get("dew_point", [])
#     )

#     precipitation = numeric_values(
#         selected.get(
#             "precipitation_probability",
#             [],
#         )
#     )

#     return {
#         "selected_period": {
#             "from": f"{from_date} {from_time}",
#             "to": f"{to_date} {to_time}",
#         },

#         "data_points": len(
#             selected.get("times", [])
#         ),

#         "cloud_cover": round_value(
#             average(cloud),
#             1,
#         ),

#         "cloud_cover_min": round_value(
#             minimum(cloud),
#             1,
#         ),

#         "cloud_cover_max": round_value(
#             maximum(cloud),
#             1,
#         ),

#         "humidity": round_value(
#             average(humidity),
#             1,
#         ),

#         "humidity_min": round_value(
#             minimum(humidity),
#             1,
#         ),

#         "humidity_max": round_value(
#             maximum(humidity),
#             1,
#         ),

#         "visibility_km": round_value(
#             average(visibility),
#             1,
#         ),

#         "visibility_min_km": round_value(
#             minimum(visibility),
#             1,
#         ),

#         "visibility_max_km": round_value(
#             maximum(visibility),
#             1,
#         ),

#         "wind_speed_kmh": round_value(
#             average(wind),
#             1,
#         ),

#         "wind_speed_max_kmh": round_value(
#             maximum(wind),
#             1,
#         ),

#         "temperature_c": round_value(
#             average(temperature),
#             1,
#         ),

#         "temperature_min_c": round_value(
#             minimum(temperature),
#             1,
#         ),

#         "temperature_max_c": round_value(
#             maximum(temperature),
#             1,
#         ),

#         "dew_point_c": round_value(
#             average(dew_point),
#             1,
#         ),

#         "dew_point_min_c": round_value(
#             minimum(dew_point),
#             1,
#         ),

#         "dew_point_max_c": round_value(
#             maximum(dew_point),
#             1,
#         ),

#         "precipitation_probability": round_value(
#             average(precipitation),
#             1,
#         ),
#     }


# # ============================================================
# # SUN SUMMARY
# # ============================================================

# def build_sun_summary(sun_data):
#     if not isinstance(sun_data, dict):
#         return None

#     results = sun_data.get("results")

#     if not isinstance(results, dict):
#         return None

#     return {
#         "sunrise": results.get("sunrise"),
#         "sunset": results.get("sunset"),

#         "civil_twilight_begin": results.get(
#             "civil_twilight_begin"
#         ),

#         "civil_twilight_end": results.get(
#             "civil_twilight_end"
#         ),

#         "nautical_twilight_begin": results.get(
#             "nautical_twilight_begin"
#         ),

#         "nautical_twilight_end": results.get(
#             "nautical_twilight_end"
#         ),

#         "astronomical_twilight_begin": results.get(
#             "astronomical_twilight_begin"
#         ),

#         "astronomical_twilight_end": results.get(
#             "astronomical_twilight_end"
#         ),
#     }


# # ============================================================
# # MOON SUMMARY
# # ============================================================

# def build_moon_summary(planets):
#     """
#     Extract Moon ONLY if the planet module actually provides it.

#     We NEVER invent Moon phase or illumination.
#     """

#     if not isinstance(planets, list):
#         return None

#     moon = None

#     for item in planets:

#         if not isinstance(item, dict):
#             continue

#         name = item.get("name")

#         if not isinstance(name, str):
#             name = get_object_name(item)

#         if isinstance(name, str):
#             if name.strip().lower() == "moon":
#                 moon = item
#                 break

#     if not moon:
#         return None

#     return {
#         "name": "Moon",

#         "phase": first_not_none(
#             moon.get("phase"),
#             moon.get("moon_phase"),
#         ),

#         "illumination": first_not_none(
#             moon.get("illumination"),
#             moon.get("moon_illumination"),
#         ),

#         "rise": first_not_none(
#             moon.get("rise"),
#             moon.get("moonrise"),
#             moon.get("rise_time"),
#         ),

#         "set": first_not_none(
#             moon.get("set"),
#             moon.get("moonset"),
#             moon.get("set_time"),
#         ),

#         "altitude": first_not_none(
#             moon.get("altitude"),
#             moon.get("alt"),
#         ),

#         "azimuth": first_not_none(
#             moon.get("azimuth"),
#             moon.get("az"),
#         ),
#     }


# # ============================================================
# # VISIBILITY
# # ============================================================

# def is_visible(item):
#     if not isinstance(item, dict):
#         return False

#     value = item.get("visible")

#     if isinstance(value, bool):
#         return value

#     observability = item.get(
#         "observability"
#     )

#     if isinstance(observability, str):

#         lowered = observability.lower()

#         if any(
#             word in lowered
#             for word in [
#                 "visible",
#                 "excellent",
#                 "good",
#                 "fair",
#                 "observable",
#             ]
#         ):
#             return True

#         if any(
#             word in lowered
#             for word in [
#                 "not visible",
#                 "poor",
#                 "below horizon",
#                 "unobservable",
#             ]
#         ):
#             return False

#     return False


# def count_visibility(objects):
#     visible = 0
#     not_visible = 0

#     for item in objects:

#         if is_visible(item):
#             visible += 1
#         else:
#             not_visible += 1

#     return {
#         "visible": visible,
#         "not_visible": not_visible,
#         "total": len(objects),
#     }


# def build_visibility_summary(
#     planets,
#     deep_sky,
#     constellations,
#     meteor_showers,
# ):
#     """
#     Count actual astronomical targets.

#     Events are intentionally not included as targets.
#     """

#     all_objects = []

#     all_objects.extend(planets or [])
#     all_objects.extend(deep_sky or [])
#     all_objects.extend(constellations or [])
#     all_objects.extend(meteor_showers or [])

#     return count_visibility(all_objects)


# # ============================================================
# # DIFFICULTY
# # ============================================================

# def normalize_difficulty(value):
#     if not isinstance(value, str):
#         return None

#     value = value.strip().lower()

#     if value in [
#         "easy",
#         "beginner",
#     ]:
#         return "Easy"

#     if value in [
#         "medium",
#         "moderate",
#     ]:
#         return "Medium"

#     if value in [
#         "hard",
#         "difficult",
#     ]:
#         return "Hard"

#     if value in [
#         "very hard",
#         "expert",
#         "extreme",
#     ]:
#         return "Very Hard"

#     return None


# def build_difficulty_summary(
#     planets,
#     deep_sky,
#     constellations,
#     meteor_showers,
# ):
#     all_objects = []

#     all_objects.extend(planets or [])
#     all_objects.extend(deep_sky or [])
#     all_objects.extend(constellations or [])
#     all_objects.extend(meteor_showers or [])

#     summary = {
#         "Easy": 0,
#         "Medium": 0,
#         "Hard": 0,
#         "Very Hard": 0,
#         "Unknown": 0,
#     }

#     for item in all_objects:

#         if not isinstance(item, dict):
#             summary["Unknown"] += 1
#             continue

#         difficulty = normalize_difficulty(
#             item.get("difficulty")
#         )

#         if difficulty:
#             summary[difficulty] += 1
#         else:
#             summary["Unknown"] += 1

#     return summary


# # ============================================================
# # OBSERVATION QUALITY
# # ============================================================

# def calculate_observation_quality(
#     weather_summary,
#     visibility_summary,
# ):
#     """
#     Simple transparent scoring.

#     Weather:
#       Cloud        -> strongest factor
#       Humidity     -> moderate factor
#       Visibility   -> moderate factor
#       Wind         -> smaller factor

#     Astronomy:
#       Visible targets provide a smaller positive contribution.

#     This is NOT a scientific seeing/transparency calculation.
#     """

#     if not isinstance(weather_summary, dict):
#         weather_summary = {}

#     cloud = weather_summary.get(
#         "cloud_cover"
#     )

#     humidity = weather_summary.get(
#         "humidity"
#     )

#     visibility = weather_summary.get(
#         "visibility_km"
#     )

#     wind = weather_summary.get(
#         "wind_speed_kmh"
#     )

#     score = 0.0

#     # -------------------------
#     # CLOUD
#     # -------------------------

#     if isinstance(cloud, (int, float)):

#         if cloud <= 10:
#             score += 4.0
#         elif cloud <= 25:
#             score += 3.5
#         elif cloud <= 40:
#             score += 2.8
#         elif cloud <= 60:
#             score += 2.0
#         elif cloud <= 80:
#             score += 1.0
#         else:
#             score += 0.2

#     # -------------------------
#     # HUMIDITY
#     # -------------------------

#     if isinstance(humidity, (int, float)):

#         if humidity <= 60:
#             score += 2.0
#         elif humidity <= 70:
#             score += 1.6
#         elif humidity <= 80:
#             score += 1.1
#         elif humidity <= 90:
#             score += 0.6
#         else:
#             score += 0.2

#     # -------------------------
#     # VISIBILITY
#     # -------------------------

#     if isinstance(visibility, (int, float)):

#         if visibility >= 20:
#             score += 1.5
#         elif visibility >= 10:
#             score += 1.2
#         elif visibility >= 5:
#             score += 0.8
#         elif visibility >= 2:
#             score += 0.4
#         else:
#             score += 0.1

#     # -------------------------
#     # WIND
#     # -------------------------

#     if isinstance(wind, (int, float)):

#         if wind <= 10:
#             score += 1.0
#         elif wind <= 20:
#             score += 0.7
#         elif wind <= 30:
#             score += 0.4
#         else:
#             score += 0.1

#     # -------------------------
#     # VISIBLE TARGET BONUS
#     # -------------------------

#     if isinstance(visibility_summary, dict):

#         visible = visibility_summary.get(
#             "visible",
#             0,
#         )

#         if isinstance(visible, int):

#             if visible >= 15:
#                 score += 1.5
#             elif visible >= 10:
#                 score += 1.2
#             elif visible >= 5:
#                 score += 0.8
#             elif visible > 0:
#                 score += 0.4

#     score = max(
#         0,
#         min(
#             10,
#             round(score, 1),
#         ),
#     )

#     # -------------------------
#     # LABEL
#     # -------------------------

#     if score >= 8:
#         label = "Excellent"

#     elif score >= 6:
#         label = "Good"

#     elif score >= 4:
#         label = "Fair"

#     elif score >= 2:
#         label = "Poor"

#     else:
#         label = "Very Poor"

#     return {
#         "score": score,
#         "label": label,
#     }


# # ============================================================
# # WEATHER DISPLAY SUMMARY
# # ============================================================

# def build_weather_display(weather_summary):
#     """
#     Small clean values for frontend cards.
#     """

#     if not isinstance(weather_summary, dict):
#         return {
#             "cloud_cover": None,
#             "humidity": None,
#             "visibility": None,
#             "wind": None,
#             "temperature": None,
#             "dew_point": None,
#         }

#     return {
#         "cloud_cover": weather_summary.get(
#             "cloud_cover"
#         ),

#         "humidity": weather_summary.get(
#             "humidity"
#         ),

#         "visibility": weather_summary.get(
#             "visibility_km"
#         ),

#         "wind": weather_summary.get(
#             "wind_speed_kmh"
#         ),

#         "temperature": weather_summary.get(
#             "temperature_c"
#         ),

#         "dew_point": weather_summary.get(
#             "dew_point_c"
#         ),
#     }


# # ============================================================
# # AI DATA CLEANUP
# # ============================================================

# def build_ai_input(
#     observation,
#     weather_summary,
#     sun_summary,
#     moon_summary,
#     planets,
#     deep_sky,
#     constellations,
#     meteor_showers,
#     events,
# ):
#     """
#     Give Gemini clean structured information.

#     Raw Open-Meteo hourly arrays are intentionally NOT sent.
#     """

#     return {
#         "observation": observation,

#         "weather": weather_summary,

#         "sun": sun_summary,

#         "moon": moon_summary,

#         "planets": planets,

#         "deep_sky": deep_sky,

#         "constellations": constellations,

#         "meteor_showers": meteor_showers,

#         "events": events,
#     }


# # ============================================================
# # MAIN OBSERVATION API
# # ============================================================

# @router.post("/observation/analyze")
# def analyze_observation(
#     latitude: float = Query(...),
#     longitude: float = Query(...),

#     from_date: str = Query(...),
#     to_date: str = Query(...),

#     from_time: str = Query("20:00"),
#     to_time: str = Query("02:00"),
# ):

#     # ========================================================
#     # VALIDATE DATE / TIME
#     # ========================================================

#     try:

#         start_datetime, end_datetime = (
#             build_observation_range(
#                 from_date,
#                 to_date,
#                 from_time,
#                 to_time,
#             )
#         )

#     except Exception as e:

#         return {
#             "success": False,
#             "error": (
#                 "Invalid date/time format. "
#                 "Use YYYY-MM-DD for dates "
#                 "and HH:MM for times."
#             ),
#             "details": str(e),
#             "type": type(e).__name__,
#         }

#     observation = {
#         "latitude": latitude,
#         "longitude": longitude,

#         "from_date": from_date,
#         "to_date": to_date,

#         "from_time": from_time,
#         "to_time": to_time,

#         "start_local": (
#             start_datetime.isoformat()
#         ),

#         "end_local": (
#             end_datetime.isoformat()
#         ),
#     }

#     # ========================================================
#     # WEATHER
#     # ========================================================

#     weather_raw = safe_call(
#         get_weather,
#         latitude,
#         longitude,
#     )

#     weather_summary = build_weather_summary(
#         weather_raw,
#         from_date,
#         to_date,
#         from_time,
#         to_time,
#     )

#     weather_display = build_weather_display(
#         weather_summary
#     )

#     # ========================================================
#     # 7TIMER ASTRONOMICAL WEATHER
#     # ========================================================

#     astro_weather = None

#     if get_astro_weather is not None:

#         astro_weather = safe_call(
#             get_astro_weather,
#             latitude,
#             longitude,
#             from_date,
#             to_date,
#             from_time,
#             to_time,
#         )

#     # ========================================================
#     # SUN
#     # ========================================================

#     # Sunrise-Sunset API works date by date.
#     #
#     # For a multi-day observation period we use the start date
#     # as the primary sun reference.

#     sun_raw = safe_call(
#         get_sun,
#         latitude,
#         longitude,
#         from_date,
#     )

#     sun_summary = build_sun_summary(
#         sun_raw
#     )

#     # ========================================================
#     # PLANETS
#     # ========================================================

#     planets_raw = safe_call(
#         get_planets,
#         latitude,
#         longitude,
#         from_date,
#         to_date,
#         from_time,
#         to_time,
#     )

#     planets = normalize_planets(
#         planets_raw
#     )

#     # ========================================================
#     # MOON
#     # ========================================================

#     moon_summary = build_moon_summary(
#         planets
#     )

#     # ========================================================
#     # DEEP SKY
#     # ========================================================

#     deep_sky_raw = safe_call(
#         get_deep_sky,
#         latitude,
#         longitude,
#         from_date,
#         to_date,
#         from_time,
#         to_time,
#     )

#     deep_sky = normalize_deep_sky(
#         deep_sky_raw
#     )

#     # ========================================================
#     # CONSTELLATIONS
#     # ========================================================

#     constellations_raw = safe_call(
#         get_constellations,
#         latitude,
#         longitude,
#         from_date,
#         to_date,
#         from_time,
#         to_time,
#     )

#     constellations = normalize_constellations(
#         constellations_raw
#     )

#     # ========================================================
#     # METEOR SHOWERS
#     # ========================================================

#     meteor_showers_raw = safe_call(
#         get_meteor_showers,
#         latitude,
#         longitude,
#         from_date,
#         to_date,
#         from_time,
#         to_time,
#     )

#     meteor_showers = normalize_meteor_showers(
#         meteor_showers_raw
#     )

#     # ========================================================
#     # ASTRONOMICAL EVENTS
#     # ========================================================

#     events_raw = safe_call(
#         get_astronomical_events,
#         latitude,
#         longitude,
#         from_date,
#         to_date,
#         from_time,
#         to_time,
#     )

#     events = normalize_events(
#         events_raw
#     )

#     # ========================================================
#     # VISIBILITY
#     # ========================================================

#     visibility_summary = (
#         build_visibility_summary(
#             planets,
#             deep_sky,
#             constellations,
#             meteor_showers,
#         )
#     )

#     # ========================================================
#     # DIFFICULTY
#     # ========================================================

#     difficulty_summary = (
#         build_difficulty_summary(
#             planets,
#             deep_sky,
#             constellations,
#             meteor_showers,
#         )
#     )

#     # ========================================================
#     # OBSERVATION QUALITY
#     # ========================================================

#     observation_quality = (
#         calculate_observation_quality(
#             weather_summary,
#             visibility_summary,
#         )
#     )

#     # ========================================================
#     # OVERVIEW
#     # ========================================================

#     overview = {
#         "cloud_cover": weather_summary.get(
#             "cloud_cover"
#         ),

#         "humidity": weather_summary.get(
#             "humidity"
#         ),

#         "visibility_km": weather_summary.get(
#             "visibility_km"
#         ),

#         "wind_speed_kmh": weather_summary.get(
#             "wind_speed_kmh"
#         ),

#         "temperature_c": weather_summary.get(
#             "temperature_c"
#         ),

#         "dew_point_c": weather_summary.get(
#             "dew_point_c"
#         ),

#         "moon_illumination": (
#             moon_summary.get("illumination")
#             if moon_summary
#             else None
#         ),

#         "visible_targets": visibility_summary.get(
#             "visible",
#             0,
#         ),

#         "total_targets": visibility_summary.get(
#             "total",
#             0,
#         ),

#         "observation_score": observation_quality.get(
#             "score"
#         ),

#         "observation_label": observation_quality.get(
#             "label"
#         ),
#     }

#     # ========================================================
#     # AI RECOMMENDATION
#     # ========================================================

#     ai_recommendation = None

#     ai_input = build_ai_input(
#         observation=observation,
#         weather_summary=weather_summary,
#         sun_summary=sun_summary,
#         moon_summary=moon_summary,
#         planets=planets,
#         deep_sky=deep_sky,
#         constellations=constellations,
#         meteor_showers=meteor_showers,
#         events=events,
#     )

#     try:

#         ai_recommendation = generate_recommendation(
#             ai_input
#         )

#     except Exception as e:

#         ai_recommendation = {
#             "score": None,
#             "recommendation": (
#                 "AI recommendation unavailable."
#             ),
#             "best_time": None,
#             "best_targets": [],
#             "weather_summary": "",
#             "astronomy_summary": "",
#             "tips": [],
#             "error": str(e),
#         }

#     # ========================================================
#     # MODULE STATUS
#     # ========================================================

#     module_status = {
#         "weather": (
#             isinstance(weather_raw, dict)
#             and not weather_raw.get("error")
#         ),

#         "astro_weather": (
#             isinstance(astro_weather, dict)
#             and not astro_weather.get("error")
#         ),

#         "sun": (
#             isinstance(sun_raw, dict)
#             and not sun_raw.get("error")
#         ),

#         "planets": (
#             isinstance(planets_raw, dict)
#             and not planets_raw.get("error")
#         ),

#         "deep_sky": (
#             isinstance(deep_sky_raw, dict)
#             and not deep_sky_raw.get("error")
#         ),

#         "constellations": (
#             isinstance(constellations_raw, dict)
#             and not constellations_raw.get("error")
#         ),

#         "meteor_showers": (
#             isinstance(meteor_showers_raw, dict)
#             and not meteor_showers_raw.get("error")
#         ),

#         "events": (
#             isinstance(events_raw, dict)
#             and not events_raw.get("error")
#         ),

#         "ai_recommendation": (
#             isinstance(ai_recommendation, dict)
#             and not ai_recommendation.get("error")
#         ),
#     }

#     # ========================================================
#     # FINAL RESPONSE
#     # ========================================================

#     return {
#         "success": True,

#         # ----------------------------------------------------
#         # Observation
#         # ----------------------------------------------------

#         "observation": observation,

#         # ----------------------------------------------------
#         # Quick Summary
#         # ----------------------------------------------------

#         "overview": overview,

#         # ----------------------------------------------------
#         # Weather
#         # ----------------------------------------------------

#         "weather": weather_raw,

#         "weather_summary": weather_summary,

#         "weather_display": weather_display,

#         # ----------------------------------------------------
#         # Astronomical Weather / 7Timer
#         # ----------------------------------------------------

#         "astro_weather": astro_weather,

#         # ----------------------------------------------------
#         # Sun
#         # ----------------------------------------------------

#         "sun": sun_raw,

#         "sun_summary": sun_summary,

#         # ----------------------------------------------------
#         # Moon
#         # ----------------------------------------------------

#         "moon": moon_summary,

#         # ----------------------------------------------------
#         # Planets
#         # ----------------------------------------------------

#         "planets": {
#             "success": True,
#             "count": len(planets),
#             "objects": planets,
#         },

#         # ----------------------------------------------------
#         # Deep Sky
#         # ----------------------------------------------------

#         "deep_sky": {
#             "success": True,
#             "count": len(deep_sky),
#             "objects": deep_sky,
#         },

#         # ----------------------------------------------------
#         # Constellations
#         # ----------------------------------------------------

#         "constellations": {
#             "success": True,
#             "count": len(constellations),
#             "objects": constellations,
#         },

#         # ----------------------------------------------------
#         # Meteor Showers
#         # ----------------------------------------------------

#         "meteor_showers": {
#             "success": True,
#             "count": len(meteor_showers),
#             "showers": meteor_showers,
#         },

#         # ----------------------------------------------------
#         # Astronomical Events
#         # ----------------------------------------------------

#         "events": {
#             "success": True,
#             "count": (
#                 len(events.get("eclipses", []))
#                 + len(events.get("conjunctions", []))
#                 + len(events.get("oppositions", []))
#                 + len(events.get("occultations", []))
#             ),
#             "events": events,
#         },

#         # ----------------------------------------------------
#         # Visibility
#         # ----------------------------------------------------

#         "visibility_summary": visibility_summary,

#         "visibility_overview": {
#             "visible": visibility_summary.get(
#                 "visible",
#                 0,
#             ),

#             "not_visible": visibility_summary.get(
#                 "not_visible",
#                 0,
#             ),

#             "total": visibility_summary.get(
#                 "total",
#                 0,
#             ),
#         },

#         # ----------------------------------------------------
#         # Difficulty
#         # ----------------------------------------------------

#         "difficulty_summary": difficulty_summary,

#         # ----------------------------------------------------
#         # Overall Quality
#         # ----------------------------------------------------

#         "observation_quality": observation_quality,

#         # ----------------------------------------------------
#         # Gemini
#         # ----------------------------------------------------

#         "ai_recommendation": ai_recommendation,

#         # ----------------------------------------------------
#         # Module Status
#         # ----------------------------------------------------

#         "module_status": module_status,
#     }



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