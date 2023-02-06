from flask import Flask, request, make_response
from flask_restx import Resource, Namespace
from database.database import Database

user = Namespace('user')

@user.route('')
class UserManagement(Resource):
    def get(self):
        # GET method 구현 부분
        db = Database()
        data = request.get_json()

        id = data['id']
        pw = data['pw']

        sql = "SELECT id, pw, nickname FROM taeukDB.user WHERE id = '" + id + "'"
        row = db.execute_one(sql)

        outnickname = row['nickname']
        outpw = row['pw']

        if (row is None):
            db.close()
            return {"message" : "아이디나 비밀번호 불일치"}
        else:
            if (outpw != pw):
                db.close()
                return {"message" : "아이디나 비밀번호 불일치"}
            else:
                return {"nickname" : outnickname}


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

            return {"is_success" : True, "message" : "유저생성성공"}

        else:
            db.close()

            return {"is_success" : False, "message" : "유저생성실패"}


    def put(self):
        # PUT method 구현 부분

        db = Database()

        data = request.get_json()

        id = data['id']
        pw = data['pw']
        nickname = data['nickname']

        sql = "SELECT id, pw FROM user WHERE id = '" + id + "'"
        
        row = db.execute_one(sql)
        print(row)
        outpw = row['pw']

        if (row is None):
            db.close()
            return {"is_success" : False, "message" : "유저닉네임변경실패"}
        else:
            if (outpw != pw):
                db.close()
                return {"is_success" : False, "message" : "유저닉네임변경실패"}
            else:
                sql = "UPDATE taeukDB.user SET nickname = '" + nickname + "' WHERE id = '" + id + "'"
                db.execute(sql)
                db.commit()
                db.close()

                return {"is_success" : True, "message" : "유저닉네임변경성공"}
    
    def delete(self):
        # DELETE method 구현 부분
        db = Database()

        data = request.get_json()

        id = data['id']
        pw = data['pw']

        sql = "SELECT id, pw FROM user WHERE id = '" + id + "'"
        
        row = db.execute_one(sql)
        print(row)
        outpw = row['pw']

        if (row is None):
            db.close()
            return {"is_success" : False, "message" : "유저삭제실패"}
        else:
            if (outpw != pw):
                db.close()
                return {"is_success" : False, "message" : "유저삭제실패"}
            else:
                sql = "DELETE FROM taeukDB.user WHERE id = '" + id + "'"
                db.execute(sql)
                db.commit()
                db.close()

                return {"is_success" : True, "message" : "유저삭제성공"}