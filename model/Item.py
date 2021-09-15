from model.BaseModel import BaseModel


class Item(BaseModel):

    def __init__(self):
        super().__init__()
        self.collection = self.db.items

    def store(self, collections):
        return self.collection.insert(collections)
