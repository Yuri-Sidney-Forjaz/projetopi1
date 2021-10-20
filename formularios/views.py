from django.shortcuts import render

def apae(request):
    return render(request, 'formularios/apae.html')

def abbc(request):
    return render(request, 'formularios/abbc.html')
