from dal.databases.base_database import BaseDataBase


class SqlDataBase(BaseDataBase):
    def __init__(self):
        super().__init__()

    def connect(self, db_url):
        pass

    def create(self, table_name, object_to_create):
        pass

    def read(self, table_name, conditions, keys_to_get=None):
        pass

    def delete(self, table_name, conditions):
        pass

    def update(self, table_name, conditions, object_to_update):
        pass
