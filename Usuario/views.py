from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import Usuario
from .forms import UsuarioCadastroForm, UsuarioLoginForm

# Create your views here.
def usuario_cadastro(request):
    form = UsuarioCadastroForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('Usuario:login')
    
    return render(request, 'Usuario/cadastro.html', {'form': form})


def usuario_login(request):
    
    form = UsuarioLoginForm(request.POST or None)
 
    context = {
        'form': form,
        'errorCredentials': False,
        'status': request.GET.get('status')
    }
    
    if form.is_valid():
        user = authenticate(
            request,
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        if user is not None:
            login(request, user)
            return redirect('Blog:home')
        
        context['errorCredentials'] = True
        
    return render(request, 'Usuario/login.html', context)
        
        
def usuario_logout(request):
    logout(request)
    return redirect('Usuario:login')