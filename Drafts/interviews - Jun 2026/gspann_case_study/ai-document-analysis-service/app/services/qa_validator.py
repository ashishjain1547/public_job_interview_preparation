from app.schemas import BusinessInsights


def validate_output(output: BusinessInsights, total_revenue: float):
    if total_revenue <= 0:
        raise ValueError("Invalid revenue calculation.")

    if not output.recommendations:
        raise ValueError("LLM returned empty recommendations.")

    return output
