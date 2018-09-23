import sys, os

sys.path.append(os.path.dirname(os.getcwd()))

from logger.sources.EcomSource import ecom_source
from logger.utils.ExecutablePath import *
from logger.utils.Reporter import *

logging.basicConfig(filename=get_log_file_name(), level=logging.INFO)

infoReport('################ SERVER STARTED ###############')

ecom = ecom_source().start()
