FROM python:3.10-slim

WORKDIR /app

COPY temporal_workflows/requirements.txt .
RUN pip install -r requirements.txt

COPY temporal_workflows .

CMD ["python", "worker.py"]
