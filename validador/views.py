# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import HttpResponseRedirect, HttpResponse
from models import TrabajosRealizados, \
                   EstructuraPoblacion, \
                   EstructuraActorSocial, \
                   EstructuraPersonas, \
                   EtapasTrabajos, \
                   C_MUNICIPIO, \
                   C_DEPENDENCIA, \
                   C_ENTIDAD, \
                   C_PROGRAMA_DGTIC
from validador.forms import nuevoTrabajoForm, nuevoRegistroActorSocial, nuevoRegistroPersona, nuevoRegistroPoblacion, selectDependenciaPoblacion


def municipios_json(request):
    lohmunicipioh = C_MUNICIPIO.objects.filter(CVE_ENT=27)
    print '-----------'
    print 'Queryset : '
    print lohmunicipioh

    lohmunicipioh_json = serializers.serialize('json', lohmunicipioh, fields=('CV_MUN','NO_MUN'))
    print '-----------'
    print 'JSON : '
    print lohmunicipioh_json
    print lohmunicipioh_json

    # muni = lohmunicipioh.values_list()
    # CV_MUN = models.CharField(max_length=3)
    # NO_MUN = models.CharField(max_length=255)
    # CVE_ENT = models.ForeignKey(C_ENTIDAD)

    return JsonResponse(lohmunicipioh_json, safe=False)

# Create your views here.
def homemain(request):
    usuario_actual = request.user
    actorestotal = EstructuraActorSocial.objects.filter(trabajo__Etapa__nombreEtapa='Cierre')
    personastotal = EstructuraPersonas.objects.filter(trabajo__Etapa__nombreEtapa='Cierre')
    poblaciontotal = EstructuraPoblacion.objects.filter(trabajo__Etapa__nombreEtapa='Cierre')
    userData = {
        'user': usuario_actual,
        'actorescount':actorestotal.count(),
        'personascount':personastotal.count(),
        'poblacioncount':poblaciontotal.count()
    }
    return render_to_response('homemain.html', userData, context_instance=RequestContext(request))

## Muestra los datos de poblacion
def showpoblacion(request):
    rmetodo = request.method
    dependencia = HttpResponse()
    nombredependencia = ''

    if rmetodo == 'POST':
        print rmetodo
        nombredependencia = C_DEPENDENCIA.objects.filter(pk=1).values_list('NB_DEPENDENCIA', flat=True)
        # print str(type (nombredependencia))
        print nombredependencia

    if rmetodo == 'GET':
        print rmetodo

    usuario_actual = request.user
    # UAdmin = usuario_actual.enlace.unidadAdministrativa
    # poblacion = EstructuraPoblacion.objects.filter(trabajo__Etapa__nombreEtapa='Cierre').order_by('CVE_MUN_id')
    # municipios = C_MUNICIPIO.objects.all()
    dependencias = selectDependenciaPoblacion
    # programas = C_PROGRAMA_DGTIC.objects.all()

    data = {
        'user': usuario_actual,
        #'unidadAdmin': UAdmin,
        #'poblacion': poblacion,
        #'municipios': municipios,
        'rmetodo': rmetodo,
        'nombredependencia': nombredependencia,
        'dependencias': dependencias,
        #'programas': programas,
        #'dependencia': dependencia
    }

    return render_to_response('showpoblacion.html', data, context_instance = RequestContext(request))


def showpobdependencia(request, dependencia_id):

    rmetodo = request.method
    nombredependencia = ''

    if rmetodo == 'POST':
        print rmetodo
        nombredependencia = C_DEPENDENCIA.objects.filter(pk=dependencia_id)

    data = {
        'user': usuario_actual,
        #'unidadAdmin': UAdmin,
        #'poblacion': poblacion,
        #'municipios': municipios,
        'dependencia': nombredependencia,
        #'programas': programas,
        #'dependencia': dependencia
    }

    return render_to_response('showpoblacion.html', data, context_instance=RequestContext(request))


## Muestra los datos de personas
def showpersonas(request):
    return render_to_response('showpoblacion.html', '', context_instance=RequestContext(request))


## Muestra los datos de actores
def showactores(request):
    return render_to_response('showpoblacion.html', '', context_instance=RequestContext(request))


