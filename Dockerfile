#stage 1 base image 
FROM python:3.12 AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

#stage 2 base image with small size

FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/

COPY . . 

ENTRYPOINT ["python","run.py"]


