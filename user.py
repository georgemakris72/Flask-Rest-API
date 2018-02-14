import sqlite3
from flask_restful import Resource,reqparse


class User:
    def __init__ (self,_id,username,password):
        self.id=_id,
        self.username=username,
        self.password=password

    @classmethod
    def find_by_username(cls,username):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        query="SELECT * FROM users WHERE username=?"
        print(username)
        result=cursor.execute(query, (username,))
        row=result.fetchone()
        if row:
            # user =cls(row[0],row[1],row[2])
            user=cls(*row)
        else:
            user=None


        connection.close()

        return user


    @classmethod
    def find_by_id(cls,_id):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        query="SELECT * FROM users WHERE id=?"
        # print(_id)
        # print("test by mo")
        result = cursor.execute(query, (_id[0],))
        row=result.fetchone()
        # print("test by mo 2")


        if row:
            # user =cls(row[0],row[1],row[2])
            user=cls(*row)
        else:
            user=None


        connection.close()

        return user


class UserRegister(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument('username',
    type=str, required=True, help="This field can't be blank.")

    parser.add_argument('password',
    type=str, required=True, help="This field can't be blank.")


    def post(self):
        data=UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message":"A user with that username already exists."},400


        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()



        query="INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()



        return {'message':'User Created successfully!'},201
