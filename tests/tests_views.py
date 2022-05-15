from django.test import TestCase
from django.test import Client
from django.urls import reverse

class TestViews(TestCase):

    def test_call_view_deny_anonymous_index(self):
        response = self.client.get('', follow=True)
        self.assertRedirects(response, '/login/?next=/')

    def test_call_view_deny_anonymous_palpite(self):
        client = Client()
        response = client.get(reverse('ajax-palpite'))
        self.assertRedirects(response, '/login/?next=/importar/')
    
    def test_call_view_deny_anonymous_administrar(self):
        client = Client()
        response = client.get(reverse('adm'))
        self.assertRedirects(response, '/login/?next=/adm/')






