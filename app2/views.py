from django.shortcuts import render

def ofertas(request):
    return render(request, 'app2/ofertas.html')


def contacto(request):
    return render(request, 'app2/contacto.html')
