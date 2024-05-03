FROM python:3.12.3

WORKDIR /app

RUN pip install Flask

COPY . .

CMD [ "python", "-m" , "server.py", "run", "--host=0.0.0.0"]
