from flask import jsonify, request
from ..services.logistics import LogisticsService
from bson import ObjectId

class LogisticsController:
    def __init__(self, db):
        self.logistics = LogisticsService(db)

   
    def update_logistics(self,id):
        data = request.json
        status = data['status']
        self.logistics.update_logistics(ObjectId(id), status)
        return jsonify({"message": "status updated"})

    