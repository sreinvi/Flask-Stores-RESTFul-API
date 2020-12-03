from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        "username", 
        type=str, 
        required=True, 
        help="This field cannot be left blank!")

    parser.add_argument(
        "password", 
        type=str, 
        required=True, 
        help="This field cannot be left blank!")

    def post(self):
        data = UserRegister.parser.parse_args()

        #Check if user already taken
        if UserModel.find_by_username(data['username']):
            return {"message": f"User {data['username']} already taken."}, 409 # HTTP Conflict

        user = UserModel(**data)
        user.save_to_db()

        return {"message": f"User {data['username']} created successfully."}, 201 # HTTP Created