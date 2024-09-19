from flask import Flask
from pymongo import MongoClient
from app.routes.order import create_order_routes
from app.routes.warehouse import create_warehouse_routes
from app.routes.logistics import create_logistics_routes

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['appstates']

# Register Routes
app.register_blueprint(create_order_routes(db))
app.register_blueprint(create_warehouse_routes(db))
app.register_blueprint(create_logistics_routes(db))

if __name__ == '__main__':
    app.run(debug=True)