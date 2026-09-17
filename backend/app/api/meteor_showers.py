# import requests

# from fastapi import APIRouter, Query
# from datetime import datetime, timezone, timedelta

# router = APIRouter()


# # ============================================================
# # OBSERVABILITY
# # ============================================================

# def get_meteor_observability(radiant_altitude):

#     # If API does not provide altitude,
#     # still allow the meteor shower to be returned.
#     if radiant_altitude is None:
#         return {
#             "visible": True,
#             "observability": "active",
#             "naked_eye": True,
#             "difficulty": "easy",
#             "recommendation": (
#                 "Meteor shower is active during the "
#                 "selected observation period. "
#                 "Best observed with the naked eye."
#             )
#         }

#     try:
#         altitude = float(radiant_altitude)

#     except (ValueError, TypeError):
#         return {
#             "visible": True,
#             "observability": "active",
#             "naked_eye": True,
#             "difficulty": "easy",
#             "recommendation": (
#                 "Meteor shower is active during the "
#                 "selected observation period. "
#                 "Best observed with the naked eye."
#             )
#         }

#     # Below horizon
#     if altitude < 0:
#         return {
#             "visible": False,
#             "observability": "below_horizon",
#             "naked_eye": False,
#             "difficulty": "difficult",
#             "recommendation": (
#                 "The meteor shower radiant is below "
#                 "the horizon at the selected time."
#             )
#         }

#     # Excellent
#     if altitude >= 40:
#         return {
#             "visible": True,
#             "observability": "excellent",
#             "naked_eye": True,
#             "difficulty": "easy",
#             "recommendation": (
#                 "Excellent meteor shower conditions. "
#                 "Best observed with the naked eye."
#             )
#         }

#     # Good
#     if altitude >= 20:
#         return {
#             "visible": True,
#             "observability": "good",
#             "naked_eye": True,
#             "difficulty": "easy",
#             "recommendation": (
#                 "Good meteor shower conditions. "
#                 "Best observed with the naked eye."
#             )
#         }

#     # Low
#     if altitude >= 10:
#         return {
#             "visible": True,
#             "observability": "low",
#             "naked_eye": True,
#             "difficulty": "moderate",
#             "recommendation": (
#                 "Meteor shower is visible, but the "
#                 "radiant is relatively low."
#             )
#         }

#     # Very low
#     return {
#         "visible": True,
#         "observability": "very_low",
#         "naked_eye": True,
#         "difficulty": "difficult",
#         "recommendation": (
#             "Meteor shower is very low in the sky. "
#             "Observation may be difficult."
#         )
#     }


# # ============================================================
# # GET RADIANT ALTITUDE
# # ============================================================

# def get_radiant_altitude(detail):

#     radiant = detail.get("radiant")

#     if isinstance(radiant, dict):

#         altitude = radiant.get("altitude_deg")

#         if altitude is None:
#             altitude = radiant.get("altitude")

#         if altitude is not None:
#             return altitude

#     return None


# # ============================================================
# # METEOR SHOWER DATA
# # ============================================================

# def get_meteor_showers_data(
#     latitude,
#     longitude,
#     from_date,
#     to_date,
#     from_time,
#     to_time
# ):

#     from_date = from_date.strip()
#     to_date = to_date.strip()
#     from_time = from_time.strip()
#     to_time = to_time.strip()

#     # ========================================================
#     # TIMEZONE
#     # ========================================================

#     india_timezone = timezone(
#         timedelta(hours=5, minutes=30)
#     )

#     start_local = datetime.strptime(
#         f"{from_date} {from_time}",
#         "%Y-%m-%d %H:%M"
#     ).replace(
#         tzinfo=india_timezone
#     )

#     end_local = datetime.strptime(
#         f"{to_date} {to_time}",
#         "%Y-%m-%d %H:%M"
#     ).replace(
#         tzinfo=india_timezone
#     )

#     if end_local <= start_local:

#         raise ValueError(
#             "To date/time must be after From date/time"
#         )

#     # ========================================================
#     # METEOR SHOWER CAL
#     # ========================================================

#     base_url = (
#         "https://meteorshowercal.com/api/v1"
#     )

#     headers = {
#         "User-Agent": "AstroEventAI/1.0"
#     }

#     # ========================================================
#     # STEP 1
#     # GET ALL SHOWERS
#     # ========================================================

#     response = requests.get(
#         f"{base_url}/showers",
#         headers=headers,
#         timeout=20
#     )

#     response.raise_for_status()

#     data = response.json()

#     if not isinstance(data, dict):
#         return []

#     all_showers = data.get(
#         "showers",
#         []
#     )

#     if not isinstance(all_showers, list):
#         return []

#     # ========================================================
#     # STEP 2
#     # GET DETAILS
#     # ========================================================

#     results = []

#     for shower in all_showers:

#         if not isinstance(shower, dict):
#             continue

#         code = shower.get("code")

#         if not code:
#             continue

#         try:

#             detail_response = requests.get(
#                 f"{base_url}/shower/{code}",
#                 params={
#                     "lat": latitude,
#                     "lon": longitude,
#                     "date": from_date
#                 },
#                 headers=headers,
#                 timeout=20
#             )

#         except requests.exceptions.RequestException:
#             continue

#         if detail_response.status_code != 200:
#             continue

#         try:

#             detail = detail_response.json()

#         except ValueError:
#             continue

#         if not isinstance(detail, dict):
#             continue

#         # ====================================================
#         # CHECK WHETHER SHOWER IS ACTIVE
#         # ====================================================

#         # Different versions of the API may use different
#         # names, so check the common activity fields.

#         active = None

#         if "active" in detail:
#             active = detail.get("active")

#         elif "active" in shower:
#             active = shower.get("active")

#         elif "is_active" in detail:
#             active = detail.get("is_active")

#         # If API explicitly says inactive, don't show it.
#         if active is False:
#             continue

#         # ====================================================
#         # RADIANT
#         # ====================================================

#         radiant_altitude = get_radiant_altitude(
#             detail
#         )

#         observability = get_meteor_observability(
#             radiant_altitude
#         )

#         # ====================================================
#         # IMPORTANT
#         #
#         # Only remove the shower when we KNOW the radiant
#         # is below the horizon.
#         #
#         # Missing altitude does NOT mean the shower doesn't
#         # exist.
#         # ====================================================

#         if (
#             radiant_altitude is not None
#             and observability["visible"] is False
#         ):
#             continue

#         # ====================================================
#         # ADD OUR CLEAN FIELDS
#         # ====================================================

#         detail["visible"] = True

#         detail["observability"] = (
#             observability["observability"]
#         )

#         detail["naked_eye"] = (
#             observability["naked_eye"]
#         )

#         detail["difficulty"] = (
#             observability["difficulty"]
#         )

#         detail["recommendation"] = (
#             observability["recommendation"]
#         )

#         # ====================================================
#         # ADD RADIANT ALTITUDE IF AVAILABLE
#         # ====================================================

