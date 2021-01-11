FROM python:3.6-slim
RUN mkdir /proj
WORKDIR /proj
ADD . /proj
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0:8000