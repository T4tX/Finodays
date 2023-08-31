# Overview
This is Fast API 3.0 along with postgres database + adminer + db_init file to simplify database handling

This repository is part of my work on the Finodays2023 hackathon, where I had to develop a platform for working with digital financial assets.


# Build images
```
docker-compose build
```
# Run container
```
docker-compose up -d
```
# Stop container
```
docker-compose down
```
# INFO
## Postgres
dbname='postgres', user='postgres', password='postgres', host='localhost:5432'
## Adminer 
localhost:8080
## API
0.0.0.0:8000
0.0.0.0:8000/docs#/


