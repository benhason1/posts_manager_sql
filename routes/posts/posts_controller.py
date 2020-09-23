from flask import request

class PostsController:
    def __init__(self, base_data_base):
        self.db_wrapper = base_data_base

    def create_post(self):
        self.db_wrapper.create("posts", request.json)
        return "post created"
