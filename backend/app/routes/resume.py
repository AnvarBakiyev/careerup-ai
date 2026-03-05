from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import Optional
import httpx

router = APIRouter(prefix="/api/resume", tags=["Resume Optimizer"])

DRONOR_API = "http://3.211.238.155:9100/api/expert/run"

class ResumeRequest(BaseModel):
    resume_text: str
    target_role: str
    target_company: Optional[str] = None

@router.post("/optimize")
async def optimize_resume(request: ResumeRequest):
    """Analyze and optimize resume."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            DRONOR_API,
            json={
                "expert_name": "careerup_resume_optimizer",
                "params": request.dict()
            },
            timeout=90
        )
    
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Expert execution failed")
    
    return response.json().get("result", {})
