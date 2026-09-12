# import requests


# def get_weather(latitude, longitude):

#     url = "https://api.open-meteo.com/v1/forecast"

#     params = {
#         "latitude": latitude,
#         "longitude": longitude,

#         "hourly": [
#             "temperature_2m",
#             "relative_humidity_2m",
#             "dew_point_2m",
#             "cloud_cover",
#             "precipitation_probability",
#             "visibility",
#             "wind_speed_10m",
#             "wind_direction_10m",
#             "wind_gusts_10m"
#         ],

#         "timezone": "auto",
#         "forecast_days": 7
#     }

#     response = requests.get(url, params=params)

#     response.raise_for_status()

#     return response.json()

# import requests


# def get_weather(latitude, longitude):

#     url = "https://api.open-meteo.com/v1/forecast"

#     params = {
#         "latitude": latitude,
#         "longitude": longitude,

#         "hourly": [
#             "temperature_2m",
#             "relative_humidity_2m",
#             "dew_point_2m",
#             "cloud_cover",
#             "precipitation_probability",
#             "visibility",
#             "wind_speed_10m",
#             "wind_direction_10m",
#             "wind_gusts_10m"
#         ],

#         "timezone": "auto",
#         "forecast_days": 7
#     }

#     response = requests.get(url, params=params)

#     response.raise_for_status()

#     return response.json()


# import time
# import requests


# def get_weather(latitude, longitude):

#     url = "https://api.open-meteo.com/v1/forecast"

#     params = {
#         "latitude": latitude,
#         "longitude": longitude,

#         "hourly": [
#             "temperature_2m",
#             "relative_humidity_2m",
#             "dew_point_2m",
#             "cloud_cover",
#             "precipitation_probability",
#             "visibility",
#             "wind_speed_10m",
#             "wind_direction_10m",
#             "wind_gusts_10m",
#         ],

#         "timezone": "auto",
#         "forecast_days": 7,
#     }

#     max_retries = 3

#     for attempt in range(max_retries):

#         try:
#             response = requests.get(
#                 url,
#                 params=params,
#                 timeout=20,
#             )

#             # Open-Meteo rate limit
#             if response.status_code == 429:

#                 if attempt < max_retries - 1:
#                     wait_time = 5 * (attempt + 1)
#                     time.sleep(wait_time)
#                     continue

#                 return {
#                     "success": False,
#                     "error": "Weather API rate limit exceeded",
#                     "type": "RateLimitError",
#                 }

#             response.raise_for_status()

#             data = response.json()

#             return {
#                 "success": True,
#                 **data,
#             }

#         except requests.exceptions.RequestException as e:

#             if attempt < max_retries - 1:
#                 time.sleep(2)
#                 continue

#             return {
#                 "success": False,
#                 "error": str(e),
#                 "type": type(e).__name__,
#             }

#         except Exception as e:

#             return {
#                 "success": False,
#                 "error": str(e),
#                 "type": type(e).__name__,
#             }

#     return {
#         "success": False,
#         "error": "Unable to fetch weather data",
#         "type": "WeatherError",
#     }


# import requests


# def get_weather(latitude, longitude):

#     url = "https://api.open-meteo.com/v1/forecast"

#     params = {
#         "latitude": latitude,
#         "longitude": longitude,
#         "hourly": ",".join([
#             "temperature_2m",
#             "relative_humidity_2m",
#             "dew_point_2m",
#             "cloud_cover",
#             "visibility",
#             "wind_speed_10m",
#         ]),
#         "timezone": "auto",
#         "forecast_days": 3,
#     }

#     response = requests.get(
#         url,
#         params=params,
#         timeout=20,
#     )

#     if response.status_code == 429:
#         return {
#             "success": False,
#             "error": "Weather provider rate limit exceeded",
#             "type": "RateLimitError",
#         }

#     response.raise_for_status()

#     return {
#         "success": True,
#         **response.json(),
#     }




# import time
# import requests


# # ---------------------------------------------------------
# # SIMPLE IN-MEMORY WEATHER CACHE
# # ---------------------------------------------------------

# _weather_cache = {}

# # Keep successful weather data for 30 minutes
# CACHE_TTL = 30 * 60


