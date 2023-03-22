FROM python:3.9-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install psycopg2

COPY wsgi.py wsgi.py
COPY /blog ./blog

EXPOSE 5000

CMD ["python", "wsgi.py"]
