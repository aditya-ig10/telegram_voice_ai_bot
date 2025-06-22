# Use a robust Python base image
FROM python:3.11-slim

# Install system dependencies, including FFmpeg and pkg-config
RUN apt-get update && apt-get install -y \
    ffmpeg \
    pkg-config \
    libavformat-dev \
    libavcodec-dev \
    libavdevice-dev \
    libavutil-dev \
    libavfilter-dev \
    libswscale-dev \
    libswresample-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and code
COPY requirements.txt .
COPY voice_bot.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Python
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "voice_bot.py"]