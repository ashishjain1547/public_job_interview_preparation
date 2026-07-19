import json
from openai import OpenAI
from app.config import settings
from app.schemas import BusinessInsights
from app.utils.logger import logger

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def analyze_with_llm(summary: dict) -> BusinessInsights:
    logger.info("Calling OpenAI API...")

    prompt = f"""
    You are a senior financial analyst.

    Given this business transaction summary:
{json.dumps(summary, indent=2)}

    Provide:
    1. Revenue overview
    2. Key findings (bullet list)
    3. Risk flags (bullet list)
    4. Strategic recommendations (bullet list)

    Return strictly valid JSON in this schema:
    {{
        "revenue_summary": "...",
        "key_findings": ["..."],
        "risk_flags": ["..."],
        "recommendations": ["..."]
    }}
    """

    response = client.chat.completions.create(
        model=settings.OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    content = response.choices[0].message.content
    parsed = json.loads(content)

    logger.info("LLM analysis completed.")
    return BusinessInsights(**parsed)
