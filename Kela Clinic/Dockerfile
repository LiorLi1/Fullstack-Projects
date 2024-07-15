#Heroku Docker file

FROM python:3.7

WORKDIR /app
ADD requirements.txt /app

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install django==2.1.15 && \
    pip install django_jenkins && \ 
    pip install requests && \
    pip install selenium && \
    pip install chromedriver_py && \
    pip install mysql

ADD . /app

ENTRYPOINT ["sh","/app/entrypoint.sh"]