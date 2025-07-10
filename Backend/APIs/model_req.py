from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel, Field, conlist
import logging, joblib, os

log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "app.log")

os.path.abspath("/logs/app.log")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
)


logger = logging.getLogger(__name__)

logger.info("Booting FastAPI app... 🔃")
model = joblib.load("model.joblib")
logger.info("Model loaded successfully...✔")

router = APIRouter()


class Input(BaseModel):
    features: conlist(float, min_length=4, max_length=4) = Field(  # type: ignore
        ...,
        description="Four numerical values: sepal length, sepal width, petal length, petal width.",
        examples=[[5.1, 3.5, 1.4, 0.2]],
    )


class_labels = {
    0: "setosa",
    1: "versicolor",
    2: "verginica",
}


@router.post("/predict", tags=["Prediction"], summary="Predict Iris flower species")
def predict(data: Input = Body(...)):
    try:

        logger.info(f"Recieved input: {data.features}")
        prediction = model.predict([data.features])[0]

        label = class_labels[prediction]
        logger.info(f"Prediction label: {label}")

        return {"prediction": label}

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
