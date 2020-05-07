FROM python:3.8.0

########## ENV ##########
ENV FLASK_APP=app
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0

# System port to use
ENV PORT=80
ENV HOST=localhost

# Database
ENV DB_HOST=mongodb://<dbuser>:<dbuser-passwd>@irene-db:27017/test?authSource=admin


# Emails
ENV ENABLE_EMAIL=0 # Set to 1 to enable
ENV EMAIL_SENDER=<your-gmail-email-or-upr-email>
ENV EMAIL_PASSWD=<your-email-passwod>

ENV FLASK_SECRET_KEY=<your-secret>
ENV FLASK_SALT=<your-salt>


COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 80
CMD gunicorn --bind 0.0.0.0:80 app:app
