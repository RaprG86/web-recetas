from  django.shortcuts import render

def registro(request):
    context={}
    return render(request,"usuarios/registro.html",context)