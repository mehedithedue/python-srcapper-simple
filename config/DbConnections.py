import os
import pymongo


class DbConnections:

    def __init__(self):
        self.__connection = None

    def connect(self):
        if not self.__connection:
            self.__connection = pymongo.MongoClient(
                "mongodb+srv://" + os.getenv("DB_USERNAME") + ":" + os.getenv("DB_PASSWORD") + "@" + os.getenv(
                    'DB_HOST') + "/" + os.getenv('DB_COLLECTION'))
        return self.__connection
