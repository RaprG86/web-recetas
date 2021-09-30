from django.shortcuts import render
from recetas_app.models.recetas import Receta

def home(request):
    recetas = Receta.objects.all()
    context={
        'recetas': recetas
    }
    return render(request,'home.html',context)