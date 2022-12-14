"""Ferme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from src import views, static 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('pwa.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('inicio/', views.Index, name="index"),
    path('', views.Ingreso, name="ingreso"),

    path('informes/productos', views.informe_productos, name="informe_productos"),
    path('informes/proveedores', views.informe_proveedores, name="informe_proveedores"),
    path('informes/pedidos', views.informe_pedidos, name="informe_pedidos"),
    path('informes/ventas', views.informe_ventas, name="informe_ventas"),
    path('informes/visitas', views.informe_visitas, name="informe_visitas"),
    path('informes', views.Seleccion_informe, name="informes"),
    path('dashboard', views.dashboard, name="dashboard"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)