import unittest
from emprestimo import verificar_emprestimo
class TestClassificarIdade(unittest.TestCase):

    def test_menordeidade(self):
        self.assertEqual(verificar_emprestimo("Pedro", 12, 0), "menor de idade")
    
    def test_baixarenda(self):
        self.assertEqual(verificar_emprestimo("Lucas", 19, 1500), "baixa renda")
    
    def test_indadimplente(self):
        self.assertEqual(verificar_emprestimo("João Silva", 12, 0), "inadimplente")
    
    def test_menordeidadeebaixarenda(self):
        self.assertEqual(verificar_emprestimo("Pedro", 12, 0), "menor de idade e baixa renda")

    def test_elegivel(self):
        self.assertEqual(verificar_emprestimo("Ana", 25, 3000), "elegível")