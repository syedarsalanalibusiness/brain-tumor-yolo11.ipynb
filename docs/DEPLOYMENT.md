# GitHub and Live Deployment

## 1. Add trained weights

After running the Colab notebook, download `best.pt` and place it at `models/best.pt` in this project. Do not upload private medical data to a public repository.

## 2. Push to GitHub

Create an empty GitHub repository, then run these commands in the project folder:

```bash
git init
git add .
git commit -m "Add brain tumor YOLOv11 project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

## 3. Deploy the API on Render

1. Sign in to [Render](https://render.com/) using GitHub.
2. Choose **New +** → **Blueprint** and select this repository.
3. Confirm the `render.yaml` configuration and deploy.
4. When deployment succeeds, the live API URL is shown in the Render dashboard.
5. Check `https://YOUR-SERVICE.onrender.com/health`.

## 4. Run Streamlit locally

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

For a Streamlit Community Cloud live link, create a separate Streamlit deployment from the same GitHub repository, set the main file to `app/streamlit_app.py`, and make sure `models/best.pt` is available. For large weights, use a private release asset or cloud storage rather than committing the file.

## Deployment limitation

I can prepare all files, but I cannot publish to your GitHub or create a public live URL without access to your GitHub/hosting account. Once you provide the repository URL or connect GitHub, the exact live link can be finalized.
