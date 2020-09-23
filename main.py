import logging
from dynaconf import settings
from dal.databases.sql_database import SqlDataBase
from flask import Flask
from routes.posts.posts_controller import PostsController
from routes.posts.posts_route import PostsRoute

def main():
    logger = logging.getLogger()
    if settings.get("LOG_LEVEL") is None:
        log_level = "ERROR"
    else:
        log_level = settings.LOG_LEVEL

    logger.setLevel(log_level)

    db = SqlDataBase(logger)

    db.connect(settings.MYSQL_HOST, settings.MYSQL_USER,
               settings.MYSQL_PASSWORD, settings.MYSQL_DB_NAME
               )

    posts_ctrl = PostsController(db)
    posts_route = PostsRoute(posts_ctrl)

    app = Flask(__name__)
    app.register_blueprint(posts_route.blueprint)
    app.run()

if __name__ == "__main__":
    main()
