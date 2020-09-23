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



if __name__ == "__main__":
    main()
