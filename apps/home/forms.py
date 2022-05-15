from django import forms

from apps.home.models import Palpite, PalpiteArquivo

class PalpiteArquivoForm(forms.ModelForm):
    class Meta:
        model = PalpiteArquivo
        exclude = ()
        
class PalpiteForm(forms.ModelForm):
    class Meta:
        model = Palpite
        exclude = ()
        widgets = {
            'palp_dt_criacao': forms.TextInput(attrs={'class': 'form-control'}),
            'palp_dezenas': forms.TextInput(attrs={'class': 'form-control'}),
            'palp_file': forms.Select(attrs={'class': 'form-control'}),
            
        }