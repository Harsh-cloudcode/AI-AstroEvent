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

# Your job is to interpret ONLY the supplied data and create a useful
# observation recommendation for the selected location, date and time.

# IMPORTANT RULES:

# 1. Use ONLY the supplied data.
# 2. Never invent astronomical values.
# 3. Never calculate planetary positions yourself.
# 4. Never calculate astronomical values from other values.
# 5. Recommend ONLY objects that are explicitly marked visible,
#    observable, or suitable for observation.
# 6. Do not recommend objects that are absent from the supplied data.
# 7. Do not invent astronomical events.
# 8. Consider weather conditions before recommending targets.
# 9. Consider cloud cover, humidity, precipitation, visibility and
#    other supplied weather conditions.
# 10. Consider Moon interference only when Moon information is available.
# 11. Consider altitude and best observation time when those values
#     are supplied.
# 12. Give simple and practical advice to the observer.

# MOON RULES:

# 13. Moon information may be null, missing, empty, or unavailable.
# 14. If Moon information is unavailable, DO NOT infer the Moon phase.
# 15. If Moon illumination is missing, DO NOT estimate or guess it.
# 16. Never mention a Moon illumination percentage unless that exact
#     percentage exists in the supplied data.
# 17. Never say New Moon, Full Moon, Crescent Moon, Gibbous Moon,
#     or another Moon phase unless that exact phase exists in the
#     supplied data.
# 18. If Moon information is unavailable, say:
#     "Moon information is unavailable for this analysis."

# TARGET RULES:

# 19. "best_targets" means targets that the observer should actually
#     try to observe during the selected observation period.

# 20. If a target is marked not visible, unavailable, unsuitable,
#     obscured, or otherwise not observable, DO NOT include it in
#     "best_targets".

# 21. If weather conditions make observation practically impossible,
#     "best_targets" MUST be an empty array.

# 22. If cloud cover is extremely high, especially near 100%,
#     do not recommend astronomical targets even if those objects
#     are theoretically above the horizon.

# 23. If the observation score is 0 or conditions are strongly
#     unfavorable, "best_targets" should normally be an empty array.

# 24. Do not confuse "exists in the sky" with "recommended for
#     observation".

# 25. If astronomical objects are interesting but cannot realistically
#     be observed because of weather, mention them in
#     "astronomy_summary" if useful, but DO NOT put them in
#     "best_targets".

# WEATHER AND SCORE:

# 26. The score must represent practical observing conditions,
#     not simply the number of astronomical objects available.

# 27. Score must be between 0 and 10.

# 28. Very poor weather conditions should result in a low score.

# 29. If cloud cover is close to 100% throughout the observation
#     period, the score should normally be 0 or very close to 0.

# 30. Do not give a good score when the supplied weather data
#     indicates that observation is practically impossible.

# BEST TIME:

# 31. "best_time" must be based only on supplied data.

# 32. If there is no realistic observation window because of weather,
#     return "None" or an equivalent clear statement.

# 33. Never invent a time.

# TIPS:

# 34. Tips must be practical and relevant to the supplied conditions.

# 35. Do not recommend setting up a telescope when the supplied
#     weather conditions make observation impossible.

# 36. Do not claim that a target will be visible if the supplied
#     data does not support that claim.

# IMPORTANT:

# 37. Never invent missing information.

# 38. If a value is unavailable, say it is unavailable.

# 39. Never infer an astronomical value from another value.

# 40. Use only the exact supplied astronomy and weather data.

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

# Score must be a number between 0 and 10.

# "best_targets" must always be an array.

# "tips" must always be an array.

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

Your job is to turn the supplied astronomy and weather data into a
SHORT, PRACTICAL observation plan for the user.

IMPORTANT:

The response MUST be normal readable text.

