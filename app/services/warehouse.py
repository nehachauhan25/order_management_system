from ..models.warehouse import WarehouseModel
from ..models.order import OrderModel
from bson import ObjectId
from pymongo import ReturnDocument

class WarehouseService:
    def __init__(self, db):
        self.warehouse_model = WarehouseModel(db)
        self.order = OrderModel(db)
        self.status = self.warehouse_model.status
        self.order_status = self.order.status

    def update(self,id,status):
        doc = {"status": status}
        # warehouse = self.warehouse_model.find(ObjectId(id))
        warehouse = self.warehouse_model.update(id,doc)
        # debugger type of find -> document mongodb document -> update

        if(warehouse):
            warehouse_status = warehouse.get('status')
            order_id = warehouse.get('order_id') 
            order = self.order.find(order_id)
            # print(type(order))
            if warehouse_status == self.status.ORDER_PICKED:
                status = self.order_status.ORDER_SHIPPED
            elif warehouse_status == self.status.ORDER_ON_HOLD:
                status = self.order_status.ORDER_ON_HOLD
            elif warehouse_status == self.status.ORDER_OUT_OF_STOCK:
                status = self.order_status.ORDER_REFUNDED
            else :
                status = self.order_status.ORDER_PROCESSING
        
            update_query = {"status": status}
            return self.order.update(ObjectId(order_id) ,update_query)

    # def update(self, id, status):
    #     doc = {"status": status}
    #     updated_warehouse = self.warehouse_model.update(ObjectId(id), doc)
        
    #     return updated_warehouse
      