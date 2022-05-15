from django.test import TestCase

from apps.home.models import Palpite, PalpiteArquivo

class TestModels(TestCase):

    def test_palpite_arquivo_creation(self):
        entry = PalpiteArquivo(palp_file="teste.txt", palp_file_nome="teste")
        self.assertEqual(entry.palp_file_nome, 'teste')

    def test_palpite_creation(self):
        file = PalpiteArquivo(palp_file="teste.txt", palp_file_nome="teste")
        entry = Palpite(palp_file=file, palp_dezenas="1,2,3,4,5,6")
        self.assertEqual(entry.palp_dezenas, "1,2,3,4,5,6")

