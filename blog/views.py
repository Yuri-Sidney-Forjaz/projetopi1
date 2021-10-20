from django.shortcuts import render
from Utils.decorator import login_required

@login_required
def home(request):
    
    context = {
        'usuario': request.user,
        'status': request.GET.get('status')
    }
    
    return render(request, 'home.html', context)

@login_required
def entidades(request):
    return render(request, 'entidades.html', {'usuario': request.session.get('usuario')})

@login_required
def sobre(request):
    return render(request, 'sobre.html', {'usuario': request.session.get('usuario')})

@login_required
def voluntario(request):
    return render(request, 'voluntario.html', {'usuario': request.session.get('usuario')})
