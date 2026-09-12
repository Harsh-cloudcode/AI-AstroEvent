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
            "wind_gusts_10m"
        ],

        "timezone": "auto",
        "forecast_days": 7
    }

    response = requests.get(url, params=params)

    response.raise_for_status()

    return response.json()
