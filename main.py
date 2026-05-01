from fastapi import FastAPI, UploadFile
import numpy as np

app = FastAPI(title="STM32 Audio Classifier")

@app.post("/api/predict")
async def predict(file: UploadFile):
    audio_bytes = await file.read()
    audio = np.frombuffer(audio_bytes, dtype=np.int16)  # adjust as needed
    # TODO: Run your model here
    result = {"class": "glass_break", "confidence": 0.92}
    return result

@app.get("/")
def home():
    return {"status": "STM32 Audio Classifier Backend Ready"}
