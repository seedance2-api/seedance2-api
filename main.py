from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
import httpx
import os
from dotenv import load_dotenv
from typing import Dict, Any, Optional
import uvicorn

load_dotenv()

app = FastAPI(
    title="SeeGen AI (Seedance 2.0) Proxy",
    description="Official proxy for SeeGen.ai Seedance 2.0 Video Generation API",
    version="2.0.0"
)

BASE_URL = os.getenv("SEEGEN_BASE_URL", "https://seegen.ai/api/v1")
API_KEY = os.getenv("SEEGEN_API_KEY")

if not API_KEY:
    raise ValueError("SEEGEN_API_KEY must be set in .env file")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


@app.get("/")
async def root():
    return {
        "message": "SeeGen AI (Seedance 2.0) Proxy is running",
        "docs": "/docs"
    }


@app.post("/jobs/createTask")
async def create_task(payload: Dict[str, Any]):
    """Create a video generation task (text2video / image2video / keyframe / reference)"""
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{BASE_URL}/jobs/createTask", json=payload, headers=HEADERS)
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail=resp.text)
        return resp.json()


@app.get("/jobs/queryTask")
async def query_task(taskId: str = Query(..., alias="taskId")):
    """Query task status and result"""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/jobs/queryTask?taskId={taskId}", headers=HEADERS)
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail=resp.text)
        return resp.json()


@app.get("/account/credits")
async def get_credits():
    """Get account credit balance"""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/account/credits", headers=HEADERS)
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail=resp.text)
        return resp.json()


@app.post("/assets/upload")
async def upload_asset(payload: Dict[str, Any]):
    """Upload asset (IMAGE/VIDEO/AUDIO) for review"""
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{BASE_URL}/assets/upload", json=payload, headers=HEADERS)
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail=resp.text)
        return resp.json()


@app.get("/assets/status")
async def asset_status(assetId: Optional[str] = None, volcAssetId: Optional[str] = None):
    """Query asset review status"""
    params = {}
    if assetId:
        params["assetId"] = assetId
    if volcAssetId:
        params["volcAssetId"] = volcAssetId

    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/assets/status", params=params, headers=HEADERS)
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail=resp.text)
        return resp.json()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