#         if radiant_altitude is not None:

#             try:

#                 detail["radiant_altitude_deg"] = round(
#                     float(radiant_altitude),
#                     2
#                 )

#             except (ValueError, TypeError):

#                 detail["radiant_altitude_deg"] = None

#         else:

#             detail["radiant_altitude_deg"] = None

#         # ====================================================
#         # ADD TO RESULTS
#         # ====================================================

#         results.append(detail)

#     return results


# # ============================================================
# # API ROUTE
# # ============================================================

# @router.get("/meteor-showers")
# def get_meteor_showers(

#     latitude: float = Query(...),

#     longitude: float = Query(...),

#     from_date: str = Query(...),

#     to_date: str = Query(...),

#     from_time: str = Query("20:00"),

#     to_time: str = Query("02:00")

# ):

#     try:

#         from_date = from_date.strip()
#         to_date = to_date.strip()
#         from_time = from_time.strip()
#         to_time = to_time.strip()

#         # ====================================================
#         # TIMEZONE
#         # ====================================================

#         india_timezone = timezone(
#             timedelta(hours=5, minutes=30)
#         )

#         start_local = datetime.strptime(
#             f"{from_date} {from_time}",
#             "%Y-%m-%d %H:%M"
#         ).replace(
#             tzinfo=india_timezone
#         )

#         end_local = datetime.strptime(
#             f"{to_date} {to_time}",
#             "%Y-%m-%d %H:%M"
#         ).replace(
#             tzinfo=india_timezone
#         )

#         # ====================================================
#         # VALIDATE
#         # ====================================================

#         if end_local <= start_local:

#             return {
#                 "success": False,
#                 "error": (
#                     "To date/time must be after "
#                     "From date/time"
#                 )
#             }

#         # ====================================================
#         # GET DATA
#         # ====================================================

#         showers = get_meteor_showers_data(

#             latitude=latitude,

#             longitude=longitude,

#             from_date=from_date,

#             to_date=to_date,

#             from_time=from_time,

#             to_time=to_time

#         )

#         # ====================================================
#         # RESPONSE
#         # ====================================================

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

#                 "to_time": to_time,

#                 "start_local": (
#                     start_local.isoformat()
#                 ),

#                 "end_local": (
#                     end_local.isoformat()
#                 )

#             },

#             "count": len(showers),

#             "showers": showers,

#             "message": (

#                 "No meteor showers are active "
#                 "during the selected observation period."

#                 if not showers

#                 else None

#             ),

#             "source": {

#                 "name": "MeteorShowerCal",

#                 "url": (
#                     "https://meteorshowercal.com/"
#                 ),

#                 "license": "CC BY 4.0"

#             }

#         }

#     except requests.exceptions.RequestException as e:

#         return {

#             "success": False,

#             "error": (
#                 "Unable to fetch meteor shower data"
#             ),

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
# from datetime import datetime, timezone, timedelta, date

# router = APIRouter()


# # ============================================================
# # TIMEZONE
# # ============================================================

# INDIA_TIMEZONE = timezone(
#     timedelta(hours=5, minutes=30)
# )


# # ============================================================
# # OBSERVABILITY
# # ============================================================

# def get_meteor_observability(radiant_altitude):

#     if radiant_altitude is None:

#         return {
#             "visible": True,
#             "observability": "active",
#             "naked_eye": True,
#             "difficulty": "easy",
#             "recommendation": (
#                 "Meteor shower is active during the "
#                 "selected observation period. "
#                 "Best observed with the naked eye."
#             )
#         }

#     try:

#         altitude = float(radiant_altitude)

#     except (ValueError, TypeError):

#         return {
#             "visible": True,
#             "observability": "active",
#             "naked_eye": True,
#             "difficulty": "easy",
#             "recommendation": (
#                 "Meteor shower is active during the "
#                 "selected observation period. "
#                 "Best observed with the naked eye."
#             )
#         }

#     if altitude < 0:

#         return {
#             "visible": False,
#             "observability": "below_horizon",
#             "naked_eye": False,
#             "difficulty": "difficult",
#             "recommendation": (
#                 "The meteor shower radiant is below "
#                 "the horizon during the selected period."
#             )
#         }

#     if altitude >= 40:

#         return {
#             "visible": True,
#             "observability": "excellent",
#             "naked_eye": True,
#             "difficulty": "easy",
#             "recommendation": (
#                 "Excellent meteor shower conditions. "
#                 "Best observed with the naked eye."
#             )
#         }

#     if altitude >= 20:

#         return {
#             "visible": True,
#             "observability": "good",
#             "naked_eye": True,
#             "difficulty": "easy",
#             "recommendation": (
#                 "Good meteor shower conditions. "
#                 "Best observed with the naked eye."
#             )
#         }

#     if altitude >= 10:

#         return {
#             "visible": True,
#             "observability": "low",
#             "naked_eye": True,
#             "difficulty": "moderate",
#             "recommendation": (
#                 "Meteor shower is visible, but the "
#                 "radiant is relatively low."
#             )
#         }

#     return {
#         "visible": True,
#         "observability": "very_low",
#         "naked_eye": True,
#         "difficulty": "difficult",
#         "recommendation": (
#             "Meteor shower is very low in the sky. "
#             "Observation may be difficult."
#         )
#     }


# # ============================================================
# # CONVERT MM-DD TO DAY OF YEAR
# # ============================================================

# def month_day_to_day_of_year(value):

#     try:

#         month, day = map(
#             int,
#             value.split("-")
#         )

#         return date(
#             2024,
#             month,
#             day
#         ).timetuple().tm_yday

#     except Exception:

#         return None


# # ============================================================
# # CHECK WHETHER SHOWER IS ACTIVE ON A DATE
# # ============================================================

# def is_active_on_date(
#     selected_date,
#     start_mmdd,
#     end_mmdd
# ):

#     start_day = month_day_to_day_of_year(
#         start_mmdd
#     )

#     end_day = month_day_to_day_of_year(
#         end_mmdd
#     )

#     selected_day = date(
#         2024,
#         selected_date.month,
#         selected_date.day
#     ).timetuple().tm_yday

#     if (
#         start_day is None
#         or end_day is None
#     ):
#         return False

#     # --------------------------------------------------------
#     # NORMAL PERIOD
#     #
#     # Example:
#     # 04-15 -> 05-27
#     # --------------------------------------------------------

#     if start_day <= end_day:

#         return (
#             start_day
#             <= selected_day
#             <= end_day
#         )

#     # --------------------------------------------------------
#     # YEAR-CROSSING PERIOD
#     #
#     # Example:
#     # 12-28 -> 01-12
#     #
#     # Active:
#     # Dec 28 -> Dec 31
#     # OR
#     # Jan 1 -> Jan 12
#     # --------------------------------------------------------

#     return (
#         selected_day >= start_day
#         or
#         selected_day <= end_day
#     )


