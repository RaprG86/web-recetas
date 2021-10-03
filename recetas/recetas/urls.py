"""recetas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from recetas_app.models.recetas import Receta
from recetas_app.views.recetas_views import receta
from recetas_app.views.home_views import home
from recetas_app.views.contacto_views import contacto
from recetas_app.views.usuarios.registro_views import registro, login, logout
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', home, name = 'home'),
    path('registro/', registro, name = 'registro'),
    path('contacto/', contacto, name = 'contacto'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),
    path('admin/', admin.site.urls),
    path('recetas/<slug:slug>$',receta, name = 'receta'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
