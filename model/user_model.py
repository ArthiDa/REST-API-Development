import mysql.connector
import json


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
            return json.dumps(res)
        else:
            return "No Data Found"

    def user_addone_model(self, data):
        query = "INSERT INTO `users`(`name`, `email`, `phone`) VALUES (%s,%s,%s)"
        values = (data["name"], data["email"], data["phone"])
        self.cur.execute(query, values)
        return "User Created Successfully"

    def user_update_model(self, data, pk):
        query = (
            "UPDATE `users` SET `name` = %s, `email` = %s, `phone` = %s WHERE id = %s"
        )
        values = (data["name"], data["email"], data["phone"], pk)
        self.cur.execute(query, values)
        if self.cur.rowcount > 0:
            return "User Updated Successfully"
        else:
            return "Nothing to Update"

    def user_delete_model(self, pk):
        query = "DELETE FROM `users` WHERE id = %s"
        values = (pk,)
        self.cur.execute(query, values)
        if self.cur.rowcount > 0:
            return "User Deleted Successfully"
        else:
            return "User Not Found"
