from flask import Blueprint, request


class UsersRoute:
    def __init__(self, users_controller):
        self.users_ctrl = users_controller
        self.blueprint = Blueprint("users", __name__)
        self.blueprint.add_url_rule(
            "/users", "create_user", self.users_ctrl.create_user, methods=["POST"])

        self.blueprint.add_url_rule(
            "/users", "delete_user", self.users_ctrl.delete_user, methods=["DELETE"])
