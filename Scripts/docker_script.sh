docker rm -f my-container

docker build -t prayagraj55/basic_mlops_project .

docker run -d -p 8000:8000 --name my-container prayagraj55/basic_mlops_project

# docker push prayagraj55/basic_mlops_project

curl -X 'POST' \
'http://localhost:8000/predict' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
  "features": [52.1, 322.5, 32.4, 2.3]
}
'