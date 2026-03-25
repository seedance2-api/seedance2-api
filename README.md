# Breaking News: Seedance 2.0 Official API Enters Open Phase

The official **Seedance 2.0 API** has now entered its open phase. However, API access is currently available **exclusively to trusted partners**.

As a premier trusted partner of ByteDance, we have successfully integrated with the official API. Building on this foundation, we are excited to launch our **Enhanced Proxy API**, enabling users worldwide to enjoy a superior generative experience ahead of general availability.

### 1. Core Capabilities and Current Limitations of the Official Seedance 2.0 API

The Seedance 2.0 API utilizes an advanced audio-video co-generation architecture and supports a rich set of multimodal inputs:  
- Text  
- Images (up to 9)  
- Videos (up to 3, total duration ≤15 seconds)  
- Audio files (up to 3 MP3s, total duration ≤15 seconds)  

It enables **director-level precise control**.

**However**, it currently has the following limitations:

- **Limited Access**: Still in early open phase and restricted to trusted partners only  
- **Resolution**: Default output is 720p  
- **Prompt Optimization**: The model is deeply optimized for Chinese-language prompts  
- **Server Location**: Official servers are located in mainland China  

### 2. Our Enhanced Proxy API: Breaking Through Official Limitations

We have built upon the official API with deep enhancements and global optimizations:

**Higher Resolution Support**  
We have added 2K and 4K output options. Through intelligent post-processing and enhancement, you can generate videos with sharper details and superior visual quality — perfect for professional deliverables and large-screen displays.

**Intelligent Multi-Language Conversion + Proprietary Prompt Enhancement**  
Our system integrates advanced NLP models that automatically translate and optimize prompts from any language (English, Japanese, Korean, Spanish, French, and more) into high-quality Chinese prompts.  

We also apply our proprietary **Prompt Enhancement Engine** to enrich details, optimize structure, and elevate creativity for natural language inputs.  

**Result**: Even casual, everyday descriptions can deliver top-tier results comparable to the official API’s native Chinese optimization.

**Low-Latency Global Deployment Across Multiple Regions**  
To solve the high-latency issues faced by overseas users, we have deployed acceleration nodes in the United States, Japan, Hong Kong, and other regions.  

Users can automatically or manually select the nearest node, significantly reducing latency and packet loss for a smooth, near-local calling experience.

All enhancements are seamlessly integrated. Simply call through our **Proxy API** to automatically enjoy every optimization — no extra configuration needed.

**Let's use Seedance 2.0 API Now**  

**Base URL:** `https://seedance2-ai.ai/api/v1`

- [Get your API key](https://seedance2-ai.ai/account)
- [Full interactive docs](https://seedance2-ai.ai/api-docs)

## Quick Start

```bash
# Check your credits
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://seedance2-ai.ai/api/v1/account/credits

# Generate a video from text
curl -X POST https://seedance2-ai.ai/api/v1/jobs/createTask \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance2",
    "inputs": {
      "prompt": "A golden retriever running on the beach at sunset",
      "duration": "5s",
      "resolution": "1280x720"
    }
  }'

# Poll for result
curl -H "Authorization: Bearer YOUR_API_KEY" \
  "https://seedance2-ai.ai/api/v1/jobs/queryTask?taskId=TASK_ID"
```

## Authentication

All requests require a Bearer token in the `Authorization` header:

```
Authorization: Bearer YOUR_API_KEY
```

API keys can be created in [Account Settings](https://seedance2-ai.ai/account) (max 10 per account, shown only once at creation).

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/jobs/createTask` | Create a video generation task |
| GET | `/jobs/queryTask?taskId={id}` | Query task status and result |
| GET | `/account/credits` | Check credit balance |

## Models

| Model | Description |
|-------|-------------|
| `seedance2` | Standard quality, best results |
| `seedance2-fast` | Faster generation, lower cost |

## Generation Modes

### Text-to-Video

Create videos from text prompts alone.

```bash
curl -X POST https://seedance2-ai.ai/api/v1/jobs/createTask \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance2",
    "inputs": {
      "prompt": "A golden retriever running on the beach at sunset",
      "duration": "5s",
      "resolution": "1280x720"
    }
  }'
```

### Image-to-Video

Animate a static image into a video.

```bash
curl -X POST https://seedance2-ai.ai/api/v1/jobs/createTask \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance2",
    "inputs": {
      "urls": ["https://example.com/photo.jpg"],
      "prompt": "The woman slowly turns her head and smiles",
      "duration": "5s"
    }
  }'
```

### Keyframe Mode

Define start and end frames — the model generates the transition between them.

```bash
curl -X POST https://seedance2-ai.ai/api/v1/jobs/createTask \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance2",
    "inputs": {
      "urls": [
        "https://example.com/first-frame.jpg",
        "https://example.com/last-frame.jpg"
      ],
      "prompt": "Smooth camera transition from day to night",
      "duration": "5s",
      "videoInputMode": "keyframe"
    }
  }'
