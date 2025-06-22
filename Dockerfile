# Use Render’s official Python base image
FROM python:3.10-slim

# Install FFmpeg and pkg-config
RUN apt-get update && apt-get install -y \
    ffmpeg \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and code
COPY requirements.txt .
COPY voice_bot.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables (optional, will override with Render Dashboard)
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "voice_bot.py"]