from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import httpx

router = APIRouter(prefix="/api/cover-letter", tags=["Cover Letter Generator"])

DRONOR_API = "http://3.211.238.155:9100/api/expert/run"

class CoverLetterRequest(BaseModel):
    job_description: str
    resume_text: str
    company_name: str
    tone: str = "professional"

@router.post("/generate")
async def generate_cover_letter(request: CoverLetterRequest):
    """Generate personalized cover letter."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            DRONOR_API,
            json={
                "expert_name": "careerup_cover_letter_gen",
                "params": request.dict()
            },
            timeout=60
        )
    
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Expert execution failed")
    
    return response.json().get("result", {})
