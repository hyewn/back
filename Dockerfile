FROM python:3.10

WORKDIR /app/

COPY . /app/

COPY static /app/static

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python main.py 