FROM python:3.9

WORKDIR /workspace

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    gnupg2 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libglib2.0-0 \
    libxrandr2 \
    libxss1 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libcups2 \
    libdbus-glib-1-2 \
    libxshmfence-dev \
    libgbm-dev

# Download and install Google Chrome specific version
RUN wget -O /tmp/google-chrome-stable_114.0.5735.198-1_amd64.deb https://dl.google.com/linux/deb/pool/main/g/google-chrome-stable/google-chrome-stable_114.0.5735.198-1_amd64.deb && \
    dpkg -i /tmp/google-chrome-stable_114.0.5735.198-1_amd64.deb || apt-get -f install -y

# Get latest ChromeDriver version
RUN LATEST_CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/$LATEST_CHROMEDRIVER_VERSION/chromedriver_linux64.zip" && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Install Python dependencies
RUN pip install --no-cache-dir selenium python-dotenv

# Set environment variables
ENV DISPLAY=:99

# Start Xvfb
CMD ["sh", "-c", "Xvfb :99 -ac & while true; do sleep 1000; done"]

ENV PYTHONUNBUFFERED=1
