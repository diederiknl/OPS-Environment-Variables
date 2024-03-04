FROM python:3.7
WORKDIR /app
COPY . .
CMD ["python", "main.py"]
