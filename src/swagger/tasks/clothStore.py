from swagger.libs import utils
import logging
from swagger.tasks.swagger import Swagger 
import sys

class clothStore(Swagger):

    def import_swagger_by_file(self, envVariables):
        try:
            utils.import_swagger(envVariables["swagger_name"],envVariables["api_gtw_id"],envVariables["swagger_parameters"],envVariables['region'])
            logging.info("The swagger file called {swagger_name} has been imported".format(swagger_name=envVariables["swagger_name"]))
            return True
        except Exception as e:
                logging.info('----- logging exception: {ex} ------'.format(ex = e))
                sys.exit(1)
