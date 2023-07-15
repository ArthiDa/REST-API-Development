import mysql.connector
import json
from flask import make_response


class user_model:
    def __init__(self):
        # Connections establishment
        try:
            self.conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="flask_api_test"
            )
            self.conn.autocommit = True
            self.cur = self.conn.cursor(dictionary=True)
        except Exception as e:
            print("An error occurred:", e)

    def user_getall_model(self):
        self.cur.execute("SELECT * From users")
        res = self.cur.fetchall()
        if len(res):
            resp = make_response({"payload":res}, 200)
            resp.headers['Access-Control-Allow-Origin'] = "*"
            return resp
        else:
            return make_response({"message":"No Data Found"}, 204)

    def user_addone_model(self, data):
        query = "INSERT INTO `users`(`name`, `email`, `phone`) VALUES (%s,%s,%s)"
        values = (data["name"], data["email"], data["phone"])
        self.cur.execute(query, values)
        return make_response({"message":"User Created Successfully"}, 201)

    def user_update_model(self, data, pk):
        query = (
            "UPDATE `users` SET `name` = %s, `email` = %s, `phone` = %s WHERE id = %s"
        )
        values = (data["name"], data["email"], data["phone"], pk)
        self.cur.execute(query, values)
        if self.cur.rowcount > 0:
            return make_response({"message":"User Updated Successfully"},201)
        else:
            return make_response({"message":"Nothing to Update"}, 202)

    def user_delete_model(self, pk):
        query = "DELETE FROM `users` WHERE id = %s"
        values = (pk,)
        self.cur.execute(query, values)
        if self.cur.rowcount > 0:
            return make_response({"message":"User Deleted Successfully"}, 200)
        else:
            return make_response({"message":"User Not Found"}, 204)

    def user_patch_model(self, data, pk):
        query = "UPDATE `users` SET "
        for key,value in data.items():
            query = query + f"{key}= '{value}', "
        query = query[:-2] + f" WHERE id={pk}"
        self.cur.execute(query)
        if self.cur.rowcount > 0:
            return make_response({"message":"User Updated Successfully"},201)
        else:
            return make_response({"message":"Nothing to Update"}, 202)