from pymongo import ReturnDocument

class Status:
    ORDER_RECEIVED = "ORDER_RECEIVED"
    ORDER_VERIFIED = "ORDER_VERIFIED"
    ORDER_PACKED = "ORDER_PACKED"
    ORDER_PICKED = "ORDER_PICKED"
    ORDER_ON_HOLD = "ORDER_ON_HOLD"
    ORDER_OUT_OF_STOCK = "ORDER_OUT_OF_STOCK"

class WarehouseModel:
    def __init__(self, db):
        self.status = Status()
        self.collection = db['warehouse']

    def create(self, order_id, status):
        return self.collection.insert_one({"order_id": order_id, "status": status})
    
    def find(self, id):
        return self.collection.find_one({"_id": id})
    
    def update(self, id, doc):
        return self.collection.find_one_and_update(
            {"_id": id}, {"$set": doc},return_document=ReturnDocument.AFTER
        )
    
    def delete(self, id):
        return self.collection.delete_one({"_id": id})
    
    
