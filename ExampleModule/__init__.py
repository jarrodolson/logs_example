'''This file contains a single class and function that does logging'''
import logging

class ExampleModule:
    def __init__(self):
        self.logger = logging.getLogger('logtime')##Sets up logger object
    
    def runExample(self, argument):
        self.logger.debug('A debugging message' + argument)
        self.logger.info('An information message' + argument)
        self.logger.warning('A warning message' + argument)
        self.logger.error('An error message' + argument)
        self.logger.critical('A critical message' + argument)