# # ============================================================
# # CHECK WHETHER SHOWER IS ACTIVE DURING SELECTED RANGE
# # ============================================================

# def is_active_during_range(
#     start_date,
#     end_date,
#     shower
# ):

#     shower_info = shower.get(
#         "shower",
#         {}
#     )

#     if not isinstance(shower_info, dict):
#         return False

#     active = shower_info.get(
#         "active"
#     )

#     if not isinstance(active, dict):
#         return False

#     active_start = active.get(
#         "start"
#     )

#     active_end = active.get(
#         "end"
#     )

#     if not active_start or not active_end:
#         return False

#     # --------------------------------------------------------
#     # Check every calendar date in selected period
#     # --------------------------------------------------------

#     current_date = start_date

#     while current_date <= end_date:

#         if is_active_on_date(
#             current_date,
#             active_start,
#             active_end
#         ):
#             return True

#         current_date += timedelta(
#             days=1
#         )

#     return False


# # ============================================================
# # GET RADIANT ALTITUDE
# # ============================================================

# def get_radiant_altitude(detail):

#     # --------------------------------------------------------
#     # New API structure:
#     #
#     # detail["shower"]["radiant"]
#     # --------------------------------------------------------

#     shower_info = detail.get(
#         "shower",
#         {}
#     )

#     if isinstance(shower_info, dict):

#         radiant = shower_info.get(
#             "radiant",
#             {}
#         )

#         if isinstance(radiant, dict):

#             altitude = radiant.get(
#                 "altitudeDeg"
#             )

#             if altitude is None:
#                 altitude = radiant.get(
#                     "altitude_deg"
#                 )

#             if altitude is None:
#                 altitude = radiant.get(
#                     "altitude"
#                 )

#             if altitude is not None:

#                 try:
#                     return float(altitude)

#                 except (
#                     ValueError,
#                     TypeError
#                 ):
#                     pass

#     # --------------------------------------------------------
#     # Older structure fallback
#     # --------------------------------------------------------

#     radiant = detail.get(
#         "radiant",
#         {}
#     )

#     if isinstance(radiant, dict):

#         altitude = radiant.get(
#             "altitudeDeg"
#         )

#         if altitude is None:
#             altitude = radiant.get(
#                 "altitude_deg"
#             )

#         if altitude is None:
#             altitude = radiant.get(
#                 "altitude"
#             )

#         if altitude is not None:

#             try:
#                 return float(altitude)

#             except (
#                 ValueError,
#                 TypeError
#             ):
#                 pass

#     return None


# # ============================================================
# # GET METEOR SHOWERS
# # ============================================================

# def get_meteor_showers_data(
#     latitude,
#     longitude,
#     from_date,
#     to_date,
#     from_time,
#     to_time
# ):

#     from_date = from_date.strip()
#     to_date = to_date.strip()
#     from_time = from_time.strip()
#     to_time = to_time.strip()

#     # ========================================================
#     # DATETIME
#     # ========================================================

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

#     if end_local <= start_local:

#         raise ValueError(
#             "To date/time must be after "
#             "From date/time"
#         )

#     start_date = start_local.date()
#     end_date = end_local.date()

#     # ========================================================
#     # API
#     # ========================================================

#     base_url = (
#         "https://meteorshowercal.com/api/v1"
#     )

#     headers = {
#         "User-Agent": "AstroEventAI/1.0"
#     }

#     # ========================================================
#     # GET ALL METEOR SHOWERS
#     # ========================================================

#     response = requests.get(
#         f"{base_url}/showers",
#         headers=headers,
#         timeout=20
#     )

#     response.raise_for_status()

#     data = response.json()

#     if not isinstance(data, dict):

#         return []

#     all_showers = data.get(
#         "showers",
#         []
#     )

#     if not isinstance(all_showers, list):

#         return []

#     results = []

#     # ========================================================
#     # PROCESS EACH SHOWER
#     # ========================================================

#     for shower in all_showers:

#         if not isinstance(
#             shower,
#             dict
#         ):
#             continue

#         code = shower.get(
#             "code"
#         )

#         if not code:
#             continue

#         # ====================================================
#         # FIRST FILTER:
#         # CHECK ACTIVITY DATES FROM /showers RESPONSE
#         # ====================================================

#         shower_active = shower.get(
#             "active"
#         )

#         if not isinstance(
#             shower_active,
#             dict
#         ):
#             continue

#         active_start = shower_active.get(
#             "start"
#         )

#         active_end = shower_active.get(
#             "end"
#         )

#         if not active_start or not active_end:
#             continue

#         # Build temporary structure for date checking
#         shower_for_check = {
#             "shower": {
#                 "active": {
#                     "start": active_start,
#                     "end": active_end
#                 }
#             }
#         }

#         # ====================================================
#         # IF NOT ACTIVE ON SELECTED DATE RANGE:
#         # DON'T EVEN CALL DETAIL API
#         # ====================================================

#         if not is_active_during_range(
#             start_date,
#             end_date,
#             shower_for_check
#         ):
#             continue

#         # ====================================================
#         # SECOND:
#         # GET DETAILS ONLY FOR ACTIVE SHOWERS
#         # ====================================================

#         detail_url = (
#             f"{base_url}/shower/{code}"
#         )

#         try:

#             detail_response = requests.get(
#                 detail_url,
#                 params={
#                     "lat": latitude,
#                     "lon": longitude,
#                     "date": from_date
#                 },
#                 headers=headers,
#                 timeout=20
#             )

#         except requests.exceptions.RequestException:

#             continue

#         if detail_response.status_code != 200:
#             continue

#         try:

#             detail = detail_response.json()

#         except ValueError:

#             continue

#         if not isinstance(
#             detail,
#             dict
#         ):
#             continue

#         # ====================================================
#         # FINAL DATE CHECK USING DETAIL RESPONSE
#         # ====================================================

#         if not is_active_during_range(
#             start_date,
#             end_date,
#             detail
#         ):

#             # If detail doesn't contain the activity data,
#             # use the /showers data already verified above.
#             detail_shower = detail.get(
#                 "shower",
#                 {}
#             )

#             detail_active = (
#                 detail_shower.get("active")
#                 if isinstance(
#                     detail_shower,
#                     dict
#                 )
#                 else None
#             )

#             if isinstance(
#                 detail_active,
#                 dict
#             ):

#                 if not is_active_during_range(
#                     start_date,
#                     end_date,
#                     {
#                         "shower": {
#                             "active": detail_active
#                         }
#                     }
#                 ):
#                     continue

#         # ====================================================
#         # RADIANT ALTITUDE
#         # ====================================================

#         radiant_altitude = get_radiant_altitude(
#             detail
#         )

#         observability = get_meteor_observability(
#             radiant_altitude
#         )

#         # ====================================================
#         # IF WE KNOW RADIANT IS BELOW HORIZON
#         # DON'T SHOW
#         # ====================================================

#         if (
#             radiant_altitude is not None
#             and observability["visible"] is False
#         ):
#             continue

