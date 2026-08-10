from io import BytesIO
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from PIL import Image
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[1]
WEIGHTS = ROOT / "models" / "best.pt"
app = FastAPI(title="Brain Tumor YOLOv11 API", version="1.0.0")
model = YOLO(str(WEIGHTS)) if WEIGHTS.exists() else None


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}


@app.post("/predict")
async def predict(file: UploadFile = File(...), confidence: float = 0.25):
    if model is None:
        raise HTTPException(503, "Model not found. Add models/best.pt before deploying.")
    if not 0.0 <= confidence <= 1.0:
        raise HTTPException(422, "confidence must be between 0 and 1")
    if file.content_type not in {"image/jpeg", "image/png"}:
        raise HTTPException(415, "Upload a JPEG or PNG image")

    image = Image.open(BytesIO(await file.read())).convert("RGB")
    result = model.predict(image, conf=confidence, verbose=False)[0]
    predictions = []
    for box in result.boxes:
        predictions.append({
            "class": result.names[int(box.cls[0])],
            "confidence": round(float(box.conf[0]), 4),
            "bbox_xyxy": [round(float(value), 2) for value in box.xyxy[0].tolist()],
        })
    return {"predictions": predictions, "count": len(predictions)}
