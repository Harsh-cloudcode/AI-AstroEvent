# import os
# import json

# from dotenv import load_dotenv
# from google import genai


# load_dotenv()

# client = genai.Client(
#     api_key=os.getenv("GEMINI_API_KEY")
# )


# def generate_recommendation(astronomy_data):

#     prompt = f"""
# You are AstroEvent AI, an astronomy observation planning assistant.

# You receive real astronomy and weather data from astronomy APIs.

# Your job is to interpret that data and create a useful observation
# recommendation for the selected location, date and time.

# IMPORTANT RULES:

# 1. Use ONLY the supplied data.
# 2. Never invent astronomical values.
# 3. Never calculate planetary positions yourself.
# 4. Recommend ONLY objects that are marked visible or observable.
# 5. Do not recommend objects that are absent from the supplied data.
# 6. Do not invent astronomical events.
# 7. Consider weather and astronomical conditions.
# 8. Consider Moon interference when data is available.
# 9. Consider altitude and best observation time.
# 10. Give simple, useful advice to the observer.

# Return ONLY valid JSON.

# Required format:

# {{
#     "score": 0,
#     "recommendation": "",
#     "best_time": "",
#     "best_targets": [],
#     "weather_summary": "",
#     "astronomy_summary": "",
#     "tips": []
# }}

# Score must be between 0 and 10.

# Astronomy data:

# {json.dumps(astronomy_data, indent=2)}
# """

#     response = client.models.generate_content(
#         model="gemini-3.5-flash",
#         contents=prompt
#     )

#     text = response.text

#     try:
#         return json.loads(text)

#     except json.JSONDecodeError:

#         return {
#             "score": None,
#             "recommendation": text,
#             "best_time": None,
#             "best_targets": [],
#             "weather_summary": "",
#             "astronomy_summary": "",
#             "tips": []
#         }


import os
import json

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_recommendation(astronomy_data):

    prompt = f"""
You are AstroEvent AI, an astronomy observation planning assistant.

You receive real astronomy and weather data from astronomy APIs.

Your job is to interpret ONLY the supplied data and create a useful
observation recommendation for the selected location, date and time.

IMPORTANT RULES:

1. Use ONLY the supplied data.
2. Never invent astronomical values.
3. Never calculate planetary positions yourself.
4. Never calculate astronomical values from other values.
5. Recommend ONLY objects that are explicitly marked visible,
   observable, or suitable for observation.
6. Do not recommend objects that are absent from the supplied data.
7. Do not invent astronomical events.
8. Consider weather conditions before recommending targets.
9. Consider cloud cover, humidity, precipitation, visibility and
   other supplied weather conditions.
10. Consider Moon interference only when Moon information is available.
11. Consider altitude and best observation time when those values
    are supplied.
12. Give simple and practical advice to the observer.

MOON RULES:

13. Moon information may be null, missing, empty, or unavailable.
14. If Moon information is unavailable, DO NOT infer the Moon phase.
15. If Moon illumination is missing, DO NOT estimate or guess it.
16. Never mention a Moon illumination percentage unless that exact
    percentage exists in the supplied data.
17. Never say New Moon, Full Moon, Crescent Moon, Gibbous Moon,
    or another Moon phase unless that exact phase exists in the
    supplied data.
18. If Moon information is unavailable, say:
    "Moon information is unavailable for this analysis."

TARGET RULES:

19. "best_targets" means targets that the observer should actually
    try to observe during the selected observation period.

20. If a target is marked not visible, unavailable, unsuitable,
    obscured, or otherwise not observable, DO NOT include it in
    "best_targets".

21. If weather conditions make observation practically impossible,
    "best_targets" MUST be an empty array.

22. If cloud cover is extremely high, especially near 100%,
    do not recommend astronomical targets even if those objects
    are theoretically above the horizon.

23. If the observation score is 0 or conditions are strongly
    unfavorable, "best_targets" should normally be an empty array.

24. Do not confuse "exists in the sky" with "recommended for
    observation".

25. If astronomical objects are interesting but cannot realistically
    be observed because of weather, mention them in
    "astronomy_summary" if useful, but DO NOT put them in
    "best_targets".

WEATHER AND SCORE:

26. The score must represent practical observing conditions,
    not simply the number of astronomical objects available.

27. Score must be between 0 and 10.

28. Very poor weather conditions should result in a low score.

29. If cloud cover is close to 100% throughout the observation
    period, the score should normally be 0 or very close to 0.

30. Do not give a good score when the supplied weather data
    indicates that observation is practically impossible.

BEST TIME:

31. "best_time" must be based only on supplied data.

32. If there is no realistic observation window because of weather,
    return "None" or an equivalent clear statement.

33. Never invent a time.

TIPS:

34. Tips must be practical and relevant to the supplied conditions.

35. Do not recommend setting up a telescope when the supplied
    weather conditions make observation impossible.

36. Do not claim that a target will be visible if the supplied
    data does not support that claim.

IMPORTANT:

37. Never invent missing information.

38. If a value is unavailable, say it is unavailable.

39. Never infer an astronomical value from another value.

40. Use only the exact supplied astronomy and weather data.

Return ONLY valid JSON.

Required format:

{{
    "score": 0,
    "recommendation": "",
    "best_time": "",
    "best_targets": [],
    "weather_summary": "",
    "astronomy_summary": "",
    "tips": []
}}

Score must be a number between 0 and 10.

"best_targets" must always be an array.

"tips" must always be an array.

Astronomy data:

{json.dumps(astronomy_data, indent=2)}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    text = response.text

    try:
        return json.loads(text)

    except json.JSONDecodeError:

        return {
            "score": None,
            "recommendation": text,
            "best_time": None,
            "best_targets": [],
            "weather_summary": "",
            "astronomy_summary": "",
            "tips": []
        }