from abc import ABC,abstractmethod

class BaseController(ABC):
    def __init__(self, base_data_base):
        self.db_wrapper = base_data_base

    @abstractmethod
    def create_post(self):
        pass

    @abstractmethod
    def delete_post(self):
        pass

    @abstractmethod
    def read_post(self,id):
        pass

    @abstractmethod
    def add_comments(self,id):
        pass
    
