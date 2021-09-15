import os
from config.DbConnections import DbConnections


class BaseModel:
    def __init__(self):
        self.connection = DbConnections().connect()
        self.db = self.connection[os.getenv("DB_COLLECTION")]

