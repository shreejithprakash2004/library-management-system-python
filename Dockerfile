FROM python:3.12-slim

WORKDIR /app

COPY LMS.py .
COPY list_of_books.txt .

CMD ["python", "LMS.py"]