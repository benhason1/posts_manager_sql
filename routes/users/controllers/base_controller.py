from abc import ABC,abstractmethod

class BaseController(ABC):
    def __init__(self, base_data_base):
        self.db_wrapper = base_data_base

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def delete_user(self):
        pass
