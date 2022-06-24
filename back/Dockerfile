FROM python:3
EXPOSE 8080
COPY . .
RUN pip install -r requirement.txt
RUN python3 manage.py migrate
RUN python3 manage.py migrate --run-syncdb
RUN python3 manage.py crontab add

# Start command, should be done in compose
#CMD python3 manage.py runserver 0.0.0.0:8080

# Seems useless
#RUN python3 manage.py migrate django_cron