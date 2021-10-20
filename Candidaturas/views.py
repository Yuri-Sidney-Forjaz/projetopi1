from django.shortcuts import render, redirect

from .models import Candidatura
from .forms import CandidaturaForm

# Create your views here.
def candidatura_criarApae(request):
    form = CandidaturaForm(request.POST or None)
    
    if form.is_valid():
        Candidatura.objects.create(
            nome_completo = form.cleaned_data['nome_completo'],
            idade = form.cleaned_data['idade'],
            contato = form.cleaned_data['contato'],
            escolaridade = form.cleaned_data['escolaridade'],
            sobre = form.cleaned_data['sobre'],
            tipo = 'APAE'
        )
       
        return redirect('/home?status=500')

    return render(request, 'formularios/apae.html', {'form': form})


def candidatura_criarAbbc(request):
    form = CandidaturaForm(request.POST or None)
    
    if form.is_valid():
        Candidatura.objects.create(
            nome_completo = form.cleaned_data['nome_completo'],
            idade = form.cleaned_data['idade'],
            contato = form.cleaned_data['contato'],
            escolaridade = form.cleaned_data['escolaridade'],
            sobre = form.cleaned_data['sobre'],
            tipo = 'ABBC'
        )
        return redirect('/home?status=500')

    return render(request, 'formularios/abbc.html', {'form': form})


def candidatura_detalhe(request, id):
    candidatura = Candidatura.objects.get(id=id)
    return render(request, 'Candidaturas/detalhe.html', {'candidatura': candidatura})



def candidatura_todas(request):
    return render(request, 'Candidaturas/todas.html', {'candidaturas': Candidatura.objects.all()})
