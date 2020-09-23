from flask import request

class UsersController:
    def __init__(self, base_data_base):
        self.db_wrapper = base_data_base

    def create_user(self):
        self.db_wrapper.create("users",request.json)
        return "user created"

    def delete_user(self):
        self.db_wrapper.delete("users",request.json)
        return "user deleted"
    