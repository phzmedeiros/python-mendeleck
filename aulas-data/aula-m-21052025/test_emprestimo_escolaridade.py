import unittest
from emprestimo_escolaridade import verificar_emprestimo

class TestEmprestimoEscolaridade(unittest.TestCase):
    def test_inadimplente(self):
        self.assertEqual(verificar_emprestimo("João Silva", 30, 5000, "superior"), "inadimplente")

    def test_menor_baixa_escolaridade(self):
        self.assertEqual(
            verificar_emprestimo("Pedro", 16, 1500, "fundamental"),
            "menor de idade, baixa renda e escolaridade insuficiente"
        )

    def test_menor_baixa(self):
        self.assertEqual(verificar_emprestimo("Ana", 16, 1500, "superior"),
                         "menor de idade e baixa renda")

    def test_menor(self):
        self.assertEqual(verificar_emprestimo("Ana", 16, 5000, "superior"),
                         "menor de idade")

    def test_baixa(self):
        self.assertEqual(verificar_emprestimo("Beatriz", 25, 1500, "superior"),
                         "baixa renda")

    def test_escolaridade(self):
        self.assertEqual(verificar_emprestimo("Carla", 25, 5000, "fundamental"),
                         "escolaridade insuficiente")

    def test_elegivel(self):
        self.assertEqual(verificar_emprestimo("Pedro", 25, 5000, "superior"),
                         "elegível")

if __name__ == "__main__":
    unittest.main()