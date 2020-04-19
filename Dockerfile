FROM python:3.8.0
COPY . /app
WORKDIR /app
#"RUN apk add build-base"
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 80
CMD python ./app.py
