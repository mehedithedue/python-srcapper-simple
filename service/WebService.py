import logging
import time
from config.AppConfig import AppConfig


class WebService:
    def __init__(self):
        self.AppConfig = AppConfig()
        self.driver = None

    def appSetup(self):
        # initiate app
        self.driver = self.AppConfig.appSetup()

    def openUrl(self, url):
        # Open the URL
        self.driver.get(url)
        time.sleep(1)

    def findElementsByXpath(self, xpath):
        try:
            time.sleep(2)
            return self.driver.find_elements_by_xpath(xpath)
        except Exception as e:
            logging.exception(e)
            return None

    def getHtmlContent(self, container, xpath):
        # get the html content from xpath
        try:
            element = container.find_element_by_xpath(xpath)

            return element.get_attribute('innerHTML').strip()

        except Exception as e:
            logging.exception(e)
            return None

    def closeBrowser(self):
        self.__exit__()

    def __exit__(self):
        try:
            if self.driver is not None:
                self.driver.close()
                self.driver.quit()
        except Exception as e:
            print(e)
