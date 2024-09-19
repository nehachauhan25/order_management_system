class DeliveryModel:
    def __init__(self, db):
        self.collection = db['delivery']

    def create_delivery(self, order_id, status):
        return self.collection.insert_one({"order_id": order_id, "status": status})

    def update_delivery_status(self, order_id, status):
        return self.collection.find_one_and_update(
            {"order_id": order_id}, {"$set": {"status": status}}
        )