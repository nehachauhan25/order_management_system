from pymongo import MongoClient
from bson import ObjectId

class Status:
    ORDER_PLACED= "ORDER_PLACED" 
    ORDER_CONFIRMED= "ORDER_CONFIRMED" 
    ORDER_PROCESSING= "ORDER_PROCESSING" 
    ORDER_SHIPPED= "ORDER_SHIPPED" 
    OUT_FOR_DELIVERY= "OUT_FOR_DELIVERY" 
    ORDER_DELIVERED= "ORDER_DELIVERED" 
    ORDER_RETURNED= "ORDER_RETURNED" 
    ORDER_REFUNDED= "ORDER_REFUNDED" 
    ORDER_ON_HOLD= "ORDER_ON_HOLD" 
    ORDER_CANCELLED= "ORDER_CANCELLED" 
    DELIVERY_ATTEMPT_FAILED= "DELIVERY_ATTEMPT_FAILED" 
  

class OrderModel:
    def __init__(self, db):
        self.collection = db['order']
        self.status = Status()
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