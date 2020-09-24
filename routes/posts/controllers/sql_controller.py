from .base_controller import BaseController
from flask import request, Response


class SqlController(BaseController):
    def __init__(self, base_data_base):
        self.db_wrapper = base_data_base

    def create_post(self):
        body = request.json
        try:
            post_details = body["post_details"]
            admin_users = body["admin_users"]

        except:
            return Response(response="bad body params", status=400)

        row_id = self.db_wrapper.create("posts", post_details)

        for admin_user in admin_users:
            self.db_wrapper.create("admin_users_to_posts", {
                                   "post_id": row_id, "user_id": admin_user})

        return "post created"

    def delete_post(self):
        self.db_wrapper.delete("posts", request.json)
        return "post deleted"

    def read_post(self, id):
        return self.db_wrapper.read("posts", id)

    def add_comments(self, id):
        body = request.json
        try:
            comments = body["comments"]
        except:
            return Response(response="no 'comments' key", status=400)

        for comment in comments:
            row_id = self.db_wrapper.create("comments", {"content": comment})
            self.db_wrapper.create("comments_to_posts", {
                                   "post_id": id, "comment_id": row_id})

        return "comments added"
