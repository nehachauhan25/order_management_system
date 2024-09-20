from flask import jsonify, request
from ..services.warehouse import WarehouseService
from bson import ObjectId

class WarehouseController:
    def __init__(self, db):
        self.warehouse = WarehouseService(db)

   
    def update(self,id):
        data = request.json
        status = data['status']
        self.warehouse.update(ObjectId(id), status)
        return jsonify({"message": "status updated"})

    