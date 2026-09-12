import requests
from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/astro-weather")
def get_astro_weather(
    latitude: float = Query(...),
    longitude: float = Query(...),
    from_date: str = Query(...),
    to_date: str = Query(...),
    from_time: str = Query("20:00"),
    to_time: str = Query("02:00")
):
    try:
        url = "https://www.7timer.info/bin/api.pl"

        params = {
            "lon": longitude,
            "lat": latitude,
            "product": "astro",
            "output": "json"
        }

        response = requests.get(
            url,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        return {
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

            "astronomical_conditions": data,

            "source": {
                "name": "7Timer!",
                "url": "https://www.7timer.info/"
            }
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": "Unable to fetch 7Timer data",
            "details": str(e),
            "type": type(e).__name__
        }

    except Exception as e:
        return {
            "error": str(e),
            "type": type(e).__name__
        }