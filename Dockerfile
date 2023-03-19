FROM python:3.10-windowsservercore-ltsc2022d

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache --user -r requirements.txt

COPY wsgi.py wsgi.py
COPY /blog ./blog

EXPOSE 5000

ENTRYPOINT flask run --host=0.0.0.0