from abc import ABC, abstractmethod

class Swagger(ABC):

  def __init__(self, swagger_name):
    self.swagger_name              = swagger_name
  
  @abstractmethod
  def import_swagger_by_file(self, results):
      pass
