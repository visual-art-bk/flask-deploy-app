
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# 크롬 드라이버 설정 및 페이지 접근
CHROME_DRIVER_PATH = "/home/kbk/chromedriver-linux64/chromedriver"

def get_web_data(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # ChromeDriver 설정
    # service = Service("/usr/local/bin/chromedriver")  # Render에서 설정한 chromedriver 경로
    # service = Service(ChromeDriverManager().install())
    service = service = Service(executable_path=CHROME_DRIVER_PATH)
    
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(3)  # 페이지 로딩 대기

        # 원하는 데이터 추출
        title = driver.title
        body_text = driver.find_element(By.TAG_NAME, 'body').text

        return {"title": title, "body_text": body_text}
    finally:
        driver.quit()
