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


import time
import requests


def get_weather(latitude, longitude):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,

        "hourly": [
            "temperature_2m",
            "relative_humidity_2m",
            "dew_point_2m",
            "cloud_cover",
            "precipitation_probability",
            "visibility",
            "wind_speed_10m",
            "wind_direction_10m",
            "wind_gusts_10m",
        ],

        "timezone": "auto",
        "forecast_days": 7,
    }

    max_retries = 3

    for attempt in range(max_retries):

        try:
            response = requests.get(
                url,
                params=params,
                timeout=20,
            )

            # Open-Meteo rate limit
            if response.status_code == 429:

                if attempt < max_retries - 1:
                    wait_time = 5 * (attempt + 1)
                    time.sleep(wait_time)
                    continue

                return {
                    "success": False,
                    "error": "Weather API rate limit exceeded",
                    "type": "RateLimitError",
                }

            response.raise_for_status()

            data = response.json()

            return {
                "success": True,
                **data,
            }

        except requests.exceptions.RequestException as e:

            if attempt < max_retries - 1:
                time.sleep(2)
                continue

            return {
                "success": False,
                "error": str(e),
                "type": type(e).__name__,
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e),
                "type": type(e).__name__,
            }

    return {
        "success": False,
        "error": "Unable to fetch weather data",
        "type": "WeatherError",
    }
