#!/bin/bash


if [ -z "$PORT" ]
then
    #echo "\$PORT is empty"
    PORT=8000
fi

echo "Running on port $PORT"
python manage.py runserver 0.0.0.0:$PORT