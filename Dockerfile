# ==================================================
# Base Python image
# ==================================================

# Use official Python image.
# slim version reduces unnecessary packages.
FROM python:3.14-slim

# ==================================================
# Python runtime configuration
# ==================================================

# Prevent Python from creating .pyc files.
# This keeps the container filesystem cleaner.
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure Python logs appear immediately.
# Important for Docker logging.
ENV PYTHONUNBUFFERED=1

# ==================================================
# Application directory
# ==================================================

# All commands will run from /app
# inside the container.
WORKDIR /book_catalog_app

# ==================================================
# Install dependencies
# ==================================================

# Copy only requirements first.
# Docker caches this layer.
# If requirements.txt does not change,
# Docker does not reinstall packages.
COPY requirements.txt .


# Install Django and dependencies.
RUN pip install --no-cache-dir -r requirements.txt



# ==================================================
# Copy application code
# ==================================================

# Copy the Django project into the container.
COPY . .

# ==================================================
# Network configuration
# ==================================================

# Document that the application uses port 8000.
EXPOSE 8000

# ==================================================
# Container startup command
# ==================================================

# Start Django development server.
# 0.0.0.0 allows access from outside the container.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]