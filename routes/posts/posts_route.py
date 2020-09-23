from flask import Blueprint, request


class PostsRoute:
    def __init__(self, posts_controller):
        self.posts_ctrl = posts_controller
        self.blueprint = Blueprint("posts", __name__)
        self.blueprint.add_url_rule(
            "/posts", "create_post",self.posts_ctrl.create_post, methods=["POST"])
