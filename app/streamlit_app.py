from pathlib import Path

import streamlit as st
from PIL import Image
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[1]
WEIGHTS = ROOT / "models" / "best.pt"


@st.cache_resource
def load_model():
    if not WEIGHTS.exists():
        return None
    return YOLO(str(WEIGHTS))


st.set_page_config(page_title="Brain Tumor Detection", page_icon="🧠")
st.title("🧠 Brain Tumor Detection with YOLOv11")
st.caption("Coursework demo — not for clinical diagnosis or treatment decisions.")

model = load_model()
if model is None:
    st.error("Model file not found. Put the Colab-downloaded best.pt at models/best.pt.")
    st.stop()

confidence = st.slider("Confidence threshold", 0.05, 0.95, 0.25, 0.05)
image_file = st.file_uploader("Upload a brain MRI image", type=["jpg", "jpeg", "png"])

if image_file:
    image = Image.open(image_file).convert("RGB")
    st.image(image, caption="Uploaded image", use_container_width=True)
    if st.button("Run detection", type="primary"):
        result = model.predict(image, conf=confidence, verbose=False)[0]
        st.image(result.plot()[:, :, ::-1], caption="YOLOv11 prediction", use_container_width=True)
        if not result.boxes:
            st.warning("No tumor region was detected at this confidence threshold.")
        else:
            for box in result.boxes:
                class_name = result.names[int(box.cls[0])]
                score = float(box.conf[0])
                st.write(f"**{class_name}** — confidence: `{score:.1%}`")
