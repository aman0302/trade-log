import sys,os, logging
sys.path.append(os.path.dirname(os.getcwd()))

from logger.sources.SmallcaseSource import smallcase_source
from logger.utils.ExecutablePath import *


logging.basicConfig(filename=get_log_file_name(), level=logging.INFO)
logging.info('################ SERVER STARTED ###############')

smallcase = smallcase_source().start()