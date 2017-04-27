from logger.action.FileWriter import FileWriter
from logger.models.SmallcaseModel import SmallcaseModel


def test_file_insert():
    sm = SmallcaseModel(name='TEST_SM', index='107.45', investment='10000.00', value='1007989.00', pnl='-10.6%',
                        actual_pnl='-1982.78', bought_on='20 APril', timestamp='12:45:78 34/34/34')
    sm_list = []
    sm_list.append(sm)

    filewriter = FileWriter()
    filewriter.write(sm_list)

test_file_insert()