import sys,os, logging
sys.path.append(os.path.dirname(os.getcwd()))

from logger.sources.SmallcaseSource import smallcase_source
from logger.utils.ExecutablePath import *
from logger.utils.Reporter import *

logging.basicConfig(filename=get_log_file_name(), level=logging.INFO)

infoReport('################ SERVER STARTED ###############')

config = {}
config['sm_begin'] = 900
config['sm_end'] = 1530
config['sm_interval'] = 5
config['sm_sheet_name'] = 'trade-log1'
config['sm_pre_time'] = 845
config['sm_post_time'] = 1545

smallcase = smallcase_source(config=config).start()