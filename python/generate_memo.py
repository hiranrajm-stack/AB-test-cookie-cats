import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

findings = """
Experiment: Cookie Cats gate placement (level 30 vs level 40)
Day-7 retention: gate_30 = 19.02%, gate_40 = 18.20%
p-value: 0.0016 (statistically significant)
95% CI on the drop: 0.31 to 1.33 percentage points
Engagement (avg gamerounds): gate_30 = 52, gate_40 = 51 (no meaningful change)
"""

prompt = f"""Write a concise business memo (under 250 words) for a product 
leadership team, based on this A/B test data:
{findings}
Include: recommendation, key evidence, and one risk/caveat to flag."""

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=prompt
)
print(response.text)
