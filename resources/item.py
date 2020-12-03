from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument("store_id",
        type=int,
        required=True,
        help="Every item need an store_id."
    )

    def get(self, name):
        item = ItemModel.findByName(name)
        if item:
            return item.json()
        return {"message": "Item not found."}, 404 # HTTP Not Found

    @jwt_required()
    def post(self, name):
        if ItemModel.findByName(name):
            return {"message": f"An item with the name {name} already exists."}

        json_data = Item.parser.parse_args()
        item = ItemModel(name, **json_data)
        try: 
            item.save_to_db()
        except: 
            return {"message": "An error ocurred inserting the item."}, 500 # HTTP Internal Error

        return item.json(), 201 # HTTP Created

    @jwt_required()
    def put(self, name):
        json_data = Item.parser.parse_args()

        item = ItemModel.findByName(name, json_data['store_id'])

        if item is None:
            item = ItemModel(name, **json_data)
        else:
            item.price = json_data['price']

        item.save_to_db()

        return item.json()

    @jwt_required()
    def delete(self, name):
        item = ItemModel.findByName(name)
        if item:
            item.delete_from_db()

        return {"message": "Item deleted"}
        

class ItemList(Resource):
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}