```

### Multi-Reference Mode

Use multiple images, videos, and audio files to guide generation.

```bash
curl -X POST https://seedance2-ai.ai/api/v1/jobs/createTask \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance2",
    "inputs": {
      "urls": [
        "https://example.com/ref1.jpg",
        "https://example.com/ref2.jpg"
      ],
      "videoUrls": ["https://example.com/motion-ref.mp4"],
      "audioUrls": ["https://example.com/audio.mp3"],
      "prompt": "Character walks through a garden",
      "duration": "5s",
      "videoInputMode": "reference",
      "resolution": "1280x720"
    }
  }'
```

**Reference limits:** max 9 images, 3 videos, 3 audio files (12 total). Videos/audio must be ≤15s. Images must be ≥400px on shortest side.

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `model` | string | Yes | — | `"seedance2"` or `"seedance2-fast"` |
| `inputs.prompt` | string | No | — | Text description of video content |
| `inputs.urls` | string[] | No | — | Image URLs (1 for i2v, 2 for keyframe, up to 9 for reference) |
| `inputs.videoUrls` | string[] | No | — | Reference video URLs (reference mode only, max 3) |
| `inputs.audioUrls` | string[] | No | — | Reference audio URLs (reference mode only, max 3) |
| `inputs.duration` | string | No | `"5s"` | `"4s"` to `"15s"` |
| `inputs.resolution` | string | No | — | See supported resolutions below |
| `inputs.videoInputMode` | string | No | `"keyframe"` | `"keyframe"` or `"reference"` |
| `inputs.upscaleResolution` | string | No | — | `"2k"` or `"4k"` |
| `callBackUrl` | string | No | — | Webhook URL for async result notification |

**Supported resolutions:** `720x720` `720x960` `960x720` `1280x720` `720x1280` `1280x540`

## Responses

### Create Task

```json
{
  "taskId": "task_abc123"
}
```

### Query Task

```json
{
  "taskId": "task_abc123",
  "model": "seedance2",
  "status": "COMPLETED",
  "creditsUsed": 200,
  "output": [
    {
      "url": "https://static.seedance2-pro.com/videos/result.mp4",
      "width": 1280,
      "height": 720
    }
  ],
  "error": null,
  "createTime": 1711234567890,
  "completeTime": 1711234612345
}
```

**Task statuses:** `PENDING` → `PROCESSING` → `COMPLETED` or `FAILED`

### Check Credits

```json
{
  "credits": 5000,
  "availableCredits": 4800
}
```

## Webhook Callbacks

Provide a `callBackUrl` to receive a POST request when the task completes:

```bash
curl -X POST https://seedance2-ai.ai/api/v1/jobs/createTask \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance2",
    "callBackUrl": "https://your-server.com/webhook/seedance",
    "inputs": {
      "prompt": "A cat playing piano",
      "duration": "5s"
    }
  }'
