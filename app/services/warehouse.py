from ..models.warehouse import WarehouseModel
from ..models.order import OrderModel
from bson import ObjectId
from pymongo import ReturnDocument

class WarehouseService:
    def __init__(self, db):
        self.warehouse_model = WarehouseModel(db)
        self.order_model = OrderModel(db)
        self.status = self.warehouse_model.status

    def update_warehouse(self, id,status):
        updated_warehouse = self.warehouse_model.update(ObjectId(id), status)
        if(updated_warehouse):
            self.upate_status(updated_warehouse)
        return updated_warehouse
        
    def upate_status(self, warehouse):
        
        warehouse_status = warehouse.get('status')
        order_id = warehouse.get('order_id') 

        if warehouse_status == self.status.ORDER_RECEIVED:
            status = "ORDER_PROCESSING"
        elif warehouse_status == self.status.ORDER_PICKED:
            status = "ORDER_SHIPPED"
        # elif warehouse_status == self.status.ORDER_ON_HOLD_:
        #     status = "ORDER_ON_HOLD"
        else :
            status = "ORDER_PROCESSING"
        
        update_query = {"status": status}
        return self.order_model.update(order_id, update_query)