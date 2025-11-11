FROM python:3.11-slim

WORKDIR /app

ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src/
COPY data ./data/

EXPOSE 5000

# Start the uvicorn
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "5000"]
