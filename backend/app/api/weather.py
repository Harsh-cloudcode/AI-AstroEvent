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




import time
import requests


# ---------------------------------------------------------
# SIMPLE IN-MEMORY WEATHER CACHE
# ---------------------------------------------------------

_weather_cache = {}

# Keep successful weather data for 30 minutes
CACHE_TTL = 30 * 60


def get_weather(latitude, longitude):

    # Round coordinates so tiny coordinate differences
    # don't create unnecessary API requests.
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

        cached_time = cached["time"]
        cached_data = cached["data"]

        # Fresh cache
        if now - cached_time < CACHE_TTL:
            return cached_data


    # -----------------------------------------------------
    # OPEN-METEO REQUEST
    # -----------------------------------------------------

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
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
            url,
            params=params,
            timeout=20,
        )

        # -------------------------------------------------
        # RATE LIMIT
        # -------------------------------------------------

        if response.status_code == 429:

            # If we have old cached weather,
            # return it instead of completely failing.
            if cache_key in _weather_cache:

                stale_data = _weather_cache[cache_key]["data"]

                return {
                    **stale_data,
                    "cached": True,
                    "stale": True,
                }

            return {
                "success": False,
                "error": "Weather provider rate limit exceeded",
                "type": "RateLimitError",
            }


        # -------------------------------------------------
        # OTHER HTTP ERRORS
        # -------------------------------------------------

        response.raise_for_status()

        data = response.json()

        result = {
            "success": True,
            **data,
        }

        # -------------------------------------------------
        # SAVE SUCCESSFUL RESPONSE
        # -------------------------------------------------

        _weather_cache[cache_key] = {
            "time": now,
            "data": result,
        }

        return result


    except requests.exceptions.Timeout:

        # Try stale cache if request timed out
        if cache_key in _weather_cache:

            stale_data = _weather_cache[cache_key]["data"]

            return {
                **stale_data,
                "cached": True,
                "stale": True,
            }

        return {
            "success": False,
            "error": "Weather provider request timed out",
            "type": "TimeoutError",
        }


    except requests.exceptions.RequestException as e:

        # Try stale cache for other request failures
        if cache_key in _weather_cache:

            stale_data = _weather_cache[cache_key]["data"]

            return {
                **stale_data,
                "cached": True,
                "stale": True,
            }

        return {
            "success": False,
            "error": str(e),
            "type": "WeatherAPIError",
        }


    except Exception as e:

        return {
            "success": False,
            "error": str(e),
            "type": type(e).__name__,
        }
