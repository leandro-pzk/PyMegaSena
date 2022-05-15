from django.test import TestCase

from apps.home.forms import PalpiteArquivoForm, PalpiteForm

class FormTest(TestCase):

    def test_palpite_arquivo_form(self):

        form_data = {'something': 'something'}
        form = PalpiteArquivoForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_palpite_form(self):

        form_data = {'something': 'something'}
        form = PalpiteForm(data=form_data)
        
        self.assertFalse(form.is_valid())
