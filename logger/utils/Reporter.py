import logging
from logger.utils.Time import *

def infoReport(msg):
    logging.info(get_current_timestamp()+msg)
    print(get_current_timestamp()+msg)

def errorReport(msg):
    logging.error(get_current_timestamp()+msg)
    print(get_current_timestamp()+msg)

def debugReport(msg):
    logging.debug(get_current_timestamp()+msg)
    print(get_current_timestamp()+msg)