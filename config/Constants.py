import os

class Constants:
    def __init__(self):
        self.SITE_URL = os.getenv("SITE_URL")
        self.ITEM_XPATH = '//div[@class="critical-product-marquee-container"]//div[@class="marquee-text-text"][1]/span/span'



