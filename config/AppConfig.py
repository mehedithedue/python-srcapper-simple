import os
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()


class AppConfig:
    def __init__(self):
        self.driver = os.getenv("DRIVER_PATH")

    def appSetup(self):
        chrome_options = webdriver.ChromeOptions()
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
        chrome_options.add_argument(f'user-agent={user_agent}')
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument('--ignore-certificate-error_checks')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument('--log-level=OFF')
        chrome_options.add_argument('--lang=en-US,en')
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(executable_path=self.driver, options=chrome_options)

        driver.maximize_window()
        return driver