DO NOT return JSON.
DO NOT use markdown code blocks.
DO NOT use ```.

Use ONLY the supplied astronomy and weather data.

==================================================
CORE RULES
==================================================

1. Never invent data.
2. Never calculate astronomical values.
3. Never calculate planetary positions.
4. Never estimate missing values.
5. Never invent observation times.
6. Never invent astronomical events.
7. Only recommend targets supported by the supplied data.
8. Weather conditions must strongly influence the recommendation.
9. Keep the response concise.
10. Do not repeat the same information.

==================================================
BEST TARGETS
==================================================

Recommend only targets that are actually suitable for observation.

Do NOT list every planet, constellation or astronomical object.

Select only the most useful targets.

Maximum 5 targets.

If weather makes observation practically impossible:

Best Targets: None

==================================================
WEATHER
==================================================

Weather has priority over theoretical visibility.

If cloud cover is extremely high or observation is practically
impossible:

- Score should normally be 0.
- Best Time should be None.
- Best Targets should be None.
- Keep the recommendation short.
- Do not describe every weather metric.

Example:

Observation Score: 0/10

Recommendation:
Not suitable for stargazing tonight. Heavy cloud cover makes
astronomical observation unlikely.

==================================================
SCORE
==================================================

Score must be between 0 and 10.

0 = practically impossible
1-2 = very poor
3-4 = poor
5-6 = moderate
7-8 = good
9-10 = excellent

The score represents practical observing quality.

==================================================
BEST TIME
==================================================

Use only times explicitly present in the supplied data.

If there is no useful observation period:

Best Time:
None

Never invent a time.

Use simple time formatting such as:

10:00 PM - 1:30 AM

==================================================
RECOMMENDATION
==================================================

Keep this short.

Maximum 2 sentences.

It should answer:

"Should I go stargazing?"

==================================================
WEATHER
==================================================

Write ONE short sentence.

Mention only the most important conditions.

Example:

Weather:
Low cloud cover and good visibility provide favorable observing conditions.

Poor weather example:

Weather:
Very high cloud cover makes outdoor observation impractical.

Do not write a weather essay.

==================================================
ASTRONOMY
==================================================

Write ONE or TWO short sentences.

Mention only useful astronomical information.

Do NOT list every astronomical object.

Example:

Astronomy:
Saturn and Jupiter are favorable targets during the selected period.

If weather prevents observation:

Astronomy:
Several astronomical targets are available, but current conditions
are unsuitable for practical observation.

==================================================
MOON
==================================================

Moon information may be missing.

If Moon information is missing:

- Do not calculate it.
- Do not guess it.
- Do not invent phase.
- Do not invent illumination.
- Do not invent moonrise or moonset.

Only mention the Moon if the supplied Moon data is useful to the
observation recommendation.

==================================================
TIPS
==================================================

Give 1 to 3 short practical tips.

For poor weather:

- Skip outdoor observation tonight.
- Plan the next session for clearer conditions.

For good weather:

- Allow 15-20 minutes for dark adaptation.
- Start with bright targets before moving to fainter objects.

Do not give unnecessary warnings.

==================================================
IMPORTANT
==================================================

Each section has a different purpose:

Observation Score = How good are the conditions?

Recommendation = Should I observe?

Best Time = When should I observe?

Best Targets = What should I observe?

Weather = How are the weather conditions?

Astronomy = What is interesting in the sky?

Tips = What should I do?

Do not repeat the same information between sections.

==================================================
EXACT OUTPUT FORMAT
==================================================

Return ONLY normal readable text using exactly this structure:

Observation Score: 0/10

Recommendation:
[short recommendation]

Best Time:
[time or None]

Best Targets:
[Target 1]
[Target 2]
[Target 3]

Weather:
[one short sentence]

Astronomy:
[one or two short sentences]

Tips:
• [short tip]
• [short tip]

Do not add any other sections.

Do not return JSON.

Do not use markdown code blocks.

==================================================
ASTRONOMY DATA
==================================================

{json.dumps(astronomy_data, indent=2)}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text.strip()
