from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from APIs.main import router as api_req_1
from APIs.model_req import router as api_req_2


app = FastAPI(
    title="Iris Flower Classifier API",
    description="🚀 Predict Iris species using a trained RandomForest model.",
    version="1.0.0",
)

app.include_router(api_req_1, prefix="/api")
app.include_router(api_req_2, prefix="/predict")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
