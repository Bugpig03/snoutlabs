FROM python:3.12.3

WORKDIR /app

RUN pip install Flask

COPY . .

EXPOSE 5001

CMD [ "python", "-m" , "server", "run", "--host=0.0.0.0"]
