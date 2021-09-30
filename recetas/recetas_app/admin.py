from django.contrib import admin
from django.contrib.admin.decorators import register
from recetas_app.models.recetas import Receta,Ingrediente,Paso
# Register your models here.

class PasoInline(admin.TabularInline):
    model = Paso
    extra = 0
class IngredienteInline(admin.TabularInline):
    model = Ingrediente
    extra = 0


@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    inlines = [IngredienteInline, PasoInline]
    list_display = ['nombre', 'created_at']


