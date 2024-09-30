# from flask import Flask
# from pymongo import MongoClient
# from app.routes.warehouse import warehouse_blueprint

# app = Flask(__name__)

# # MongoDB connection
# client = MongoClient('mongodb://localhost:27017/')
# db = client['appstates']

# # Register the blueprint for routes
# app.register_blueprint(warehouse_blueprint)

# def create_app():
#     return app