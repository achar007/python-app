FROM python:3.13-alpine

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

COPY source /app

CMD python /app/app.py 
