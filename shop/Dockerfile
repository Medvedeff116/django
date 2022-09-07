FROM python:3.10-alpine
WORKDIR /projectpython
COPY requirements.txt /projectpython/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /projectpython/
ENV PYTHONUNBUFFERED 1
#ENV PATH /usr/local/bin:$PATH
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install djangorestframework
RUN pip install django-rest-swagger
RUN pip install install pyaml
RUN pip install django-cors-headers
#COPY . \C:\Users\Pasha\PycharmProjects\pythonProject1\projectpython\
#EXPOSE 8000
#CMD ["python", "manage.py", "runserver"]