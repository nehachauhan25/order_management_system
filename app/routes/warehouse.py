from flask import Blueprint
from ..controllers.warehouse import WarehouseController

def create_warehouse_routes(db):
    warehouse_bp = Blueprint('warehouse', __name__)
    warehouse = WarehouseController(db)

    @warehouse_bp.route('/warehouse/<id>', methods=['PUT'])
    def update(id):
        return warehouse.update(id)

   
    return warehouse_bp