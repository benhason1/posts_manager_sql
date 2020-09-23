from flask import request


class PostsController:
    def __init__(self, base_data_base):
        self.db_wrapper = base_data_base

    def create_post(self):
        self.db_wrapper.create("posts", request.json)
        return "post created"

    def delete_post(self):
        self.db_wrapper.delete("posts", request.json)
        return "post deleted"

    def read_post(self, id):
        return self.db_wrapper.read("posts",id)