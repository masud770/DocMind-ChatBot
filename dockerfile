# Python 3.11 slim base
FROM python:3.11-slim

WORKDIR /app

# Copy only necessary files
COPY requirements.txt .
COPY main.py .
COPY models.py .
COPY rag.py .
COPY utils.py .
COPY streamlit_app.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]