#         # ====================================================
#         # ADD CLEAN DATA
#         # ====================================================

#         detail["visible"] = True

#         detail["observability"] = (
#             observability[
#                 "observability"
#             ]
#         )

#         detail["naked_eye"] = (
#             observability[
#                 "naked_eye"
#             ]
#         )

#         detail["difficulty"] = (
#             observability[
#                 "difficulty"
#             ]
#         )

#         detail["recommendation"] = (
#             observability[
#                 "recommendation"
#             ]
#         )

#         detail["radiant_altitude_deg"] = (
#             radiant_altitude
#         )

#         detail["selected_date"] = (
#             from_date
#         )

#         # ====================================================
#         # ADD ONLY THIS ACTIVE SHOWER
#         # ====================================================

#         results.append(
#             detail
#         )

#     return results


# # ============================================================
# # API
# # ============================================================

# @router.get("/meteor-showers")
# def get_meteor_showers(

#     latitude: float = Query(...),

#     longitude: float = Query(...),

#     from_date: str = Query(...),

#     to_date: str = Query(...),

#     from_time: str = Query("20:00"),

#     to_time: str = Query("02:00")

# ):

#     try:

#         from_date = from_date.strip()
#         to_date = to_date.strip()
#         from_time = from_time.strip()
#         to_time = to_time.strip()

#         start_local = datetime.strptime(
#             f"{from_date} {from_time}",
#             "%Y-%m-%d %H:%M"
#         ).replace(
#             tzinfo=INDIA_TIMEZONE
#         )

#         end_local = datetime.strptime(
#             f"{to_date} {to_time}",
#             "%Y-%m-%d %H:%M"
#         ).replace(
#             tzinfo=INDIA_TIMEZONE
#         )

#         if end_local <= start_local:

#             return {
#                 "success": False,
#                 "error": (
#                     "To date/time must be after "
#                     "From date/time"
#                 )
#             }

#         showers = get_meteor_showers_data(

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

#                 "to_time": to_time,

#                 "start_local": (
#                     start_local.isoformat()
#                 ),

#                 "end_local": (
#                     end_local.isoformat()
#                 )

#             },

#             "count": len(showers),

#             "showers": showers,

#             "message": (

#                 "No meteor showers are active "
#                 "during the selected observation period."

#                 if not showers

#                 else None

#             ),

#             "source": {

#                 "name": "MeteorShowerCal",

#                 "url": (
#                     "https://meteorshowercal.com/"
#                 ),

#                 "license": "CC BY 4.0"

#             }

#         }

#     except requests.exceptions.RequestException as e:

#         return {

#             "success": False,

#             "error": (
#                 "Unable to fetch meteor shower data"
#             ),

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
# from datetime import datetime, timezone, timedelta, date


# router = APIRouter()


# # ============================================================
# # TIMEZONE
# # ============================================================

# INDIA_TIMEZONE = timezone(
#     timedelta(hours=5, minutes=30)
# )


# # ============================================================
# # CONSTANTS
# # ============================================================

# BASE_URL = "https://meteorshowercal.com/api/v1"

# HEADERS = {
#     "User-Agent": "AstroEventAI/1.0"
# }


# # ============================================================
# # OBSERVABILITY
# # ============================================================

# def get_meteor_observability(radiant_altitude):

#     if radiant_altitude is None:
#         return {
#             "visible": True,
#             "observability": "active",
#             "naked_eye": True,
#             "difficulty": "easy",
#             "recommendation": (
#                 "Meteor shower is active during the selected "
#                 "observation period. Best observed with the naked eye."
#             )
#         }

#     try:
#         altitude = float(radiant_altitude)

#     except (ValueError, TypeError):

#         return {
#             "visible": True,
#             "observability": "active",
#             "naked_eye": True,
#             "difficulty": "easy",
#             "recommendation": (
#                 "Meteor shower is active during the selected "
#                 "observation period. Best observed with the naked eye."
#             )
#         }

#     # Below horizon
#     if altitude < 0:

#         return {
#             "visible": False,
#             "observability": "below_horizon",
#             "naked_eye": False,
#             "difficulty": "difficult",
#             "recommendation": (
#                 "The meteor shower radiant is below the "
#                 "horizon during the selected period."
#             )
#         }

#     # Excellent
#     if altitude >= 40:

#         return {
#             "visible": True,
#             "observability": "excellent",
#             "naked_eye": True,
#             "difficulty": "easy",
#             "recommendation": (
#                 "Excellent meteor shower conditions. "
#                 "Best observed with the naked eye."
#             )
#         }

#     # Good
#     if altitude >= 20:

#         return {
#             "visible": True,
#             "observability": "good",
#             "naked_eye": True,
#             "difficulty": "easy",
#             "recommendation": (
#                 "Good meteor shower conditions. "
#                 "Best observed with the naked eye."
#             )
#         }

#     # Low
#     if altitude >= 10:

#         return {
#             "visible": True,
#             "observability": "low",
#             "naked_eye": True,
#             "difficulty": "moderate",
#             "recommendation": (
#                 "Meteor shower is visible, but the radiant "
#                 "is relatively low."
#             )
#         }

#     # Very low
#     return {
#         "visible": True,
#         "observability": "very_low",
#         "naked_eye": True,
#         "difficulty": "difficult",
#         "recommendation": (
#             "Meteor shower is very low in the sky. "
#             "Observation may be difficult."
#         )
#     }


# # ============================================================
# # PARSE API DATE
# # ============================================================

# def parse_season_date(value):
#     """
#     Convert different possible API date formats into
#     a month/day tuple.

#     Supported examples:

#         12-13
#         12/13
#         2026-12-13
#         2026/12/13
#         12-13-2026
#         12/13/2026
#         ISO datetime strings
#     """

#     if value is None:
#         return None

#     if isinstance(value, date):
#         return value.month, value.day

#     value = str(value).strip()

#     if not value:
#         return None

#     # --------------------------------------------------------
#     # ISO datetime
#     # --------------------------------------------------------

#     try:
#         parsed = datetime.fromisoformat(
#             value.replace("Z", "+00:00")
#         )

#         return parsed.month, parsed.day

#     except Exception:
#         pass

#     # --------------------------------------------------------
#     # Remove time portion if present
#     # --------------------------------------------------------

#     value = value.split("T")[0]
#     value = value.split(" ")[0]

#     # --------------------------------------------------------
#     # Normalize separators
#     # --------------------------------------------------------

#     value = value.replace("/", "-")

#     parts = value.split("-")

#     try:

#         # ----------------------------------------------------
#         # YYYY-MM-DD
#         # ----------------------------------------------------

#         if len(parts) == 3:

#             if len(parts[0]) == 4:

#                 year = int(parts[0])
#                 month = int(parts[1])
#                 day = int(parts[2])

#                 date(
#                     year,
#                     month,
#                     day
#                 )

#                 return month, day

