from ..models.warehouse import WarehouseModel
from ..models.ruleset import RuleModel
from ..models.order import OrderModel
from bson import ObjectId
from pymongo import ReturnDocument
from json_logic import jsonLogic

class WarehouseService:
    def __init__(self, db):
        self.warehouse_model = WarehouseModel(db)
        self.rule_model = RuleModel(db)
        self.order = OrderModel(db)
        self.status = self.warehouse_model.status
        self.order_status = self.order.status

    def update(self,id,status):
        doc = {"status": status}
        # warehouse = self.warehouse_model.find(ObjectId(id))
        warehouse = self.warehouse_model.update(id,doc)

        if(warehouse):
            warehouse_status = warehouse.get('status')
            order_id = warehouse.get('order_id') 
            order = self.order.find(order_id)

            data = {
                "warehouse_status": warehouse_status,
                "order_status": order.get('status')
            }
            
            rules = [
                {
                    "conditions": {
                    "and": [
                        {
                        "===": [
                            {
                            "var": ["warehouse_status"]
                            },
                            "ORDER_ON_HOLD"
                        ]
                        },
                        {
                        "!==": [
                            {
                            "var": ["order_status"]
                            },
                            "ORDER_ON_HOLD"
                        ]
                        }
                    ]
                    },
                    "event": "ORDER_ON_HOLD"
                },
                {
                    "conditions": {
                    "and": [
                        {
                        "===": [
                            {
                            "var": ["warehouse_status"]
                            },
                            "ORDER_PICKED"
                        ]
                        },
                        {
                        "!==": [
                            {
                            "var": ["order_status"]
                            },
                            "ORDER_SHIPPED"
                        ]
                        },
                    ]
                    },
                    "event": "ORDER_SHIPPED"
                },
                {
                    "conditions": {
                    "and": [
                        {
                        "!==": [
                            {
                            "var": ["order_status"]
                            },
                            "ORDER_PROCESSING"
                        ]
                        },
                        {"or": [
                        {
                        "===": [
                            {
                            "var": ["warehouse_status"]
                            },
                            "ORDER_RECEIVED"
                        ]
                        },
                        {
                        "===": [
                            {
                            "var": ["warehouse_status"]
                            },
                            "ORDER_VERIFIED"
                        ]
                        },
                        {
                        "===": [
                            {
                            "var": ["warehouse_status"]
                            },
                            "ORDER_PACKED"
                        ]
                        }
                    ]}
                    ]
                    },
                    "event": "ORDER_PROCESSING"
                }
                ]
            
            for rule in rules:
                logic_rule = rule['conditions']
                condition = jsonLogic(logic_rule, data)
                if(condition):
                    event = rule.get("event")
                    update_query = {"status": event}
                    return self.order.update(ObjectId(order_id) ,update_query)
            
            return None


  