from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 크롬 드라이버 설정 및 페이지 접근
CHROME_DRIVER_PATH = "/home/kbk/chromedriver-linux64/chromedriver"


class WebDriverManager:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            # service = service = Service(executable_path=CHROME_DRIVER_PATH)
            service = Service(ChromeDriverManager().install())

            options = webdriver.ChromeOptions()
            # options.add_argument("--headless")  # 브라우저 GUI를 사용하지 않음
            # options.add_argument("--no-sandbox")
            # options.add_argument("--disable-dev-shm-usage")

            cls._driver = webdriver.Chrome(options=options, service=service)
        return cls._driver

    @classmethod
    def close_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
