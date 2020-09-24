from flask import Blueprint, request


class PostsRoute:
    def __init__(self, base_posts_controller):
        self.posts_ctrl = base_posts_controller
        self.blueprint = Blueprint("posts", __name__)
        self.blueprint.add_url_rule(
            "/posts", "create_post",self.posts_ctrl.create_post, methods=["POST"])

        self.blueprint.add_url_rule(
            "/posts", "delete_post",self.posts_ctrl.delete_post, methods=["DELETE"])

        self.blueprint.add_url_rule(
            "/posts/<id>", "read_post",self.posts_ctrl.read_post, methods=["GET"])

        self.blueprint.add_url_rule(
            "/posts/<id>/comments", "add_comments",self.posts_ctrl.add_comments, methods=["POST"])