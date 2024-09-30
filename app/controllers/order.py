from flask import jsonify, request
from ..services.order import OrderService
from bson import ObjectId

class OrderController:
    def __init__(self, db):
        self.order = OrderService(db)

    def create_order(self):
        product_name = request.json['product_name']
        order_id = self.order.create_order(product_name)
        return jsonify({"order_id": str(order_id), "message": "Order created successfully"})

    def update_order(self,order_id):
        data = request.json
        # order_id = data['order_id']
        warehouse_status = data['warehouse_status']
        logistic_status = data['logistic_status']
        delivery_status = data['delivery_status']
        # print(warehouse_status,logistic_status, order_id)
        self.order.update_order_status(ObjectId(order_id), warehouse_status, logistic_status)
        return jsonify({"message": "Order status updated"})

    def get_orders(self):
        orders = self.order.get_orders()
        orders_list = list(orders)

        for order in orders_list:
            if '_id' in order:
                order['_id'] = str(order['_id'])
            if 'delivery' in order:
                order['delivery'] = str(order['delivery'])
            if 'logistic' in order:
                order['logistic'] = str(order['logistic'])
            if 'warehouse' in order:
                order['warehouse'] = str(order['warehouse'])
    
        return {"order":orders_list}

    def delete_order(self, order_id):
        self.order.delete_order(order_id)
        return jsonify({"message": "Order deleted"})