# def get_weather(latitude, longitude):

#     # Round coordinates so tiny coordinate differences
#     # don't create unnecessary API requests.
#     cache_key = (
#         round(float(latitude), 4),
#         round(float(longitude), 4),
#     )

#     now = time.time()

#     # -----------------------------------------------------
#     # CHECK CACHE
#     # -----------------------------------------------------

#     if cache_key in _weather_cache:

#         cached = _weather_cache[cache_key]

#         cached_time = cached["time"]
#         cached_data = cached["data"]

#         # Fresh cache
#         if now - cached_time < CACHE_TTL:
#             return cached_data


#     # -----------------------------------------------------
#     # OPEN-METEO REQUEST
#     # -----------------------------------------------------

#     url = "https://api.open-meteo.com/v1/forecast"

#     params = {
#         "latitude": latitude,
#         "longitude": longitude,

#         "hourly": ",".join([
#             "temperature_2m",
#             "relative_humidity_2m",
#             "dew_point_2m",
#             "cloud_cover",
#             "visibility",
#             "wind_speed_10m",
#         ]),

#         "timezone": "auto",
#         "forecast_days": 3,
#     }

#     try:

#         response = requests.get(
#             url,
#             params=params,
#             timeout=20,
#         )

#         # -------------------------------------------------
#         # RATE LIMIT
#         # -------------------------------------------------

#         if response.status_code == 429:

#             # If we have old cached weather,
#             # return it instead of completely failing.
#             if cache_key in _weather_cache:

#                 stale_data = _weather_cache[cache_key]["data"]

#                 return {
#                     **stale_data,
#                     "cached": True,
#                     "stale": True,
#                 }

#             return {
#                 "success": False,
#                 "error": "Weather provider rate limit exceeded",
#                 "type": "RateLimitError",
#             }


#         # -------------------------------------------------
#         # OTHER HTTP ERRORS
#         # -------------------------------------------------

#         response.raise_for_status()

#         data = response.json()

#         result = {
#             "success": True,
#             **data,
#         }

#         # -------------------------------------------------
#         # SAVE SUCCESSFUL RESPONSE
#         # -------------------------------------------------

#         _weather_cache[cache_key] = {
#             "time": now,
#             "data": result,
#         }

#         return result


#     except requests.exceptions.Timeout:

#         # Try stale cache if request timed out
#         if cache_key in _weather_cache:

#             stale_data = _weather_cache[cache_key]["data"]

#             return {
#                 **stale_data,
#                 "cached": True,
#                 "stale": True,
#             }

#         return {
#             "success": False,
#             "error": "Weather provider request timed out",
#             "type": "TimeoutError",
#         }


#     except requests.exceptions.RequestException as e:

#         # Try stale cache for other request failures
#         if cache_key in _weather_cache:

#             stale_data = _weather_cache[cache_key]["data"]

#             return {
#                 **stale_data,
#                 "cached": True,
#                 "stale": True,
#             }

#         return {
#             "success": False,
#             "error": str(e),
#             "type": "WeatherAPIError",
#         }


#     except Exception as e:

#         return {
#             "success": False,
#             "error": str(e),
#             "type": type(e).__name__,
#         }


import os
import time
import requests
from dotenv import load_dotenv


# ---------------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# ---------------------------------------------------------

load_dotenv()


WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


# ---------------------------------------------------------
# SIMPLE IN-MEMORY WEATHER CACHE
# ---------------------------------------------------------

_weather_cache = {}

# Keep successful weather data for 30 minutes
CACHE_TTL = 30 * 60


# ---------------------------------------------------------
# WEATHER API
# ---------------------------------------------------------

