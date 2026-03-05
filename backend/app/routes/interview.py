from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import httpx

router = APIRouter(prefix="/api/interview", tags=["Interview Coach"])

DRONOR_API = "http://3.211.238.155:9100/api/expert/run"

class InterviewRequest(BaseModel):
    role: str = "product_manager"
    company_type: str = "faang"
    question_type: str = "behavioral"
    mode: str = "generate"
    user_answer: Optional[str] = None
    question_index: int = 0

class InterviewResponse(BaseModel):
    status: str
    question: Optional[str] = None
    tip: Optional[str] = None
    evaluation: Optional[dict] = None
    summary: Optional[str] = None

@router.post("/practice", response_model=InterviewResponse)
async def interview_practice(request: InterviewRequest):
    """Generate interview question or evaluate answer."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            DRONOR_API,
            json={
                "expert_name": "careerup_interview_coach",
                "params": request.dict()
            },
            timeout=60
        )
    
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Expert execution failed")
    
    result = response.json()
    return result.get("result", {})
