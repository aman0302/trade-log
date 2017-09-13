from logger.models.SmallcaseModel import smallcase_model
from logger.action.GoogleSheet import googlesheet
from logger.utils.Time import *
import unittest


class googlesheet_test(unittest.TestCase):
    def test_stress(self):
        sm = smallcase_model(name='TEST_SM', index='107.45',
                             investment='10000.00', value='1007989.00',
                             pnl='-10.6%', actual_pnl='-1982.78',
                             bought_on='20 APril', timestamp='12:45:78 34/34/34')
        sm_list = []
        sm_list.append(sm)
        gs = googlesheet("trade-log1")

        for i in range(100):
            gs.insert_smallcase_data(sm_list)

    def test_sheet_creation(self):
        sm = smallcase_model(name=get_current_timestamp(), index='107.45',
                             investment='10000.00', value='1007989.00',
                             pnl='-10.6%', actual_pnl='-1982.78',
                             bought_on='20 APril', timestamp='12:45:78 34/34/34')

        sm_list = []
        sm_list.append(sm)
        gs = googlesheet("trade-log1")

        for i in range(100):
            gs.insert_smallcase_data(sm_list)
