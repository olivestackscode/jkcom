from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import asyncio
import random
import json
import os

app = FastAPI()

# Mount the public directory for static files
app.mount("/static", StaticFiles(directory="public"), name="static")

@app.get("/")
async def get():
    with open("public/index.html", "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.get("/api/status")
async def get_status():
    return {
        "status": "online",
        "version": "0.1.0",
        "sensors": ["camera", "radar", "gps"]
    }

@app.websocket("/ws/telemetry")
async def telemetry_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Simulate telemetry data
            data = {
                "timestamp": asyncio.get_event_loop().time(),
                "perception": {
                    "objects": [
                        {"id": 1, "class": "car", "distance": random.uniform(5, 50), "velocity": random.uniform(0, 30)},
                        {"id": 2, "class": "pedestrian", "distance": random.uniform(2, 20), "velocity": random.uniform(0, 5)}
                    ]
                },
                "localization": {
                    "lat": 6.4542 + random.uniform(-0.001, 0.001),
                    "lng": 3.3887 + random.uniform(-0.001, 0.001),
                    "heading": random.uniform(0, 360)
                },
                "radar": {
                    "points": [{"x": random.uniform(-10, 10), "y": random.uniform(0, 50)} for _ in range(10)]
                }
            }
            await websocket.send_text(json.dumps(data))
            await asyncio.sleep(0.5)
    except Exception as e:
        print(f"WebSocket closed: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
