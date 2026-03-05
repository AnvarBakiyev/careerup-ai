from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import httpx

router = APIRouter(prefix="/api/roadmap", tags=["Career Roadmap"])

DRONOR_API = "http://3.211.238.155:9100/api/expert/run"

class RoadmapRequest(BaseModel):
    current_role: str
    target_role: str
    target_company: Optional[str] = None
    timeline_months: int = 6

@router.post("/generate")
async def generate_roadmap(request: RoadmapRequest):
    """Generate personalized career roadmap."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            DRONOR_API,
            json={
                "expert_name": "careerup_roadmap_generator",
                "params": request.dict()
            },
            timeout=90
        )
    
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Expert execution failed")
    
    return response.json().get("result", {})
