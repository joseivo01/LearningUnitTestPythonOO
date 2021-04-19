import unittest

from datetime import date
from datas import Datas

class TestDatas(unittest.TestCase):
    def setUp(self):
        self.atualDate = date.today()
        self.data_test = Datas(self.atualDate.day,
                          self.atualDate.month,
                          self.atualDate.year)
    def test_checkDateformated(self):
        self.assertEqual(self.data_test.formatada(),
                         'Data: {}/{}/{}'.format(self.atualDate.day,
                                                self.atualDate.month,
                                                self.atualDate.year))

if __name__ == '__main__':
    unittest.main()