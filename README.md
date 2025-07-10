# 🌸 Iris Flower Classifier API (FastAPI + Docker)

A production-style API that predicts the species of an Iris flower based on input features using a trained Random Forest classifier. Fully containerized using Docker.

## 🚀 Features
- FastAPI backend
- Dockerized deployment
- Iris dataset (scikit-learn)
- Prediction with class names
- Input validation
- Swagger UI at `/docs`

## 🔧 Technologies
- Python, FastAPI, scikit-learn, joblib
- Docker
- curl / Swagger UI

## 📦 Setup

```bash
# Train model
python train_model.py

# Build Docker image
docker build -t  prayagraj55/basic_mlops_project.

# Run container
docker run -p 8000:8000 -d --name mlops-container prayagraj55/basic_mlops_project
