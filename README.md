# Docker & Streamlit Practice

## What This Is

Simple Streamlit web app running in Docker. Started by hitting `ModuleNotFoundError` when trying to run it without Docker. Solved it by containerizing everything.

## The Problem

Tried running the app directly and got:

<img width="857" height="120" alt="image" src="https://github.com/user-attachments/assets/f25a4035-e1c0-484c-85b7-055ac6e31bab" />

Had to manually install packages each time. Docker solves this.

## Quick Start

### 1. Start Docker Desktop
Open Docker Desktop and wait for it to fully load.

### 2. Build the Image
```bash
cd `your setup location`
docker build -t streamlit-app .
```

### 3. Run the App
```bash
docker run -p 8501:8501 streamlit-app
```

### 4. Open Browser
Go to: **http://localhost:8501**

### 5. Stop
Press `Ctrl + C` in terminal

## Files Needed

- `app.py` — Your app
- `Dockerfile` — Docker config
- `requirements.txt` — Dependencies

## Dockerfile

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## requirements.txt

```
streamlit==1.28.0
pandas==2.0.0
```

## Errors that i faced

| Error | Fix |
|-------|-----|
| Docker daemon error and file not found error | Start Docker Desktop |
| Port 8501 in use | `docker run -p 8502:8501 streamlit-app` |

## Why Docker?

- ✅ No manual package installation
- ✅ Works the same everywhere
- ✅ Easy to share
- ✅ Isolated environment

**Status**: Working and Learning! 🎉


<img width="1908" height="961" alt="image" src="https://github.com/user-attachments/assets/50b37fdc-f34e-4f07-8aea-08a4bae6908d" />

