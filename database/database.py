import pymysql
import configparser

config = configparser.ConfigParser()
config.read_file(open('config/config.ini'))

class Database:
    def __init__(self):
        self.db = pymysql.connect(
            host='43.201.112.59',
            user='taeuk',
            password='3862',
            db='taeukDB',
            port=3306,
            charset='utf8'
        )

        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def execute_one(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()    # fetchone()은 한번 호출에 하나의 Row 만을 가져올 때 사용된다.
        return row

    def execute_all(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()    # fetchall() 메서드는 모든 데이터를 한꺼번에 가져올 때 사용된다.
        return row

    def commit(self):
        self.db.commit()

    def close(self):
        self.cursor.close()