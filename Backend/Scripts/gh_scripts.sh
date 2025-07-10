docker pull ghcr.io/dsrathore1/iris-flower-classifier-api:latest

docker run -d -p 8000:8000 --name Iris-API-Contianer ghcr.io/dsrathore1/iris-flower-classifier-api:latest

curl -X 'POST' \
'http://localhost:8000/predict' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
  "features": [52.1, 322.5, 32.4, 2.3]
}
'