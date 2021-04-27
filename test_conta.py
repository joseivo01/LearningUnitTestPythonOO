import unittest

from conta import Conta

class TestDatas(unittest.TestCase):
    def setUp(self):
        self.conta = Conta(1, "josé ivo", 300, 1000)
        self.conta_destino = Conta(2, "destinatario", 800, 2000)
    
    def test_extract(self):
        self.assertEqual(self.conta.extrato(),
                         "O titular: josé ivo possui um saldo de 300R$")
        
    def test_checkSafeMoney(self):
        self.conta.deposita(700)
        self.assertEqual(self.conta.get_saldo(), 1000)
        
    #verificar se o valor é realmente retirado, se houver saldo suficiente
    def test_checkWithdraw(self):
        valorDeSaque = 300
        self.conta.saca(valorDeSaque)
        self.assertEqual(self.conta.get_saldo(),0)
    
    def test_checkRecipient(self):
        valorDeTransferencia = 300
        self.conta.transfere(valorDeTransferencia, self.conta_destino)
        
    #Verificar que ao transderir o destino exista e se tem valor suficiente
    
    
    
    ###############   BAD WAY ############
    def test_checkWithdrawBadWay(self):
        valorDeSaque = 400
        with self.assertRaises(RuntimeError):
            self.conta.saca(valorDeSaque)
    
if __name__ == '__main__':
    unittest.main()