class RuleModel:
    def __init__(self, db):
        self.collection = db['ruleset']

    def find(self, warehouse_status):
        rule = self.collection.find_one({"warehouse_status": warehouse_status})
        if not rule:
            rule = self.collection.find_one({"warehouse_status": "*"})
        return rule