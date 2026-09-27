FROM python:3.11-slim

WORKDIR /code

# Copy and install dependencies
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the app directory into /code/app inside the container
COPY ./app /code/app

EXPOSE 8000

# Run Uvicorn pointing to main.py inside the app directory
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]