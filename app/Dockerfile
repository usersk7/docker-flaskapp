FROM python:3.6

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
RUN mkdir static
RUN mkdir templates
COPY static /app/static
COPY templates /app/templates
COPY app.py /app
CMD python app.py
