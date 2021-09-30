from django.shortcuts import render

def contacto(request):
    context={}
    return render(request, "contacto.html",context)