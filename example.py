import os
import json
import requests
from dotenv import load_dotenv

# load
load_dotenv()

API_KEY = os.getenv("SEEDANCE_API_KEY")
BASE_URL = os.getenv("SEEDANCE_BASE_URL", "https://api.seedance2-ai.com/v1")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def text2video_example():
    """text to video example"""
    payload = {
        "prompt": "A beautiful sunset over the ocean, realistic, 4K",
        "duration": 5,
        "width": 1024,
        "height": 576,
        "negative_prompt": "blurry, low quality, ugly"
    }
    
    response = requests.post(
        f"{BASE_URL}/generations/text2video",
        headers=headers,
        json=payload
    )
    
    print("Text2Video Response:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    return response.json()

def image2video_example(image_path):
    """image to video example"""
    files = {
        "image": open(image_path, "rb")
    }
    
    data = {
        "prompt": "Smooth motion, cinematic, high quality",
        "duration": 5,
        "motion_strength": 0.8
    }
    
    response = requests.post(
        f"{BASE_URL}/generations/image2video",
        headers={"Authorization": f"Bearer {API_KEY}"},
        files=files,
        data=data
    )
    
    print("\nImage2Video Response:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    return response.json()

def get_task_status_example(task_id):
    """get task status example"""
    response = requests.get(
        f"{BASE_URL}/tasks/{task_id}",
        headers=headers
    )
    
    print("\nTask Status:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    return response.json()

if __name__ == "__main__":
    # run example
    text2video_example()
    
    # image to video（replace to your path）
    # image2video_example("your_image.jpg")
