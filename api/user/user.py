from flask import Flask, request, make_response
from flask_restx import Resource, Namespace
from database.database import Database

user = Namespace('user')

@user.route('')
class UserManagement(Resource):
    def get(self):
        # GET method 구현 부분
        return {}

    def post(self):
        db = Database()

        data = request.get_json()

        id = data['id']
        pw = data['pw']
        nickname = data['nickname']

        sql = "SELECT * FROM user WHERE id = '" + id + "'"
        
        row = db.execute_one(sql)

        if (row is None):
            sql = "INSERT INTO user VALUES ('" + id + "', '" + pw + "', '" + nickname + "')"
            db.execute(sql)
            db.commit()
            db.close()

            return {"msg" : True, "code" : 200}

        else:
            db.close()

            return {"msg" : False, "code" : 500}
    def put(self):
        # PUT method 구현 부분
        return {}
    
    def delete(self):
        # DELETE method 구현 부분
        return {}