#             # ------------------------------------------------
#             # MM-DD-YYYY
#             # ------------------------------------------------

#             if len(parts[2]) == 4:

#                 month = int(parts[0])
#                 day = int(parts[1])
#                 year = int(parts[2])

#                 date(
#                     year,
#                     month,
#                     day
#                 )

#                 return month, day

#         # ----------------------------------------------------
#         # MM-DD
#         # ----------------------------------------------------

#         if len(parts) == 2:

#             month = int(parts[0])
#             day = int(parts[1])

#             # Validate
#             date(
#                 2024,
#                 month,
#                 day
#             )

#             return month, day

#     except Exception:
#         return None

#     return None


# # ============================================================
# # CONVERT MONTH/DAY TO DAY OF YEAR
# # ============================================================

# def month_day_to_day_of_year(value):

#     parsed = parse_season_date(value)

#     if parsed is None:
#         return None

#     month, day = parsed

#     try:

#         return date(
#             2024,
#             month,
#             day
#         ).timetuple().tm_yday

#     except Exception:

#         return None


# # ============================================================
# # CHECK WHETHER SHOWER IS ACTIVE ON A DATE
# # ============================================================

# def is_active_on_date(
#     selected_date,
#     start_value,
#     end_value
# ):

#     start_day = month_day_to_day_of_year(
#         start_value
#     )

#     end_day = month_day_to_day_of_year(
#         end_value
#     )

#     if start_day is None or end_day is None:
#         return False

#     # Use same reference year for comparison.
#     selected_reference = date(
#         2024,
#         selected_date.month,
#         selected_date.day
#     )

#     selected_day = selected_reference.timetuple().tm_yday

#     # --------------------------------------------------------
#     # NORMAL SEASON
#     #
#     # Example:
#     # 04-15 -> 05-27
#     # --------------------------------------------------------

#     if start_day <= end_day:

#         return (
#             start_day
#             <= selected_day
#             <= end_day
#         )

#     # --------------------------------------------------------
#     # YEAR-CROSSING SEASON
#     #
#     # Example:
#     #
#     # 12-28 -> 01-12
#     #
#     # Active:
#     # Dec 28 -> Dec 31
#     # OR
#     # Jan 1 -> Jan 12
#     # --------------------------------------------------------

#     return (
#         selected_day >= start_day
#         or selected_day <= end_day
#     )


# # ============================================================
# # EXTRACT ACTIVE PERIOD
# # ============================================================

# def get_active_period(shower_data):

#     if not isinstance(shower_data, dict):
#         return None, None

#     # --------------------------------------------------------
#     # Possible structure:
#     #
#     # {
#     #   "active": {
#     #       "start": "10-20",
#     #       "end": "12-10"
#     #   }
#     # }
#     # --------------------------------------------------------

#     active = shower_data.get("active")

#     if isinstance(active, dict):

#         start = active.get("start")
#         end = active.get("end")

#         if start and end:
#             return start, end

#     # --------------------------------------------------------
#     # Possible nested structure:
#     #
#     # shower.active
#     # --------------------------------------------------------

#     shower = shower_data.get("shower")

#     if isinstance(shower, dict):

#         active = shower.get("active")

#         if isinstance(active, dict):

#             start = active.get("start")
#             end = active.get("end")

#             if start and end:
#                 return start, end

#     return None, None


# # ============================================================
# # CHECK WHETHER SHOWER IS ACTIVE DURING RANGE
# # ============================================================

# def is_active_during_range(
#     start_date,
#     end_date,
#     shower
# ):

#     active_start, active_end = get_active_period(
#         shower
#     )

#     if not active_start or not active_end:
#         return False

#     current_date = start_date

#     while current_date <= end_date:

#         if is_active_on_date(
#             current_date,
#             active_start,
#             active_end
#         ):
#             return True

#         current_date += timedelta(days=1)

#     return False


# # ============================================================
# # GET RADIANT ALTITUDE
# # ============================================================

# def get_radiant_altitude(detail):

#     if not isinstance(detail, dict):
#         return None

#     # --------------------------------------------------------
#     # New API structure
#     # --------------------------------------------------------

#     shower_info = detail.get(
#         "shower",
#         {}
#     )

#     if isinstance(shower_info, dict):

#         radiant = shower_info.get(
#             "radiant",
#             {}
#         )

#         if isinstance(radiant, dict):

#             altitude = radiant.get(
#                 "altitudeDeg"
#             )

#             if altitude is None:
#                 altitude = radiant.get(
#                     "altitude_deg"
#                 )

#             if altitude is None:
#                 altitude = radiant.get(
#                     "altitude"
#                 )

#             if altitude is not None:

#                 try:
#                     return float(altitude)

#                 except (
#                     ValueError,
#                     TypeError
#                 ):
#                     pass

#     # --------------------------------------------------------
#     # Older structure
#     # --------------------------------------------------------

#     radiant = detail.get(
#         "radiant",
#         {}
#     )

#     if isinstance(radiant, dict):

#         altitude = radiant.get(
#             "altitudeDeg"
#         )

#         if altitude is None:
#             altitude = radiant.get(
#                 "altitude_deg"
#             )

#         if altitude is None:
#             altitude = radiant.get(
#                 "altitude"
#             )

#         if altitude is not None:

#             try:
#                 return float(altitude)

#             except (
#                 ValueError,
#                 TypeError
#             ):
#                 pass

#     return None


# # ============================================================
# # GET SHOWER NAME
# # ============================================================

# def get_shower_name(data):

#     if not isinstance(data, dict):
#         return None

#     # Direct fields
#     for key in [
#         "name",
#         "display_name",
#         "shower_name",
#         "title",
#         "label"
#     ]:

#         value = data.get(key)

#         if isinstance(value, str) and value.strip():
#             return value.strip()

#     # Nested shower
#     shower = data.get("shower")

#     if isinstance(shower, dict):

#         for key in [
#             "name",
#             "display_name",
#             "shower_name",
#             "title",
#             "label"
#         ]:

#             value = shower.get(key)

#             if isinstance(value, str) and value.strip():
#                 return value.strip()

#     return None


# # ============================================================
# # GET METEOR SHOWERS DATA
# # ============================================================

# def get_meteor_showers_data(
#     latitude,
#     longitude,
#     from_date,
#     to_date,
#     from_time="20:00",
#     to_time="02:00"
# ):

#     from_date = str(from_date).strip()
#     to_date = str(to_date).strip()
#     from_time = str(from_time).strip()
#     to_time = str(to_time).strip()

#     # ========================================================
#     # DATETIME
#     # ========================================================

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

#     if end_local <= start_local:

#         raise ValueError(
#             "To date/time must be after "
#             "From date/time"
#         )

#     start_date = start_local.date()
#     end_date = end_local.date()

#     # ========================================================
#     # GET ALL SHOWERS
#     # ========================================================

#     response = requests.get(
#         f"{BASE_URL}/showers",
#         headers=HEADERS,
#         timeout=20
#     )

