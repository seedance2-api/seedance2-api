import os
import asyncio
import time
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SEEGEN_API_KEY")
BASE_URL = os.getenv("SEEGEN_BASE_URL", "https://seegen.ai/api/v1")
CALLBACK_URL = os.getenv("CALLBACK_URL")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


async def create_task(payload: dict):
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(f"{BASE_URL}/jobs/createTask", json=payload, headers=headers)
        resp.raise_for_status()
        return resp.json()


async def query_task(task_id: str):
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.get(f"{BASE_URL}/jobs/queryTask?taskId={task_id}", headers=headers)
        resp.raise_for_status()
        return resp.json()


async def get_credits():
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.get(f"{BASE_URL}/account/credits", headers=headers)
        resp.raise_for_status()
        return resp.json()


async def upload_asset(url: str, asset_type: str = "IMAGE", name: str = None):
    """Upload asset (IMAGE / VIDEO / AUDIO) for review"""
    payload = {
        "url": url,
        "type": asset_type,
        "name": name or f"asset_{int(time.time())}"
    }
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(f"{BASE_URL}/assets/upload", json=payload, headers=headers)
        resp.raise_for_status()
        return resp.json()


# ==================== Usage Examples ====================

if __name__ == "__main__":
    async def main():
        print("Available credits:", await get_credits())

        # Example 1: Text-to-Video
        payload = {
            "model": "sd2",
            "inputs": {
                "prompt": "A golden retriever running on the beach at sunset, cinematic lighting, highly detailed",
                "duration": "5s",
                "resolution": "1280x720"
            },
            "callBackUrl": CALLBACK_URL
        }

        result = await create_task(payload)
        task_id = result["taskId"]
        print(f"Task created successfully. Task ID: {task_id}")

        # Polling for result
        for _ in range(36):  # ~6 minutes max
            status = await query_task(task_id)
            print(f"Status: {status['status']}")
            if status["status"] == "COMPLETED":
                print("Generation completed!")
                print("Video URL:", status["output"][0]["url"])
                break
            elif status["status"] == "FAILED":
                print("Generation failed:", status.get("error"))
                break
            await asyncio.sleep(10)

    asyncio.run(main())
