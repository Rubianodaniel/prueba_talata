FROM python:3

RUN mkdir -p /home/app
COPY . /home/app
RUN pip install -r requirements.txt
RUN pip install gunicorn

EXPOSE 3000

CMD ["python3", "/home/app/main.py" ]




#CMD exec gunicorn --bind --workers 2 --threads 8 --timeout 0 main:app