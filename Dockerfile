# Python 이미지 설정
FROM python:3.8-slim

# Chrome 및 ChromeDriver 설치
RUN apt-get update && apt-get install -y wget gnupg unzip \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && wget -N https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && chmod +x chromedriver \
    && mv -f chromedriver /usr/local/bin/chromedriver

# 작업 디렉토리 설정
WORKDIR /app

# 종속성 복사 및 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# 소스 코드 복사
COPY . .

# 애플리케이션 시작
CMD ["gunicorn", "main:app"]
