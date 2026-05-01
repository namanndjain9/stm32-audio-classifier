from fastapi import FastAPI, UploadFile, File
import numpy as np
from datetime import datetime

app = FastAPI(title="STM32 Audio Test Server")

@app.post("/api/predict")
async def predict(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    
    # Basic info
    size_kb = len(audio_bytes) / 1024
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    print(f"\n{'='*60}")
    print(f"[{timestamp}] AUDIO RECEIVED!")
    print(f"Size: {size_kb:.2f} KB")
    print(f"Data type: {type(audio_bytes)}")
    print(f"First 10 bytes: {audio_bytes[:10]}")
    print(f"{'='*60}\n")
    
    # Simple response
    return {
        "status": "success",
        "message": "Audio received successfully",
        "size_kb": round(size_kb, 2),
        "received_at": timestamp,
        "note": "Ready for classification! ✅"
    }

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "STM32 Audio Classifier Backend is running",
        "endpoint": "/api/predict"
    }s
