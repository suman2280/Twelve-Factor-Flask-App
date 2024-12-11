FROM python:3.12-alpine

WORKDIR /twelve-factor-flask-app

COPY requirements.txt /twelve-factor-flask-app/

RUN pip install -r requirements.txt --no-cache-dir

COPY . /twelve-factor-flask-app/

EXPOSE 5000

CMD ["python", "app.py"]