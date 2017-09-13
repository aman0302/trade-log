import sys,os, logging

from logger.action.BrowserFactory import browser_factory
from logger.sources.SmallcaseSource import smallcase_source

sys.path.append(os.path.dirname(os.getcwd()))

from logger.utils.ExecutablePath import *


logging.basicConfig(filename=get_log_file_name(), level=logging.INFO)
logging.info('################ SERVER STARTED ###############')

smallcase = smallcase_source().start()