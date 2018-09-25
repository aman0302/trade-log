import sys, os

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.getcwd())+"\\trade-log")

from logger.utils.ExecutablePath import *
from logger.utils.Reporter import *
from logger.UI.UIAction import ui_action

logging.basicConfig(filename=get_log_file_name(), level=logging.INFO)

infoReport('################ SERVER STARTED ###############')

ui = ui_action()
ui.mainloop()
