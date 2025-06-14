FROM python:3.9-slim-bookworm

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

CMD ["fastapi", "run", "main.py", "--port", "80"]