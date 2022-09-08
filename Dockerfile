FROM python:3.7.1
LABEL author Brian Mafu(brianmafu@gmail.com)
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["sh", "/app/entrypoint.sh"]


