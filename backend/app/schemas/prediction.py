# backend/app/schemas/prediction.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ForecastPoint(BaseModel):
    ds: datetime
    yhat: float
    yhat_lower: float
    yhat_upper: float


class ForecastResponse(BaseModel):
    metric: str
    full_name: str
    forecast: list[ForecastPoint]


class RiskAssessment(BaseModel):
    metric_type: str
    is_risky: bool
    severity: str
    peak_yhat: float
    expected_breach: Optional[datetime]
    confidence: float
