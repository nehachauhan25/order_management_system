from flask import Blueprint
from ..controllers.order import OrderController

def create_order_routes(db):
    order_bp = Blueprint('order', __name__)
    order = OrderController(db)

    @order_bp.route('/orders', methods=['POST'])
    def create_order():
        return order.create_order()

    @order_bp.route('/orders', methods=['GET'])
    def get_orders():
        return order.get_orders()

    @order_bp.route('/orders/<order_id>', methods=['PUT'])
    def update_order(order_id):
        return order.update_order(order_id)

    @order_bp.route('/orders/<order_id>', methods=['DELETE'])
    def delete_order(order_id):
        return order.delete_order(order_id)

    return order_bp