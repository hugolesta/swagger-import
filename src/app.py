import os
import logging
from swagger.tasks.swagger import Swagger
import time as ttime
import sys
import json
import importlib
import swagger.libs.utils as utils


logging.basicConfig(level=logging.INFO)

def swagger_factory(class_name):
    # swaggers should be created under this path (src/swaggers/tasks/swagger_files)
    module_name = "swagger.tasks." + class_name
    module = importlib.import_module(module_name)
    # the name of the class should match the name of the file
    class_ = getattr(module, class_name)
    instance = class_(class_name)
    return instance

def generate_swagger_by_name(envVariables):
        
    swagger = swagger_factory(envVariables["swagger_name"])

    if swagger is not None:

        swagger.import_swagger_by_file(envVariables)

        return True
    else:
        logging.error("Error! Unknown swagger name")
        return False

envVariables = {
    'swagger_name': os.environ.get('PROJECT_SWAGGER_NAME'),
    'api_gtw_id': os.environ.get('PROJECT_API_GTW_ID'),   
    'swagger_parameters': os.environ.get('PROJECT_SWAGGER_PARAMETERS'),
    'region' : os.environ.get('AWS_REGION'),
}

if __name__ == "__main__":
    #DECIDES WHAT SWAGGER NEEDS TO BE EXECUTED
    generate_swagger_by_name(envVariables)