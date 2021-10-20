from django.db import models

# Create your models here.

ESCOLARIDADE_CHOICE = [
    ('Ensino Fundamental', 'Ensino Fundamental'),
    ('Ensino Médio', 'Ensino Médio'),
    ('Ensino Superior', 'Ensino Superior'),
]

class Candidatura(models.Model):
    nome_completo = models.CharField(max_length=200)
    idade = models.IntegerField()
    contato = models.CharField(max_length=25)
    escolaridade = models.CharField(max_length=30, choices=ESCOLARIDADE_CHOICE)
    sobre = models.TextField(max_length=1000)
    tipo = models.TextField(max_length=50)
    
    def __str__(self):
        return f'{self.nome_completo} / {self.tipo}'
    
