'''This file contains the main class for the example library/application'''

import logging
##Need to import the configuration file and associated functions... script automatically runs
import configure_logs

from ExampleModule import ExampleModule##An outside module, that will use same logger

class ExampleClass:
    def __init__(self, someExampleValue):
        ##Find log named logtime, in system and loads as logger
        self.logger = logging.getLogger("logtime")
        self.logger.debug('A bug here!')
        self.logger.info('Some info here...')
        self.logger.warning('Be warned!')
        self.logger.error('Oh no! An error.')
        self.logger.critical('Criticality incident')
        em = ExampleModule()
        em.runExample(' - my name is')

ec = ExampleClass('abcdefg')