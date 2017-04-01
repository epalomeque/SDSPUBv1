"""padron_unico_sdstabasco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from validador import views

urlpatterns = [
    url(r'^soopadmin/', include(admin.site.urls)),
    # URLS de la aplicacion
    url(r'^$', views.homemain, name='homemain'),
    url(r'^poblacion/$', views.showpoblacion, name='poblacion'),
    url(r'^poblacion/(?P<dependencia_id>[0-9]+)$', views.showpoblacion, name='poblacion'),
    url(r'^personas/$', views.showpersonas, name='personas'),
    url(r'^actores/$', views.showactores, name='actores'),
    url(r'^validador$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^validador/home$', views.home, name='home'),
    url(r'^validador/validar/(?P<trabajo_id>[0-9]+)$', views.validar, name="validar"),
    url(r'^validador/validar/(?P<trabajo_id>[0-9]+)/agregar$', views.validaragregar, name="validaragregar"),
    url(r'^validador/validar/(?P<trabajo_id>[0-9]+)/irarevision$', views.validarirarevision, name="validarirarevision"),
    url(r'^validador/validar/(?P<trabajo_id>[0-9]+)/idr/(?P<idr>[0-9]+)$', views.validarverregistro, name="validarverregistro"),
    url(r'^validador/logout$', logout, {'next_page': '/validador'}, name='logout'),
    url(r'^validador/noautorizado$', views.no_autorizado, name='no_autorizado'),
    url(r'^validador/borrar/(?P<trabajo_id>[0-9]+)$', views.borrar, name="borrar"),
    url(r'^lohmunicipioh$', views.municipios_json, name="lohmunicipioh"),
]
