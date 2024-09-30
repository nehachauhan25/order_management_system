from pymongo import ReturnDocument

class Status:
    ORDER_IN_TRANSIT = "ORDER_IN_TRANSIT"
    ORDER_AWAITING_PICKUP = "ORDER_AWAITING_PICKUP"
    ORDER_DELAYED = "ORDER_DELAYED"
    ORDER_OUT_FOR_DELIVERY = "ORDER_OUT_FOR_DELIVERY"


class LogisticsModel:
    def __init__(self, db):
        self.collection = db['logistics']
        self.status = Status

    def create_logistics(self, order_id, status):
        return self.collection.insert_one({"order_id": order_id, "status": status})

    def update(self, id, status):
        return self.collection.find_one_and_update(
            {"_id": id}, {"$set": {"status": status}},return_document=ReturnDocument.AFTER
        )