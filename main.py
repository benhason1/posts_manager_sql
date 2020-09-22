import logging
from dynaconf import settings

def main():
    logger = logging.getLogger()
    if settings.get("LOG_LEVEL") is None:
        log_level = "ERROR"
    else:
        log_level = settings.LOG_LEVEL

    logger.setLevel(log_level)

if __name__ == "__main__":
    main()
