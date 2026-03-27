from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
import requests
import json
import os
from dotenv import load_dotenv
from typing import Optional, Dict, Any

# load
load_dotenv()

app = FastAPI(
    title="Seedance2 AI API",
    description="Seedance2 AI Video Generator API Service",
    version="1.0.0"
)

# config
BASE_URL = os.getenv("SEEDANCE_BASE_URL", "https://api.seedance2-ai.com/v1")
API_KEY = os.getenv("SEEDANCE_API_KEY")

if not API_KEY:
    raise ValueError("Please set SEEDANCE_API_KEY on .env")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

@app.get("/")
async def root():
    return {"message": "Seedance2 AI API working", "docs": "/docs"}

@app.post("/generate/text2video")
async def text2video(
    prompt: str = Form(...),
    duration: int = Form(5),
    width: int = Form(1024),
    height: int = Form(576),
    negative_prompt: Optional[str] = Form(None)
):
    """text to video"""
    try:
        payload = {
            "prompt": prompt,
            "duration": duration,
            "width": width,
            "height": height,
            "negative_prompt": negative_prompt
        }
        
        response = requests.post(
            f"{BASE_URL}/generations/text2video",
            headers=HEADERS,
            json=payload
        )
        
        if response.status_code not in (200, 201):
            raise HTTPException(
                status_code=response.status_code,
                detail=response.text
            )
            
        return JSONResponse(content=response.json())
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate/image2video")
async def image2video(
    image: UploadFile = File(...),
    prompt: str = Form(...),
    duration: int = Form(5),
    motion_strength: float = Form(0.8)
):
    """image to video"""
    try:
        files = {
            "image": (image.filename, await image.read(), image.content_type)
        }
        
        data = {
            "prompt": prompt,
            "duration": duration,
            "motion_strength": motion_strength
        }
        
        response = requests.post(
            f"{BASE_URL}/generations/image2video",
            headers={"Authorization": f"Bearer {API_KEY}"},
            files=files,
            data=data
        )
        
        if response.status_code not in (200, 201):
            raise HTTPException(
                status_code=response.status_code,
                detail=response.text
            )
            
        return JSONResponse(content=response.json())
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    """get task status"""
    try:
        response = requests.get(
            f"{BASE_URL}/tasks/{task_id}",
            headers=HEADERS
        )
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.text
            )
            
        return JSONResponse(content=response.json())
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tasks")
async def list_tasks(limit: int = 10, offset: int = 0):
    """get tasks list"""
    try:
        params = {"limit": limit, "offset": offset}
        response = requests.get(
            f"{BASE_URL}/tasks",
            headers=HEADERS,
            params=params
        )
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.text
            )
            
        return JSONResponse(content=response.json())
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
