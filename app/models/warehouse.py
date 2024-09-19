from pymongo import ReturnDocument

class Status:
    ORDER_PACKED = "ORDER_PACKED"
    ORDER_RECEIVED = "ORDER_RECEIVED"
    ORDER_PICKED = "ORDER_PICKED"
    ORDER_ON_HOLD = "ORDER_ON_HOLD"

class WarehouseModel:
    def __init__(self, db):
        self.status = Status()
        self.collection = db['warehouse']

    def create_warehouse(self, order_id, status):
        return self.collection.insert_one({"order_id": order_id, "status": status})
    
    def read(self, id):
        return self.collection.find_one({"_id": id})
    
    def update(self, id, status):
        return self.collection.find_one_and_update(
            {"_id": id}, {"$set": {"status": status}},return_document=ReturnDocument.AFTER
        )
    
