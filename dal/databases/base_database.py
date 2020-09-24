from abc import ABC, abstractmethod


class BaseDataBase(ABC):
    def __init__(self):
        self.connection = None

    @abstractmethod
    def connect(self, host, user, password, database):
        pass

    @abstractmethod
    def create(self, table_name, object_to_create):
        pass

    @abstractmethod
    def read(self, table_name, identifaction):
        pass

    @abstractmethod
    def delete(self, table_name, conditions):
        pass

    @abstractmethod
    def update(self, table_name, identifaction, updated_object):
        pass
