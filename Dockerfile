FROM python:3.8.0

########## ENV ##########
ENV FLASK_APP=app
ENV FLASK_ENV=development
ENV FLASK_DEBUG=0

# System port to use
ENV PORT=80
ENV HOST=localhost

# Database
ENV DB_NAME='IReNEdb'
ENV DB_HOST="mongodb://testuser:testpassword@irene-db:27017/?authSource=admin"

# Emails
ENV ENABLE_EMAIL=0 
ENV EMAIL_SENDER=irene.mock5@gmail.com
ENV EMAIL_PASSWD=icom@uprm

# Set to true for testing purpouses
ENV FLASK_SECRET_KEY=SomeVerySecretString
ENV FLASK_SALT=SomeVerySecretSalt


COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 80
CMD gunicorn --bind 0.0.0.0:80 app:app
