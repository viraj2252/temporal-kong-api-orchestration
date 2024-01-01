FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the entire project
COPY . /app/

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["python", "kong-trigger-service/app.py"]
