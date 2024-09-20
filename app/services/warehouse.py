from ..models.warehouse import WarehouseModel
from ..models.order import OrderModel
from bson import ObjectId
from pymongo import ReturnDocument

class WarehouseService:
    def __init__(self, db):
        self.warehouse_model = WarehouseModel(db)
        self.order = OrderModel(db)
        self.status = self.warehouse_model.status
  
    # def update_option(self,id,status):
    #     doc = {"status": status}
    #     # warehouse = self.warehouse_model.find(ObjectId(id))
    #     warehouse = self.warehouse_model.update(id,doc)

    #     if(warehouse):
    #         warehouse_status = warehouse.get('status')
    #         order_id = warehouse.get('order_id') 
    #         order = self.order.find(order_id)

    #         if warehouse_status == self.status.ORDER_RECEIVED:
    #             status = "ORDER_PROCESSING"
    #         elif warehouse_status == self.status.ORDER_PICKED:
    #             status = "ORDER_SHIPPED"
    #         else :
    #             status = "ORDER_PROCESSING"
        
    #         update_query = {"status": status}
    #         return self.order.update(ObjectId(order_id) ,update_query)

    def update(self, id,status):
        doc = {"status": status}
        updated_warehouse = self.warehouse_model.update(ObjectId(id), doc)
        if(updated_warehouse):
            self.upate_status(id)
        return updated_warehouse
      

    def upate_status(self, id):
        
        warehouse = self.warehouse_model.find(id)
        warehouse_status = warehouse.get('status')

        order_id = warehouse.get('order_id') 
        # order = self.order.find(order_id)

        # if warehouse_status == self.status.ORDER_RECEIVED or warehouse_status == self.status.ORDER_VERIFIED or warehouse_status == self.status.ORDER_PACKED:
        #     status = "ORDER_PROCESSING"
        if warehouse_status == self.status.ORDER_PICKED:
            status = "ORDER_SHIPPED"
        elif warehouse_status == self.status.ORDER_OUT_OF_STOCK:
            status = "ORDER_OUT_OF_STOCK"
        elif warehouse_status == self.status.ORDER_ON_HOLD:
            status = "ORDER_ON_HOLD"
        else :
            status = "ORDER_PROCESSING"
        
        update_query = {"status": status}
        return self.order.update(order_id, update_query)