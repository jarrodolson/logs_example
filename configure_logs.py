'''This file shows how to configure logs, including a set of functions to modify the config'''

import logging
import logging.config

##debug_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

configDict = {
    'version': 1,##required
    'disable_existing_loggers': False,##False is best, True provides backward compatibility
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s: %(message)s - %(asctime)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',##For 'file-like objects... i.e. to screen
            'level': 'INFO',##Anything below this level will be ignored, depends on 'loggers['level']
            'formatter': 'simple',##referring to formatters
        },
    },
    'loggers': {
        'logtime': {##Called by name to load, using 'logging.getLogger('logtime')'
            'handlers': ['console'],##as many names from 'handlers' as desired
            'level': 'DEBUG',##First pass filter, if none set in 'handlers', this is only filter
        },
    },
}

def addFileLog(logLevel='WARNING', writemode='a'):
    fileConfig_handlers = {
        'class': 'logging.FileHandler',
        'level': logLevel,
        'filename': 'simpleTestLog.log',
        'mode': writemode,
        'formatter': 'verbose',
    }
    configDict['handlers']['file'] = fileConfig_handlers##Add to main dictionary handlers as 'file'
    configDict['loggers']['logtime']['handlers'].append('file')##Append to loggers set of handlers

addFileLog()##Adding to simple configuration
logging.config.dictConfig(configDict)
# logger = logging.getLogger('logtime')

# logger.debug('A bug here!')
# logger.info('Some info here...')
# logger.warning('Be warned!')
# logger.error('Oh no! An error.')
# logger.critical('Criticality incident')