#     response.raise_for_status()

#     data = response.json()

#     if not isinstance(data, dict):
#         return []

#     all_showers = data.get(
#         "showers",
#         []
#     )

#     if not isinstance(all_showers, list):
#         return []

#     results = []

#     # ========================================================
#     # PROCESS EACH SHOWER
#     # ========================================================

#     for shower in all_showers:

#         if not isinstance(shower, dict):
#             continue

#         code = shower.get("code")

#         if not code:
#             continue

#         # ====================================================
#         # GET SEASON DATES
#         # ====================================================

#         active_start, active_end = get_active_period(
#             shower
#         )

#         if not active_start or not active_end:
#             continue

#         # ====================================================
#         # IMPORTANT:
#         # FILTER BY THE USER'S ACTUAL DATE RANGE
#         # BEFORE CALLING DETAIL API
#         # ====================================================

#         if not is_active_during_range(
#             start_date,
#             end_date,
#             shower
#         ):
#             continue

#         # ====================================================
#         # DETAIL API
#         # ====================================================

#         detail_url = (
#             f"{BASE_URL}/shower/{code}"
#         )

#         try:

#             detail_response = requests.get(
#                 detail_url,
#                 params={
#                     "lat": latitude,
#                     "lon": longitude,
#                     "date": from_date
#                 },
#                 headers=HEADERS,
#                 timeout=20
#             )

#             detail_response.raise_for_status()

#         except requests.exceptions.RequestException:
#             continue

#         try:

#             detail = detail_response.json()

#         except ValueError:
#             continue

#         if not isinstance(detail, dict):
#             continue

#         # ====================================================
#         # IMPORTANT:
#         # VERIFY DETAIL DATE DATA IF AVAILABLE
#         # ====================================================

#         detail_start, detail_end = get_active_period(
#             detail
#         )

#         if detail_start and detail_end:

#             if not is_active_during_range(
#                 start_date,
#                 end_date,
#                 detail
#             ):
#                 continue

#         # ====================================================
#         # RADIANT ALTITUDE
#         # ====================================================

#         radiant_altitude = get_radiant_altitude(
#             detail
#         )

#         observability = get_meteor_observability(
#             radiant_altitude
#         )

#         # ====================================================
#         # BELOW HORIZON
#         # ====================================================

#         if (
#             radiant_altitude is not None
#             and observability["visible"] is False
#         ):
#             continue

#         # ====================================================
#         # NAME
#         # ====================================================

#         name = get_shower_name(detail)

#         if not name:
#             name = get_shower_name(shower)

#         # ====================================================
#         # MERGE SUMMARY DATA FROM /SHOWERS
#         # ====================================================

#         if name:
#             detail["name"] = name

#         detail["code"] = code

#         detail["visible"] = True

#         detail["observability"] = (
#             observability[
#                 "observability"
#             ]
#         )

#         detail["naked_eye"] = (
#             observability[
#                 "naked_eye"
#             ]
#         )

#         detail["difficulty"] = (
#             observability[
#                 "difficulty"
#             ]
#         )

#         detail["recommendation"] = (
#             observability[
#                 "recommendation"
#             ]
#         )

#         detail["radiant_altitude_deg"] = (
#             radiant_altitude
#         )

#         detail["selected_date"] = from_date

#         # Preserve season information
#         detail["active"] = {
#             "start": active_start,
#             "end": active_end
#         }

#         # ====================================================
#         # ADD ONLY VERIFIED ACTIVE SHOWER
#         # ====================================================

#         results.append(detail)

#     return results


# # ============================================================
# # API ROUTE
# # ============================================================

# @router.get("/meteor-showers")
# def get_meteor_showers(

#     latitude: float = Query(...),

#     longitude: float = Query(...),

#     from_date: str = Query(...),

#     to_date: str = Query(...),

#     from_time: str = Query("20:00"),

#     to_time: str = Query("02:00")

# ):

#     try:

#         from_date = from_date.strip()
#         to_date = to_date.strip()
#         from_time = from_time.strip()
#         to_time = to_time.strip()

#         start_local = datetime.strptime(
#             f"{from_date} {from_time}",
#             "%Y-%m-%d %H:%M"
#         ).replace(
#             tzinfo=INDIA_TIMEZONE
#         )

#         end_local = datetime.strptime(
#             f"{to_date} {to_time}",
#             "%Y-%m-%d %H:%M"
#         ).replace(
#             tzinfo=INDIA_TIMEZONE
#         )

#         if end_local <= start_local:

#             return {
#                 "success": False,
#                 "error": (
#                     "To date/time must be after "
#                     "From date/time"
#                 )
#             }

#         showers = get_meteor_showers_data(

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

#                 "to_time": to_time,

#                 "start_local": (
#                     start_local.isoformat()
#                 ),

#                 "end_local": (
#                     end_local.isoformat()
#                 )

#             },

#             "count": len(showers),

#             "showers": showers,

#             "message": (

#                 "No meteor showers are active "
#                 "during the selected observation period."

#                 if not showers

#                 else None

#             ),

#             "source": {

#                 "name": "MeteorShowerCal",

#                 "url": (
#                     "https://meteorshowercal.com/"
#                 ),

#                 "license": "CC BY 4.0"

#             }

#         }

#     except requests.exceptions.RequestException as e:

#         return {

#             "success": False,

#             "error": (
#                 "Unable to fetch meteor shower data"
#             ),

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

from fastapi import APIRouter, Query
from datetime import datetime, timezone, timedelta, date


router = APIRouter()


# ============================================================
# TIMEZONE
# ============================================================

INDIA_TIMEZONE = timezone(
    timedelta(hours=5, minutes=30)
)


# ============================================================
# CONSTANTS
# ============================================================

BASE_URL = "https://meteorshowercal.com/api/v1"

HEADERS = {
    "User-Agent": "AstroEventAI/1.0"
}


# ============================================================
# OBSERVABILITY
# ============================================================

def get_meteor_observability(radiant_altitude):

    if radiant_altitude is None:
        return {
            "visible": True,
            "observability": "active",
            "naked_eye": True,
            "difficulty": "easy",
            "recommendation": (
                "Meteor shower is active during the selected "
                "observation period. Best observed with the naked eye."
            )
        }

    try:
        altitude = float(radiant_altitude)

    except (ValueError, TypeError):

        return {
            "visible": True,
            "observability": "active",
            "naked_eye": True,
            "difficulty": "easy",
            "recommendation": (
                "Meteor shower is active during the selected "
                "observation period. Best observed with the naked eye."
            )
        }

    # Below horizon
    if altitude < 0:

        return {
            "visible": False,
            "observability": "below_horizon",
            "naked_eye": False,
            "difficulty": "difficult",
            "recommendation": (
                "The meteor shower radiant is below the "
                "horizon during the selected period."
            )
        }

    # Excellent
    if altitude >= 40:

        return {
            "visible": True,
            "observability": "excellent",
            "naked_eye": True,
            "difficulty": "easy",
            "recommendation": (
                "Excellent meteor shower conditions. "
                "Best observed with the naked eye."
            )
        }

    # Good
    if altitude >= 20:

        return {
            "visible": True,
            "observability": "good",
            "naked_eye": True,
            "difficulty": "easy",
            "recommendation": (
                "Good meteor shower conditions. "
                "Best observed with the naked eye."
            )
        }

    # Low
    if altitude >= 10:

        return {
            "visible": True,
            "observability": "low",
            "naked_eye": True,
            "difficulty": "moderate",
            "recommendation": (
                "Meteor shower is visible, but the radiant "
                "is relatively low."
            )
        }

    # Very low
    return {
        "visible": True,
        "observability": "very_low",
        "naked_eye": True,
        "difficulty": "difficult",
        "recommendation": (
            "Meteor shower is very low in the sky. "
            "Observation may be difficult."
        )
    }


