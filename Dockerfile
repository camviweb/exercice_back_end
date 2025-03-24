FROM python:3.9-slim

WORKDIR /api

COPY . /api

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=main.py
ENV FLASK_ENV=development 
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

CMD ["flask", "run"]


