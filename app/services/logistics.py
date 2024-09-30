from ..models.logistics import LogisticsModel
from ..models.order import OrderModel
from bson import ObjectId

class LogisticsService:
    def __init__(self, db):
        self.logistics_model = LogisticsModel(db)
        self.order_model = OrderModel(db)
        self.status = self.logistics_model.status

    def update_logistics(self, id,status):
        updated_logistics = self.logistics_model.update(ObjectId(id), status)
        if(updated_logistics):
            self.upate_status(updated_logistics)
        return updated_logistics
        
    def upate_status(self, logistics):
        
        logistics_status = logistics.get('status')
        order_id = logistics.get('order_id') 

        if logistics_status == self.status.ORDER_AWAITING_PICKUP:
            status = "ORDER_PROCESSING"
        elif logistics_status == self.status.ORDER_IN_TRANSIT:
            status = "ORDER_SHIPPED"
        else :
            status = "ORDER_PROCESSING"
        
        update_query = {"status": status}
        return self.order_model.update(order_id, update_query)