FROM python:3.11-slim

WORKDIR /app

COPY ./ /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "application.py", "--server.port=80", "--server.address=0.0.0.0"]