@login_required()
def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        nuevo_trabajo = nuevoTrabajoForm(request.POST)
        # print nuevo_trabajo.is_bound
        # print nuevo_trabajo.is_valid()
        # print nuevo_trabajo.errors
        # check whether it's valid:
        if nuevo_trabajo.is_valid():
            print 'trabajo valido'
            # process the data in form.cleaned_data as required
            el_trabajo = nuevo_trabajo.save()
            # redirect to a new URL:
            return HttpResponseRedirect('home')
        # elif nuevo_trabajo.

    usuario_actual = request.user
    nombre = usuario_actual.first_name
    # print nombre
    correoe = usuario_actual.email
    # print  correoe
    UAdmin = usuario_actual.enlace.unidadAdministrativa
    # print UAdmin
    trabajos_pedientes = TrabajosRealizados.objects.filter(Usuario=usuario_actual)

    for e in trabajos_pedientes:
        if e.TipoPadron_id ==1 : # Actor Social
            registros = EstructuraActorSocial.objects.filter(trabajo=e.pk)
        elif e.TipoPadron_id == 2 : # Personas
            registros = EstructuraPersonas.objects.filter(trabajo=e.pk)
        elif e.TipoPadron_id == 3 : # Poblacion
            registros = EstructuraPoblacion.objects.filter(trabajo=e.pk)
        e.CantidadRegistros = registros.count()

    # print trabajos_pedientes.count()
    userData = {
        'user': usuario_actual,
        'unidadAdmin': UAdmin,
        'nuevoTrabajo': nuevoTrabajoForm(initial={'Usuario':usuario_actual, 'Etapa':3}),
        'pendientes': trabajos_pedientes,
        'total_pendientes': trabajos_pedientes.count(),
    }

    return render_to_response('home.html', userData, context_instance=RequestContext(request))


## No autorizado o 404
def no_autorizado(request):
    return render_to_response('no_autorizado.html')


## Borrar trabajo
@login_required()
def borrar(request, trabajo_id):
    trabajo = TrabajosRealizados.objects.get(pk=trabajo_id)
    if trabajo.Usuario == request.user:
        trabajo.delete()
    else:
        return HttpResponseRedirect('/noautorizado')

    return HttpResponseRedirect('/validador')


## Validacion
@login_required()
def validar(request, trabajo_id):
    usuario_actual = request.user
    UAdmin = usuario_actual.enlace.unidadAdministrativa
    # Abrir estatus del trabajo
    trabajo = TrabajosRealizados.objects.get(pk=trabajo_id)
    # El valor del numero de pagina en el paginador
    page = ''

    if trabajo.Usuario == request.user:
        tipopadronid = trabajo.TipoPadron_id  # obtengo el tipo de padron # print 'tipopadronid: ' + str(tipopadronid)
        anioejercicio = trabajo.AnioEjercicio  # obtengo el anio de ejercicio
        trimperiodoid = trabajo.Trimestre.identPeriodo  # obtengo el trimestre registrado
        Etapa = trabajo.Etapa_id

        if tipopadronid == 1 : # Actor Social
            registros = EstructuraActorSocial.objects.filter(trabajo=trabajo).order_by('pk')
        elif tipopadronid == 2 : # Personas
            registros = EstructuraPersonas.objects.filter(trabajo=trabajo).order_by('pk')
        elif tipopadronid == 3 : # Poblacion
            registros = EstructuraPoblacion.objects.filter(trabajo=trabajo).order_by('pk')

        trabajo.CantidadRegistros = registros.count()

        if request.method == 'POST':
            print request.method

        print registros

    else:
        return HttpResponseRedirect('/noautorizado')

    data = {
        'user': usuario_actual,
        'unidadAdmin': UAdmin,
        'trabajo': trabajo,
        'registros': registros
    }

    return render_to_response('validar.html', data, context_instance=RequestContext(request))


