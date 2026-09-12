from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai_recommendation import generate_recommendation


router = APIRouter()


class RecommendationRequest(BaseModel):

    astronomy_data: dict


@router.post("/ai/recommendation")
def ai_recommendation(
    request: RecommendationRequest
):

    try:

        result = generate_recommendation(
            request.astronomy_data
        )

        return {
            "success": True,
            "recommendation": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e),
            "type": type(e).__name__
        }