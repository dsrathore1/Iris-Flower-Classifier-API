from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel, Field, conlist
import logging, joblib, os

os.path.abspath("logs/app.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("logs/app.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

logger.info("Booting FastAPI app... 🔃")
model = joblib.load("model.joblib")
logger.info("Model loaded successfully...✔")

app = FastAPI(
    title="Iris Flower Classifier API",
    description="🚀 Predict Iris species using a trained RandomForest model.",
    version="1.0.0",
)


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


@app.get("/")
async def home():
    return {"message": "All running good!", "status": 200}


@app.post("/predict", tags=["Prediction"], summary="Predict Iris flower species")
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


"""
| Feature             | Description |
| ------------------- | ----------- |
| `sepal length (cm)` | feature[0] |
| `sepal width (cm)`  | feature[1] |
| `petal length (cm)` | feature[2] |
| `petal width (cm)`  | feature[3] |

| Class           | Label |
| --------------- | ----- |
| Iris Setosa     | `0`   |
| Iris Versicolor | `1`   |
| Iris Virginica  | `2`   |


"""
