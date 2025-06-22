# Use a more complete base image
FROM python:3.11-bullseye

# Install system dependencies including FFmpeg and build tools
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libavformat-dev \
    libavcodec-dev \
    libavdevice-dev \
    libavutil-dev \
    libavfilter-dev \
    libswscale-dev \
    libswresample-dev \
    pkg-config \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and app code
COPY requirements.txt .
COPY voice_bot.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set Python to run unbuffered
ENV PYTHONUNBUFFERED=1

# Run the app
CMD ["python", "voice_bot.py"]
