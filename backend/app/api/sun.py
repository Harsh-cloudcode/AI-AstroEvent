import requests
from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/sun")
def get_sun(
    latitude: float = Query(...),
    longitude: float = Query(...),
    date: str = Query(...)
):
    url = "https://api.sunrise-sunset.org/v2"

    params = {
        "lat": latitude,
        "lng": longitude,
        "date": date
    }

    response = requests.get(url, params=params)

    response.raise_for_status()

    return response.json()