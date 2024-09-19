from ..models.order import OrderModel
from ..models.warehouse import WarehouseModel
from ..models.logistics import LogisticsModel
from ..models.delivery import DeliveryModel
from bson import ObjectId

class OrderService:
    def __init__(self, db):
        self.order_model = OrderModel(db)
        self.warehouse_model = WarehouseModel(db)
        self.logistics_model = LogisticsModel(db)
        self.delivery_model = DeliveryModel(db)

    def calc_average_status(self, logistic_status, warehouse_status, delivery_status="Order Awaiting Out of delivery"):
        status = "Order Processing"
        if (warehouse_status == "Order Received" or warehouse_status == "Order Packed" or warehouse_status == "Order Verified") or (warehouse_status == "Order Picked" and logistic_status == "Order Awaiting Pickup"):
            status = "Order Processing"
        elif warehouse_status == "Order Picked":
            if logistic_status == "Order In Transit":
                status = "Order Shipped"
            elif logistic_status == "Order Delayed":
                status = "Order Processing"
            elif logistic_status == "Order Out for Delivery":
                if delivery_status == "Order Awaiting out of delivery":
                    status = "Order Out for Delivery"
                elif delivery_status == "Delivery Attempt Failed":
                    status = "Delivery Attempt Failed"
                elif delivery_status == "Order Delivered":
                    status = "Order Delivered"
                elif delivery_status == "Order Returned":
                    status = "Order Returned"
                elif delivery_status == "Order Refunded":
                    status = "Order Refunded"
                elif delivery_status == "Order Canceled":
                    status = "Order Canceled"
        elif warehouse_status == "Order On Hold":
            status = "Order On Hold"
        elif warehouse_status == "Order Out of stock":
            status = "Order Refunded"

        return status

    def create_order(self, product_name):
        order_id = self.order_model.create_order(product_name)
        self.warehouse_model.create_warehouse(order_id, "Order Received")
        self.logistics_model.create_logistics(order_id, "Order Awaiting Pickup")
        self.delivery_model.create_delivery(order_id, "Order Awaiting Out of delivery")
        return order_id

    def update_order_status(self, order_id, warehouse_status, logistic_status):
        order_status = self.calc_average_status(logistic_status, warehouse_status)
        self.warehouse_model.update_warehouse_status(order_id, warehouse_status)
        self.logistics_model.update_logistics_status(order_id, logistic_status)
        self.order_model.update_order_status(order_id, order_status)

    def get_orders(self):
        return self.order_model.get_orders()

    def delete_order(self, order_id):
        return self.order_model.delete_order(order_id)