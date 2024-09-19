from flask import Blueprint
from ..controllers.logistics import LogisticsController

def create_logistics_routes(db):
    logistics_bp = Blueprint('logistics', __name__)
    logistics = LogisticsController(db)

    @logistics_bp.route('/logistics/<id>', methods=['PUT'])
    def update_logistics(id):
        return logistics.update_logistics(id)

   
    return logistics_bp