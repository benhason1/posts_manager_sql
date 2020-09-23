import logging
from dynaconf import settings
from dal.databases.sql_database import SqlDataBase


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

    # db.delete("comments", {"ID":1})
    # db.create("admin_users_to_posts",{"post_id":11,"user_id":4})


    print(db.read("posts", "9"))

    # db.create("posts",{"content":"funny","creator_user_id":"4"})
    # db.create("users",{"username":"liran","password":"lll"})


if __name__ == "__main__":
    main()
