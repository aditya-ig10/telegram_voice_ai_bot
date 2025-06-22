FROM python:3.11-bullseye

# Prevent interactive prompts during install
ENV DEBIAN_FRONTEND=noninteractive

# Install FFmpeg & build dependencies
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
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Ensure pkg-config can find libraries
ENV PKG_CONFIG_PATH="/usr/lib/x86_64-linux-gnu/pkgconfig:/usr/share/pkgconfig"

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY voice_bot.py .

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Set unbuffered logs
ENV PYTHONUNBUFFERED=1

# Run the app
CMD ["python", "voice_bot.py"]
