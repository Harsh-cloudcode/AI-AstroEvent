
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.weather import get_weather
from app.api.sun import router as sun_router
# from app.api.planets import router as planets_router
from app.api.planets import router as planets_router
from app.api.meteor_showers import router as meteor_showers_router
from app.api.deep_objects import router as deep_sky_router
from app.api.light_pollution import router as astro_weather_router
from app.api.atronomical_events import router as astronomical_events_router
from app.api.ai_recommendation import router as ai_recommendation_router
from app.api.observation import router as observation_router
from app.api.constellations import router as constellations_router


app = FastAPI(
    title="AstroEvent AI API",
    description="Astronomy observation planning backend",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://ai-astro-event.vercel.app",
        "https://ai-astro-event-84dq60j1v-harshaldeshmukh386-2972s-projects.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Basic Routes
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "AstroEvent AI backend is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# --------------------------------------------------
# Weather
# --------------------------------------------------

@app.get("/api/weather")
def weather():
    return get_weather(
        18.5204,
        73.8567
    )


# --------------------------------------------------
# Astronomy API Routers
# --------------------------------------------------

app.include_router(
    sun_router,
    prefix="/api"
)

app.include_router(
    planets_router,
    prefix="/api"
)

app.include_router(
    meteor_showers_router,
    prefix="/api"
)

app.include_router(
    deep_sky_router,
    prefix="/api"
)

app.include_router(
    astro_weather_router,
    prefix="/api"
)

app.include_router(
    astronomical_events_router,
    prefix="/api"
)

app.include_router(
    ai_recommendation_router,
    prefix="/api"
)

app.include_router(
    observation_router,
    prefix="/api"
)

app.include_router(
    constellations_router,
    prefix="/api"
)
