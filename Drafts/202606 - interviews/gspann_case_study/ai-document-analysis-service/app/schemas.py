from pydantic import BaseModel
from typing import List


class BusinessInsights(BaseModel):
    revenue_summary: str
    key_findings: List[str]
    risk_flags: List[str]
    recommendations: List[str]


class APIResponse(BaseModel):
    status: str
    data: BusinessInsights
