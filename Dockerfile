FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
#RUN python manage.py migrate

#gunicorn
#CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]

#daphne
#CMD ["daphne", "-b", "0.0.0.0", "-p", "8001", "core.asgi:application"]