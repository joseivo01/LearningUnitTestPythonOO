import unittest


from cliente import Cliente

class TestClient(unittest.TestCase):
    
    def setUp(self):
        self.cliente = Cliente("João","0124578")
    #testar se clinte não inicializa nullo
    def test_notNullClientName(self):
        self.assertIsNotNone(self.cliente.get_nome())     
        
    def test_notNullClientCpf(self):
        self.assertIsNotNone(self.cliente.get_cpf())
        
        
if __name__ == '__main__':
    unittest.main()