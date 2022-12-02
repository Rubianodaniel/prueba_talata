FROM python:3
ENV PYTHONUNBUFFERED=True

RUN mkdir -p /home/app
COPY . /home/app
WORKDIR /home/app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install Flask gunicorn

EXPOSE 5000

CMD exec gunicorn --bind :$PORT --workers 3 --threads 0 main:app



#CMD exec gunicorn --bind --workers 2 --threads 8 --timeout 0 main:app