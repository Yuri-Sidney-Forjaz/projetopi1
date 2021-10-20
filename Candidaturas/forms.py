from django import forms
from .models import Candidatura

   # nome_completo = models.CharField(max_length=200)
   # idade = models.IntegerField()
   # escolaridade = models.CharField(max_length=30, choices=ESCOLARIDADE_CHOICE)
   # sobre = models.TextField(max_length=550)
    


class CandidaturaForm(forms.ModelForm):
    class Meta:
        model = Candidatura
        fields = '__all__'
        exclude = ['tipo']
        widgets = {
            'sobre': forms.Textarea(attrs={
                'placeholder': 'Qual sua formação e qual área profissional gostaria de se candidatar?'
            })
        }
        
    
    def clean_nome_completo(self):
        nome = self.cleaned_data['nome_completo']
        
        if len(nome) <= 6:
            raise forms.ValidationError('Nome completo incorreto.')
        
        return nome
    
    
    def clean_idade(self):
        idade = self.cleaned_data['idade']
        
        if idade < 18:
            raise forms.ValidationError('Você deve ter 18 anos')
        elif idade > 65:
            raise forms.ValidationError('Idade incorreta. Tente novamente...')
        
        return idade
    
    
        
    
    
    
