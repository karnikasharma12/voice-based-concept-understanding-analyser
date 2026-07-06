import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_summary(transcript):
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=f"""
Summarize the following student's explanation in 3-4 lines.

Transcript:
{transcript}
"""
        )

        return response.output_text

    except Exception as e:
        return f"Summary generation failed: {e}"

