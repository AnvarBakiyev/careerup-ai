from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import httpx

router = APIRouter(prefix="/api/personality", tags=["Personality Tests"])

DRONOR_API = "http://3.211.238.155:9100/api/expert/run"

class PersonalityRequest(BaseModel):
    test_type: str = "interview_perception"
    answers_json: Optional[str] = None
    target_role: Optional[str] = None

@router.post("/test")
async def personality_test(request: PersonalityRequest):
    """Get test questions or analyze answers."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            DRONOR_API,
            json={
                "expert_name": "careerup_personality_test",
                "params": request.dict()
            },
            timeout=60
        )
    
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Expert execution failed")
    
    return response.json().get("result", {})
