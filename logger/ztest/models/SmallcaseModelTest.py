from logger.models.SmallcaseModel import smallcase_model
import unittest as unittest

class SmallcaseMode_test(unittest.TestCase):

    def test_get_ordered_data(self):
        sm = smallcase_model('sm1', '100.56', 'Rs. 6,766.89', 'Rs. 56,57.78', '-56.56%', '-5656.78', '20Apr', 'rtrt')
        assert sm.name == "sm1"
