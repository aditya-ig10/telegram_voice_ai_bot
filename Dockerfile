# Use full Debian base for all FFmpeg and build tools
FROM python:3.11-bullseye

# Install dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    pkg-config \
    build-essential \
    libavformat-dev \
    libavcodec-dev \
    libavdevice-dev \
    libavutil-dev \
    libavfilter-dev \
    libswscale-dev \
    libswresample-dev \
    && rm -rf /var/lib/apt/lists/*

# Ensure pkg-config can find .pc files
ENV PKG_CONFIG_PATH=/usr/lib/x86_64-linux-gnu/pkgconfig

# Set working directory
WORKDIR /app

# Copy code
COPY requirements.txt .
COPY voice_bot.py .

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Unbuffered logs
ENV PYTHONUNBUFFERED=1

# Start the bot
CMD ["python", "voice_bot.py"]
