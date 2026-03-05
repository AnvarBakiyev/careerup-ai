from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import httpx

router = APIRouter(prefix="/api/skills", tags=["Skill Assessment"])

DRONOR_API = "http://3.211.238.155:9100/api/expert/run"

class SkillRequest(BaseModel):
    role: str = "product_manager"
    answers_json: Optional[str] = None
    experience_years: int = 3

@router.post("/assess")
async def assess_skills(request: SkillRequest):
    """Get skill assessment questions or evaluate answers."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            DRONOR_API,
            json={
                "expert_name": "careerup_skill_assessor",
                "params": request.dict()
            },
            timeout=90
        )
    
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Expert execution failed")
    
    return response.json().get("result", {})
