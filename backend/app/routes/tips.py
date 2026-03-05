from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import httpx

router = APIRouter(prefix="/api/tips", tags=["Insider Tips"])

DRONOR_API = "http://3.211.238.155:9100/api/expert/run"

class TipsRequest(BaseModel):
    topic: str
    role: Optional[str] = None
    company_type: Optional[str] = None

@router.post("/search")
async def search_tips(request: TipsRequest):
    """Search for insider career tips."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            DRONOR_API,
            json={
                "expert_name": "careerup_insider_tips",
                "params": request.dict()
            },
            timeout=60
        )
    
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Expert execution failed")
    
    return response.json().get("result", {})
