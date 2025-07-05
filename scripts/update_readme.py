import os
import openai

# Load API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Read existing README
with open("README.md", "r", encoding="utf-8") as f:
    current = f.read()

# Prepare prompt for AI
prompt = (
    "You are a GitHub Action assistant. "
    "Please improve and structure the following README for a Grafana dashboards project:\n\n"
    + current
)

# Call OpenAI with the new chat interface
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant for documentation."},
        {"role": "user",   "content": prompt}
    ],
    temperature=0.3,
)

# Extract and write updated content
updated = response.choices[0].message.content
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)
