import datetime
import logging
import time

from model.Item import Item
from service.WebService import WebService


class ScrapperController:
    def __init__(self):
        self.webService = WebService()
        self.itemModel = None

    def startBrowser(self):
        self.webService.appSetup()

    def getItemList(self, xpath):
        try:
            return self.webService.findElementsByXpath(xpath)
        except Exception as e:
            return None

    def openUrl(self, url):
        self.webService.openUrl(url)
        time.sleep(1)

    def extractItemFromList(self, itemHtmlSpanList):
        """
        :param itemList: 
        :return: 
        """
        items = []
        try:
            for itemHtmlContent in itemHtmlSpanList:
                itemDictionary = self.extractInfoHtmlElement(itemHtmlContent)
                if itemDictionary is None : continue
                items.append(itemDictionary)
        except Exception as e:
            logging.exception(e)
        return items

    def extractInfoHtmlElement(self, itemSpanElement):
        try:
            itemName = self.webService.getHtmlContent(itemSpanElement, 'span[contains(@class, "bold")]').replace(':', '')
            itemAmount = self.webService.getHtmlContent(itemSpanElement, 'span[contains(@class, "line-item-bold")]')

            created = datetime.datetime.now()
            itemUnitList = itemAmount.split()
            amount = itemUnitList[0]
            unit = itemUnitList[1]

            if (not itemName or not amount) :
                raise ValueError("No data in content ")
            return {"item": itemName, "amount": amount, "unit": unit, "created": created}

        except Exception as e:
            logging.exception(e)
            return None
        
    def storeItems(self, items):
        Item().store(items)

    def closeBroswer(self):
        self.webService.closeBrowser()
