from logger.models.SmallcaseModel import SmallcaseModel
from logger.action.GoogleSheet import GoogleSheet
from logger.utils.Time import *


def stress_test():
    sm = SmallcaseModel(name='TEST_SM', index='107.45', investment='10000.00', value='1007989.00', pnl='-10.6%',
                        actual_pnl='-1982.78', bought_on='20 APril', timestamp='12:45:78 34/34/34')
    sm_list = []
    sm_list.append(sm)
    gs = GoogleSheet()

    for i in range(100):
        gs.insert_data(sm_list)


def sheet_creation_test():
    sm = SmallcaseModel(name=get_current_timestamp(), index='107.45', investment='10000.00', value='1007989.00',
                        pnl='-10.6%',
                        actual_pnl='-1982.78', bought_on='20 APril', timestamp='12:45:78 34/34/34')

    sm_list = []
    sm_list.append(sm)
    gs = GoogleSheet()

    for i in range(100):
        gs.insert_data(sm_list)

