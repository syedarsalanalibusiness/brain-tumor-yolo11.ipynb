# Brain Tumor Detection Using YOLOv11

This submission trains a YOLOv11 object-detection model to localize and classify brain tumors in MRI images.

## Dataset

- Classes: `Astrocytoma`, `Glioblastoma`
- Format: YOLO bounding-box labels
- Splits: `train`, `valid`, `test`
- Source archive: `brain.yolov11.zip`

## Submission contents

- `notebooks/brain_yolov11_colab.ipynb` — run-ready Google Colab notebook.
- `assignment/REPORT.md` — detailed, step-by-step assignment write-up.
- `app/streamlit_app.py` — optional prediction interface.
- `api/main.py` — optional FastAPI prediction API.
- `docs/DEPLOYMENT.md` — GitHub and live-link deployment steps.

## Important medical note

This project is for coursework and research demonstration only. It is not a diagnostic device and must not be used for clinical decision-making.
