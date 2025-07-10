FROM python:slim

WORKDIR /app

COPY requirements.txt .

RUN touch model.joblib

RUN pip install -r requirements.txt

COPY . .

RUN python train_model.py

EXPOSE 8000

CMD [ "uvicorn","app:app", "--host", "0.0.0.0", "--port", "8000", "--reload" ]