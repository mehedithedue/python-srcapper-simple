import logging
import time
from config.Constants import Constants
from controller.ScrapperController import ScrapperController

logging.basicConfig(filename='log/info.log', level=logging.INFO)

if __name__ == "__main__":
    '''
    Start the chrome browser
    '''
    webScrapperController = ScrapperController()
    const = Constants()
    webScrapperController.startBrowser()

    while True:

        try:

            webScrapperController.openUrl(const.SITE_URL)
            itemHtmlSpanList = webScrapperController.getItemList(const.ITEM_XPATH)

            if itemHtmlSpanList:
                # item html element found, now extract the item name and unit
                items = webScrapperController.extractItemFromList(itemHtmlSpanList)
                # store the item in mongo db
                if items: webScrapperController.storeItems(items)

            time.sleep(300)

        except Exception as e:
            logging.exception("Exception : ")
            webScrapperController.closeBroswer()
            raise e
