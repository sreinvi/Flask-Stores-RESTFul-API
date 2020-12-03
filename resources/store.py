from db import db
from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.findByName()
        if store: 
            return store.json() 

        return {"message": "Store not found."}, 404 # HTTP Not Found

    def post(self, name):
        if StoreModel.findByName(name):
            return {"message": "Store already exists."}

        store = StoreModel(name)
        try: store.save_to_db()
        except: return {"message": "An error occurred while creating the store."}, 500 # HTTP Internal Server Error

        return store.json(), 201 # HTTP Created

    def delete(self, name):
        store = StoreModel.findByName(name)
        if store:
            store.delete_from_db()

        return {"message": "Store deleted."}

class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}