# ============================================================
# PARSE API DATE
# ============================================================

def parse_season_date(value):
    """
    Convert different possible API date formats into
    a month/day tuple.

    Supported examples:

        12-13
        12/13
        2026-12-13
        2026/12/13
        12-13-2026
        12/13/2026
        ISO datetime strings
    """

    if value is None:
        return None

    if isinstance(value, date):
        return value.month, value.day

    value = str(value).strip()

    if not value:
        return None

    # --------------------------------------------------------
    # ISO datetime
    # --------------------------------------------------------

    try:
        parsed = datetime.fromisoformat(
            value.replace("Z", "+00:00")
        )

        return parsed.month, parsed.day

    except Exception:
        pass

    # --------------------------------------------------------
    # Remove time portion if present
    # --------------------------------------------------------

    value = value.split("T")[0]
    value = value.split(" ")[0]

    # --------------------------------------------------------
    # Normalize separators
    # --------------------------------------------------------

    value = value.replace("/", "-")

    parts = value.split("-")

    try:

        # ----------------------------------------------------
        # YYYY-MM-DD
        # ----------------------------------------------------

        if len(parts) == 3:

            if len(parts[0]) == 4:

                year = int(parts[0])
                month = int(parts[1])
                day = int(parts[2])

                date(
                    year,
                    month,
                    day
                )

                return month, day

            # ------------------------------------------------
            # MM-DD-YYYY
            # ------------------------------------------------

            if len(parts[2]) == 4:

                month = int(parts[0])
                day = int(parts[1])
                year = int(parts[2])

                date(
                    year,
                    month,
                    day
                )

                return month, day

        # ----------------------------------------------------
        # MM-DD
        # ----------------------------------------------------

        if len(parts) == 2:

            month = int(parts[0])
            day = int(parts[1])

            # Validate
            date(
                2024,
                month,
                day
            )

            return month, day

    except Exception:
        return None

    return None


# ============================================================
# CONVERT MONTH/DAY TO DAY OF YEAR
# ============================================================

def month_day_to_day_of_year(value):

    parsed = parse_season_date(value)

    if parsed is None:
        return None

    month, day = parsed

    try:

        return date(
            2024,
            month,
            day
        ).timetuple().tm_yday

    except Exception:

        return None


# ============================================================
# CHECK WHETHER SHOWER IS ACTIVE ON A DATE
# ============================================================

def is_active_on_date(
    selected_date,
    start_value,
    end_value
):

    start_day = month_day_to_day_of_year(
        start_value
    )

    end_day = month_day_to_day_of_year(
        end_value
    )

    if start_day is None or end_day is None:
        return False

    # Use same reference year for comparison.
    selected_reference = date(
        2024,
        selected_date.month,
        selected_date.day
    )

    selected_day = selected_reference.timetuple().tm_yday

    # --------------------------------------------------------
    # NORMAL SEASON
    #
    # Example:
    # 04-15 -> 05-27
    # --------------------------------------------------------

    if start_day <= end_day:

        return (
            start_day
            <= selected_day
            <= end_day
        )

    # --------------------------------------------------------
    # YEAR-CROSSING SEASON
    #
    # Example:
    #
    # 12-28 -> 01-12
    #
    # Active:
    # Dec 28 -> Dec 31
    # OR
    # Jan 1 -> Jan 12
    # --------------------------------------------------------

    return (
        selected_day >= start_day
        or selected_day <= end_day
    )


# ============================================================
# EXTRACT ACTIVE PERIOD
# ============================================================

def get_active_period(shower_data):

    if not isinstance(shower_data, dict):
        return None, None

    # --------------------------------------------------------
    # Possible structure:
    #
    # {
    #   "active": {
    #       "start": "10-20",
    #       "end": "12-10"
    #   }
    # }
    # --------------------------------------------------------

    active = shower_data.get("active")

    if isinstance(active, dict):

        start = active.get("start")
        end = active.get("end")

        if start and end:
            return start, end

    # --------------------------------------------------------
    # Possible nested structure:
    #
    # shower.active
    # --------------------------------------------------------

    shower = shower_data.get("shower")

    if isinstance(shower, dict):

        active = shower.get("active")

        if isinstance(active, dict):

            start = active.get("start")
            end = active.get("end")

            if start and end:
                return start, end

    return None, None


# ============================================================
# CHECK WHETHER SHOWER IS ACTIVE DURING RANGE
# ============================================================

def is_active_during_range(
    start_date,
    end_date,
    shower
):

    active_start, active_end = get_active_period(
        shower
    )

    if not active_start or not active_end:
        return False

    current_date = start_date

    while current_date <= end_date:

        if is_active_on_date(
            current_date,
            active_start,
            active_end
        ):
            return True

        current_date += timedelta(days=1)

    return False


# ============================================================
# GET RADIANT ALTITUDE
# ============================================================

def get_radiant_altitude(detail):

    if not isinstance(detail, dict):
        return None

    # --------------------------------------------------------
    # New API structure
    # --------------------------------------------------------

    shower_info = detail.get(
        "shower",
        {}
    )

    if isinstance(shower_info, dict):

        radiant = shower_info.get(
            "radiant",
            {}
        )

        if isinstance(radiant, dict):

            altitude = radiant.get(
                "altitudeDeg"
            )

            if altitude is None:
                altitude = radiant.get(
                    "altitude_deg"
                )

            if altitude is None:
                altitude = radiant.get(
                    "altitude"
                )

            if altitude is not None:

                try:
                    return float(altitude)

                except (
                    ValueError,
                    TypeError
                ):
                    pass

    # --------------------------------------------------------
    # Older structure
    # --------------------------------------------------------

    radiant = detail.get(
        "radiant",
        {}
    )

    if isinstance(radiant, dict):

        altitude = radiant.get(
            "altitudeDeg"
        )

        if altitude is None:
            altitude = radiant.get(
                "altitude_deg"
            )

        if altitude is None:
            altitude = radiant.get(
                "altitude"
            )

        if altitude is not None:

            try:
                return float(altitude)

            except (
                ValueError,
                TypeError
            ):
                pass

    return None


