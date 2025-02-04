from flask import Flask, request, make_response, jsonify
from flask_restx import Resource, Namespace
from database.database import Database

user = Namespace('user')

@user.route('',methods=['GET'])
class UserManagementGet(Resource):
    def get(self):
        # GET method 구현 부분
        db = Database()
        id = request.args.get('id')
        pw = request.args.get('password')

        sql = "SELECT id, pw, nickname FROM taeukDB.user WHERE id = '" + id + "'"
        row = db.execute_one(sql)
        

        if (row is None):
            db.close()
            return make_response(jsonify({"message" : "해당 유저가 존재하지 않음"}), 400)

        else:
            outnickname = row['nickname']
            outpw = row['pw']
            if (outpw != pw):
                db.close()
                return make_response(jsonify({"message" : "아이디나 비밀번호 불일치"}), 400)

            else:
                return make_response(jsonify({"nickname" : outnickname}), 200)



@user.route('')
class UserManagement(Resource):
    def post(self):
        db = Database()

        data = request.get_json()

        id = data['id']
        pw = data['password']
        nickname = data['nickname']

        sql = "SELECT * FROM user WHERE id = '" + id + "'"
        
        row = db.execute_one(sql)

        if (row is None):
            sql = "INSERT INTO user VALUES ('" + id + "', '" + pw + "', '" + nickname + "')"
            db.execute(sql)
            db.commit()
            db.close()

            return make_response(jsonify({"is_success" : True, "message" : "유저 생성 성공"}), 200)

        else:
            db.close()
            return make_response(jsonify({"is_success" : False, "message" : "이미 있는 유저"}), 400)



    def put(self):
        # PUT method 구현 부분

        db = Database()

        data = request.get_json()

        id = data['id']
        pw = data['password']
        nickname = data['nickname']

        sql = "SELECT id, pw, nickname FROM user WHERE id = '" + id + "'"
        
        row = db.execute_one(sql)

        if (row is None):
            db.close()
            return make_response(jsonify({"is_success" : False, "message" : "아이디나 비밀번호 불일치"}), 400)
        else:
            outnickname = row['nickname']
            outpw = row['pw']
            if (outpw != pw):
                db.close()
                return make_response(jsonify({"is_success" : False, "message" : "아이디나 비밀번호 불일치"}), 400)
            
            elif (outnickname == nickname):
                 return make_response(jsonify({"is_success" : False, "message" : "현재 닉네임과 같음"}), 400)
            
            else:
                sql = "UPDATE taeukDB.user SET nickname = '" + nickname + "' WHERE id = '" + id + "'"
                db.execute(sql)
                db.commit()
                db.close()

                return make_response(jsonify({"is_success" : True, "message" : "유저 닉네임 변경 성공"}), 200)

    
    def delete(self):
        # DELETE method 구현 부분
        db = Database()

        data = request.get_json()

        id = data['id']
        pw = data['password']

        sql = "SELECT id, pw FROM user WHERE id = '" + id + "'"
        
        row = db.execute_one(sql)
        

        if (row is None):
            db.close()
            return make_response(jsonify({"is_success" : False, "message" : "아이디나 비밀번호 불일치"}), 400)

        else:
            outpw = row['pw']
            if (outpw != pw):
                db.close()
                return make_response(jsonify({"is_success" : False, "message" : "아이디나 비밀번호 불일치"}), 400)
            else:
                sql = "DELETE FROM taeukDB.user WHERE id = '" + id + "'"
                db.execute(sql)
                db.commit()
                db.close()
                return make_response(jsonify({"is_success" : True, "message" : "유저 삭제 성공"}), 200)