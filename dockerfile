FROM python:3

RUN mkdir -p /home/app
COPY . /home/app
WORKDIR /home/app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

EXPOSE 3000

CMD ["python3", "/home/app/main.py" ]




#CMD exec gunicorn --bind --workers 2 --threads 8 --timeout 0 main:app