def get_weather(latitude, longitude):

    cache_key = (
        round(float(latitude), 4),
        round(float(longitude), 4),
    )

    now = time.time()


    # -----------------------------------------------------
    # CHECK CACHE
    # -----------------------------------------------------

    if cache_key in _weather_cache:

        cached = _weather_cache[cache_key]

        if now - cached["time"] < CACHE_TTL:

            return cached["data"]


    # -----------------------------------------------------
    # TRY OPEN-METEO FIRST
    # -----------------------------------------------------

    open_meteo_url = "https://api.open-meteo.com/v1/forecast"

    open_meteo_params = {

        "latitude": latitude,
        "longitude": longitude,

        "hourly": ",".join([
            "temperature_2m",
            "relative_humidity_2m",
            "dew_point_2m",
            "cloud_cover",
            "visibility",
            "wind_speed_10m",
        ]),

        "timezone": "auto",
        "forecast_days": 3,
    }


    try:

        response = requests.get(
            open_meteo_url,
            params=open_meteo_params,
            timeout=15,
        )


        # -------------------------------------------------
        # OPEN-METEO SUCCESS
        # -------------------------------------------------

        if response.status_code == 200:

            data = response.json()

            result = {
                "success": True,
                **data,
            }

            _weather_cache[cache_key] = {
                "time": now,
                "data": result,
            }

            return result


        # -------------------------------------------------
        # OPEN-METEO RATE LIMIT
        # -------------------------------------------------

        if response.status_code == 429:

            print("Open-Meteo rate limit reached. Trying WeatherAPI...")


        else:

            print(
                f"Open-Meteo returned HTTP {response.status_code}. "
                "Trying WeatherAPI..."
            )


    except requests.exceptions.RequestException as e:

        print(
            f"Open-Meteo request failed: {e}. "
            "Trying WeatherAPI..."
        )


    # ---------------------------------------------------------
    # WEATHERAPI FALLBACK
    # ---------------------------------------------------------

    if not WEATHER_API_KEY:

        return {
            "success": False,
            "error": "WEATHER_API_KEY is not configured",
            "type": "ConfigurationError",
        }


    weatherapi_url = "https://api.weatherapi.com/v1/forecast.json"

    weatherapi_params = {

        "key": WEATHER_API_KEY,

        "q": f"{latitude},{longitude}",

        "days": 3,

        "aqi": "no",

        "alerts": "no",
    }


    try:

        response = requests.get(
            weatherapi_url,
            params=weatherapi_params,
            timeout=20,
        )

        response.raise_for_status()

        data = response.json()


        # -------------------------------------------------
        # CONVERT WEATHERAPI DATA INTO OPEN-METEO FORMAT
        # -------------------------------------------------

        hourly_times = []
        temperatures = []
        humidity = []
        dew_point = []
        cloud_cover = []
        visibility = []
        wind_speed = []


        for day in data.get("forecast", {}).get("forecastday", []):

            for hour in day.get("hour", []):

                hourly_times.append(
                    hour.get("time")
                )

                temperatures.append(
                    hour.get("temp_c")
                )

                humidity.append(
                    hour.get("humidity")
                )

                dew_point.append(
                    hour.get("dewpoint_c")
                )

                cloud_cover.append(
                    hour.get("cloud")
                )

                visibility.append(
                    hour.get("vis_km")
                )

                wind_speed.append(
                    hour.get("wind_kph")
                )


        result = {

            "success": True,

            "source": "WeatherAPI",

            "latitude": latitude,

            "longitude": longitude,

            "timezone": data.get(
                "location",
                {}
            ).get(
                "tz_id"
            ),

            "hourly": {

                "time": hourly_times,

                "temperature_2m": temperatures,

                "relative_humidity_2m": humidity,

                "dew_point_2m": dew_point,

                "cloud_cover": cloud_cover,

                "visibility": visibility,

                "wind_speed_10m": wind_speed,
            },
        }


        # -------------------------------------------------
        # SAVE FALLBACK RESULT TO CACHE
        # -------------------------------------------------

        _weather_cache[cache_key] = {

            "time": now,

            "data": result,
        }


        return result


    except requests.exceptions.RequestException as e:

        # -------------------------------------------------
        # USE STALE CACHE IF AVAILABLE
        # -------------------------------------------------

        if cache_key in _weather_cache:

            stale_data = _weather_cache[cache_key]["data"]

            return {
                **stale_data,
                "cached": True,
                "stale": True,
            }


        return {

            "success": False,

            "error": f"Weather fallback failed: {str(e)}",

            "type": "WeatherAPIError",
        }


    except Exception as e:

        return {

            "success": False,

            "error": str(e),

            "type": type(e).__name__,
        }
