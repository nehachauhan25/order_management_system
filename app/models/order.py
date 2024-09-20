from pymongo import MongoClient
from bson import ObjectId

status = {
    "ORDER_PLACED": "ORDER_PLACED" ,
    "ORDER_RECEIVED": "ORDER_RECEIVED" ,
    "OUT_OF_DELIVERY": "OUT_OF_DELIVERY" 
  }

class OrderModel:
    def __init__(self, db):
        self.collection = db['order']
        self.status = status
    def create(self, product_name):
        return self.collection.insert_one({"product_name": product_name}).inserted_id

    def find(self, id):
        return self.collection.find_one({"_id":id})
    
    def update(self, id, update_query):
        return self.collection.update_one(
            {"_id": id}, {"$set": update_query}
        )

    def delete(self, order_id):
        return self.collection.find_one_and_delete({"_id": order_id})