# ============================================================
# GET SHOWER NAME
# ============================================================

def get_shower_name(data):

    if not isinstance(data, dict):
        return None

    # Direct fields
    for key in [
        "name",
        "display_name",
        "shower_name",
        "title",
        "label"
    ]:

        value = data.get(key)

        if isinstance(value, str) and value.strip():
            return value.strip()

    # Nested shower
    shower = data.get("shower")

    if isinstance(shower, dict):

        for key in [
            "name",
            "display_name",
            "shower_name",
            "title",
            "label"
        ]:

            value = shower.get(key)

            if isinstance(value, str) and value.strip():
                return value.strip()

    return None


# ============================================================
# GET METEOR SHOWERS DATA
# ============================================================

def get_meteor_showers_data(
    latitude,
    longitude,
    from_date,
    to_date,
    from_time="20:00",
    to_time="02:00"
):

    from_date = str(from_date).strip()
    to_date = str(to_date).strip()
    from_time = str(from_time).strip()
    to_time = str(to_time).strip()

    # ========================================================
    # DATETIME
    # ========================================================

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

    if end_local <= start_local:

        raise ValueError(
            "To date/time must be after "
            "From date/time"
        )

    start_date = start_local.date()
    end_date = end_local.date()

    # ========================================================
    # GET ALL SHOWERS
    # ========================================================

    response = requests.get(
        f"{BASE_URL}/showers",
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    if not isinstance(data, dict):
        return []

    all_showers = data.get(
        "showers",
        []
    )

    if not isinstance(all_showers, list):
        return []

    results = []

    # ========================================================
    # PROCESS EACH SHOWER
    # ========================================================

    for shower in all_showers:

        if not isinstance(shower, dict):
            continue

        code = shower.get("code")

        if not code:
            continue

        # ====================================================
        # GET SEASON DATES
        # ====================================================

        active_start, active_end = get_active_period(
            shower
        )

        if not active_start or not active_end:
            continue

        # ====================================================
        # IMPORTANT:
        # FILTER BY THE USER'S ACTUAL DATE RANGE
        # BEFORE CALLING DETAIL API
        # ====================================================

        if not is_active_during_range(
            start_date,
            end_date,
            shower
        ):
            continue

        # ====================================================
        # DETAIL API
        # ====================================================

        detail_url = (
            f"{BASE_URL}/shower/{code}"
        )

        try:

            detail_response = requests.get(
                detail_url,
                params={
                    "lat": latitude,
                    "lon": longitude,
                    "date": from_date
                },
                headers=HEADERS,
                timeout=20
            )

            detail_response.raise_for_status()

        except requests.exceptions.RequestException:
            continue

        try:

            detail = detail_response.json()

        except ValueError:
            continue

        if not isinstance(detail, dict):
            continue

        # ====================================================
        # IMPORTANT:
        # VERIFY DETAIL DATE DATA IF AVAILABLE
        # ====================================================

        detail_start, detail_end = get_active_period(
            detail
        )

        if detail_start and detail_end:

            if not is_active_during_range(
                start_date,
                end_date,
                detail
            ):
                continue

        # ====================================================
        # RADIANT ALTITUDE
        # ====================================================

        radiant_altitude = get_radiant_altitude(
            detail
        )

        observability = get_meteor_observability(
            radiant_altitude
        )

        # ====================================================
        # BELOW HORIZON
        # ====================================================

        if (
            radiant_altitude is not None
            and observability["visible"] is False
        ):
            continue

        # ====================================================
        # NAME
        # ====================================================

        name = get_shower_name(detail)

        if not name:
            name = get_shower_name(shower)

        # ====================================================
        # MERGE SUMMARY DATA FROM /SHOWERS
        # ====================================================

        if name:
            detail["name"] = name

        detail["code"] = code

        detail["visible"] = True

        detail["observability"] = (
            observability[
                "observability"
            ]
        )

        detail["naked_eye"] = (
            observability[
                "naked_eye"
            ]
        )

        detail["difficulty"] = (
            observability[
                "difficulty"
            ]
        )

        detail["recommendation"] = (
            observability[
                "recommendation"
            ]
        )

        detail["radiant_altitude_deg"] = (
            radiant_altitude
        )

detail["radiant_altitude_deg"] = (
    radiant_altitude
)

# ========================================================
# BEST OBSERVATION WINDOW
# ========================================================

local_data = detail.get("local")

if isinstance(local_data, dict):

    best_window = local_data.get("bestWindow")

    if isinstance(best_window, dict):

        detail["best_window"] = {
            "start": best_window.get("start"),
            "end": best_window.get("end"),
        }

    hourly = local_data.get("hourly")

    if isinstance(hourly, list) and hourly:

        valid_hours = [
            item
            for item in hourly
            if isinstance(item, dict)
            and item.get("hr") is not None
        ]

        if valid_hours:

            peak_hour = max(
                valid_hours,
                key=lambda item: float(
                    item.get("hr", 0)
                )
            )

            detail["best_time"] = (
                peak_hour.get("local")
            )

            detail["peak_rate"] = (
                peak_hour.get("hr")
            )

            detail["peak_radiant_altitude_deg"] = (
                peak_hour.get("radiantAlt")
            )

detail["selected_date"] = from_date

# Preserve season information
detail["active"] = {
    "start": active_start,
    "end": active_end
}

# ====================================================
# ADD ONLY VERIFIED ACTIVE SHOWER
# ====================================================

results.append(detail)

return results

# ============================================================
# API ROUTE
# ============================================================

@router.get("/meteor-showers")
def get_meteor_showers(

    latitude: float = Query(...),

    longitude: float = Query(...),

    from_date: str = Query(...),

    to_date: str = Query(...),

    from_time: str = Query("20:00"),

    to_time: str = Query("02:00")

):

    try:

        from_date = from_date.strip()
        to_date = to_date.strip()
        from_time = from_time.strip()
        to_time = to_time.strip()

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

        if end_local <= start_local:

            return {
                "success": False,
                "error": (
                    "To date/time must be after "
                    "From date/time"
                )
            }

        showers = get_meteor_showers_data(

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

                "to_time": to_time,

                "start_local": (
                    start_local.isoformat()
                ),

                "end_local": (
                    end_local.isoformat()
                )

            },

            "count": len(showers),

            "showers": showers,

            "message": (

                "No meteor showers are active "
                "during the selected observation period."

                if not showers

                else None

            ),

            "source": {

                "name": "MeteorShowerCal",

                "url": (
                    "https://meteorshowercal.com/"
                ),

                "license": "CC BY 4.0"

            }

        }

    except requests.exceptions.RequestException as e:

        return {

            "success": False,

            "error": (
                "Unable to fetch meteor shower data"
            ),

            "details": str(e),

            "type": type(e).__name__

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e),

            "type": type(e).__name__

        }
