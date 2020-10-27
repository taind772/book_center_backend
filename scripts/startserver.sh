#!/bin/sh

python manage.py makemigrations document
python manage.py migrate --database=db
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'djangotestpw')" | python manage.py shell