```

The callback payload has the same schema as the [Query Task](#query-task) response. Retries up to 3 times (1s, 5s, 30s delays) on non-2xx responses.

## Credit Pricing

| Duration | seedance2 | seedance2-fast |
|----------|-----------|----------------|
| 5s base | 200 | 160 |
| 5s + 2K upscale | 300 | 260 |
| 5s + 4K upscale | 400 | 360 |

**Formula:** `duration_seconds × 40` credits (base rate), plus upscale surcharge.

Multi-reference mode with video inputs: base cost × 2 + upscale charges.

## Error Codes

| Status | Meaning | What to Do |
|--------|---------|------------|
| 400 | Invalid parameters | Check the error message and fix request body |
| 401 | Invalid or missing API key | Verify your `Authorization: Bearer` header |
| 402 | Insufficient credits | [Purchase more credits](https://seedance2-ai.ai/credits) |
| 403 | Access denied | You can only query your own tasks |
| 404 | Task not found | Verify the `taskId` is correct |
| 429 | Concurrency limit reached | Max 3 simultaneous tasks — wait for one to finish |
| 500 | Internal server error | Retry after a few seconds |

## JavaScript Example

```javascript
const API_KEY = process.env.SEEDANCE_API_KEY;
const BASE = "https://seedance2-ai.ai/api/v1";
const headers = {
  Authorization: `Bearer ${API_KEY}`,
  "Content-Type": "application/json",
};

// Check credits
const { availableCredits } = await fetch(`${BASE}/account/credits`, { headers }).then(r => r.json());
console.log(`Credits: ${availableCredits}`);

// Create task
const { taskId } = await fetch(`${BASE}/jobs/createTask`, {
  method: "POST",
  headers,
  body: JSON.stringify({
    model: "seedance2",
    inputs: {
      urls: ["https://example.com/photo.jpg"],
      prompt: "The person slowly looks up and smiles",
      duration: "5s",
    },
  }),
}).then(r => r.json());
console.log(`Task created: ${taskId}`);

// Poll for result (5s intervals, 5min timeout)
const start = Date.now();
while (Date.now() - start < 300_000) {
  const result = await fetch(`${BASE}/jobs/queryTask?taskId=${taskId}`, { headers }).then(r => r.json());

  if (result.status === "COMPLETED") {
    console.log(`Video: ${result.output[0].url}`);
    break;
  }
  if (result.status === "FAILED") {
    throw new Error(result.error);
  }

  await new Promise(r => setTimeout(r, 5000));
}
```

## Python Example

```python
import requests
import time
import os

API_KEY = os.environ["SEEDANCE_API_KEY"]
BASE = "https://seedance2-ai.ai/api/v1"
headers = {"Authorization": f"Bearer {API_KEY}"}

# Check credits
credits = requests.get(f"{BASE}/account/credits", headers=headers).json()
print(f"Credits: {credits['availableCredits']}")

# Create task
task = requests.post(
    f"{BASE}/jobs/createTask",
    headers=headers,
    json={
        "model": "seedance2",
        "inputs": {
            "urls": ["https://example.com/photo.jpg"],
            "prompt": "The person slowly looks up and smiles",
            "duration": "5s",
        },
    },
).json()
print(f"Task created: {task['taskId']}")

# Poll for result
for _ in range(60):
    result = requests.get(f"{BASE}/jobs/queryTask", headers=headers, params={"taskId": task["taskId"]}).json()

    if result["status"] == "COMPLETED":
        print(f"Video: {result['output'][0]['url']}")
        break
    if result["status"] == "FAILED":
        raise Exception(result["error"])

    time.sleep(5)
```

## Limits

- **Concurrency:** 3 simultaneous tasks per account
- **Video duration:** 4–15 seconds
- **API keys:** Up to 10 per account
- **Polling:** 5-second intervals recommended
- **Reference mode:** Max 12 files total (9 images + 3 videos + 3 audio)

## Links

- [API Documentation](https://seedance2-ai.ai/api-docs)
- [Get API Key](https://seedance2-ai.ai/account)
- [Purchase Credits](https://seedance2-ai.ai/credits)
