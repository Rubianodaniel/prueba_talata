FROM python:3

ENV PYTHONUNBUFFERED True
EXPOSE 5000

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install -r requirements.txt
RUN pip install gunicorn


CMD exec gunicorn --bind --workers 2 --threads 8 --timeout 0 main:app