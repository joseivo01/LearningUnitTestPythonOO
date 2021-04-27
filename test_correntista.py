import unittest


from correntista import Correntista
from conta import Conta

class TestClient(unittest.TestCase):
    
    def setUp(self):
        self.contaTest = Conta(12, "João", 0, 1000)
        self.correntista = Correntista("João", "012.457.800-75", self.contaTest)
    #testar se clinte não inicializa nullo
    def test_notNullCorrentista(self):
        self.assertIsNotNone(self.correntista)     
        
    def test_notNullConta(self):
        self.assertIsNotNone(self.correntista.getConta())
        
        
if __name__ == '__main__':
    unittest.main()