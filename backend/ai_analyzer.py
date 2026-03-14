from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume(resume_text):

    prompt = f"""
You are an AI resume reviewer.

Analyze the following resume and provide:

1. Extracted Skills
2. Extracted Projects
3. Resume Score out of 10
4. Suggestions for improvement
5. A 2-line professional summary

Resume:
{resume_text}
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content