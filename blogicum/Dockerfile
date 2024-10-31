FROM python:3.12-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc 

WORKDIR /blogicum

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONBUFFERED 1
ENV PORT 8000
EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "127.0.0.1"]
CMD python3 manage.py runserver 127.0.0.1${PORT}