@login_required()
def validaragregar(request, trabajo_id):

    usuario_actual = request.user
    UAdmin = usuario_actual.enlace.unidadAdministrativa
    formulario = ''
    # Abrir estatus del trabajo
    trabajo = TrabajosRealizados.objects.get(pk=trabajo_id)
    print trabajo.TipoPadron

    if request.method == 'POST':
        print '-----'
        print trabajo.TipoPadron.nombrePadron
        print trabajo.TipoPadron.pk
        print request.POST
        if trabajo.TipoPadron.pk == 1:
            formulario = nuevoRegistroActorSocial(request.POST)
            print 'POST - Padron 1'
        elif trabajo.TipoPadron.pk == 2:
            formulario = nuevoRegistroPersona(request.POST)
            print 'POST - Padron 2'
        elif trabajo.TipoPadron.pk == 3:
            formulario = nuevoRegistroPoblacion(request.POST)
            print 'POST - Padron 3'

        print formulario

        if formulario.is_valid():
            print 'trabajo valido'
            formulario.cleaned_data
            print 'cleaned_data'
            # process the data in form.cleaned_data as required
            el_trabajo = formulario.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/validador/validar/'+str(trabajo.pk))


    elif request.method == 'GET':
        if trabajo.TipoPadron_id == 1:
            formulario = nuevoRegistroActorSocial( initial={'trabajo':trabajo_id, 'CD_DEPENDENCIA':UAdmin.pk} )
            print 'GET - Padron 1'
        elif trabajo.TipoPadron_id == 2:
            formulario = nuevoRegistroPersona( initial={'trabajo':trabajo_id, 'CD_DEPENDENCIA':UAdmin.pk} )
            print 'GET - Padron 2'
        elif trabajo.TipoPadron_id == 3:
            formulario = nuevoRegistroPoblacion( initial={'trabajo':trabajo_id, 'CD_DEPENDENCIA':UAdmin.pk} )
            print 'GET - Padron 3'

    # El valor del numero de pagina en el paginador
    page = ''

    data = {
        'user': usuario_actual,
        'unidadAdmin': UAdmin,
        'trabajo': trabajo,
        'formulario': formulario,
    }

    return render_to_response('validaragregar.html', data, context_instance=RequestContext(request))


@login_required()
def validarirarevision(request, trabajo_id):

    usuario_actual = request.user
    UAdmin = usuario_actual.enlace.unidadAdministrativa
    # Abrir estatus del trabajo
    trabajo = TrabajosRealizados.objects.get(pk=trabajo_id)

    trabajo.Etapa = EtapasTrabajos.objects.get(nombreEtapa="Registro")

    trabajo.save()

    mensaje = 'El trabajo del PUB con identificador <strong>'+ str(trabajo.pk) + '<strong> ha sido enviado a revision, el usuario es: <strong>' + str(trabajo.Usuario) + '</strong>, y pertenece a la dependencia <strong>' + str(trabajo.Usuario.enlace.unidadAdministrativa.NB_DEPEN_CORTO) + '</strong> '

    send_mail(
        'Un padrón ha sido enviado a Registro',
        mensaje,
        'emmanuel@origamienlinea.com',
        ['epalomeque@gmail.com'],
        fail_silently=False,
    )

    return HttpResponseRedirect( '/validador/validar/'+str(trabajo.pk) )


@login_required()
def validarverregistro(request, trabajo_id, idr):

    usuario_actual = request.user
    UAdmin = usuario_actual.enlace.unidadAdministrativa

    # Obtengo el tipo de trabajo
    trabajo = TrabajosRealizados.objects.get(pk=trabajo_id)

    # Obtengo el registro que estoy buscando y los nombres de los campos
    if trabajo.Usuario == request.user:
        tipopadronid = trabajo.TipoPadron_id  # obtengo el tipo de padron # print 'tipopadronid: ' + str(tipopadronid)

        if tipopadronid == 1: # Actor Social
            registros = EstructuraActorSocial.objects.filter(trabajo=trabajo).order_by('pk')
            campos = EstructuraActorSocial._meta.get_all_field_names
        elif tipopadronid == 2: # Personas
            registros = EstructuraPersonas.objects.filter(trabajo=trabajo).order_by('pk')
            campos = EstructuraPersonas._meta.get_all_field_names
        elif tipopadronid == 3: # Poblacion
            registros = EstructuraPoblacion.objects.filter(trabajo=trabajo).order_by('pk')
            campos = EstructuraPoblacion._meta.get_all_field_names

        record = registros.filter(pk=idr).values()
        # print record

    else:
        return HttpResponseRedirect('/noautorizado')


    data = {
        'user': usuario_actual,
        'unidadAdmin': UAdmin,
        'trabajo': trabajo,
        'record': record,
        'campos': campos
    }
    return render_to_response('veridr.html', data, context_instance=RequestContext(request))