# -*- coding: utf-8 -*-
import json
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
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
from models import TrabajosRealizados, EstructuraPoblacion, EstructuraActorSocial, \
                   EstructuraPersonas, EtapasTrabajos, C_MUNICIPIO, C_DEPENDENCIA, \
                   C_ENTIDAD, C_PROGRAMA_DGTIC, C_PROGRAMA
from validador.forms import nuevoTrabajoForm, nuevoRegistroActorSocial, nuevoRegistroPersona, nuevoRegistroPoblacion, selectDependenciaPoblacion


def municipios_json(request):
    lohmunicipioh = list(C_MUNICIPIO.objects.filter(CVE_ENT=27).values('CV_MUN', 'NO_MUN', 'CVE_ENT'))
    print '-----------'
    print 'Queryset : '
    print lohmunicipioh
    #muni = lohmunicipioh
    #print muni

    #lohmunicipioh_serializado = serializers.serialize('json', lohmunicipioh)

    #print '-----------'
    #print 'JSON : '
    #print lohmunicipioh_serializado
    # muni = lohmunicipioh_serializado


    return HttpResponse(json.dumps(lohmunicipioh))


def cprogsxpadron(tipopadron):
    count = C_PROGRAMA.objects.filter(TP_BENEFICIARIO=tipopadron).count()
    return count


# Devuelve lista de programas ordenadas por clave de programa
def lprogsxpadron(tipopadron):
    lista = C_PROGRAMA.objects.filter(TP_BENEFICIARIO=tipopadron).order_by('CD_PROGRAMA')
    return lista.values('NB_PROGRAMA','ANIO','CD_PROGRAMA')


# Devuelve lista de municipios en la entidad solicitada ordenadas por clave de municipio
def lmunicipios(entidad):
    lista = C_MUNICIPIO.objects.filter(CVE_ENT__CD_ENT=entidad).order_by('CV_MUN')
    return lista.values('NO_MUN','CV_MUN')


# Devuelve queryset de registros en etapa de cierre del padron solicitado
def qrecordsEtapaCierre(tipopadron):
    qrecords=''
    if tipopadron == 'AS':
        qrecords = EstructuraActorSocial.objects.filter(trabajo__Etapa__nombreEtapa='Cierre')
    elif tipopadron == 'PF':
        qrecords = EstructuraPersonas.objects.filter(trabajo__Etapa__nombreEtapa='Cierre')
    elif tipopadron == 'PB':
        qrecords = EstructuraPoblacion.objects.filter(trabajo__Etapa__nombreEtapa='Cierre')
    return qrecords


def qrecordsXmunicipio(tipopadron, mun, cd_padron=0):
    qrecords=''
    #print 'qrecordsXmunicipio('+str(tipopadron) + ', '+ str(mun)+', '+ str(cd_padron)+')'

    #print '**'
    #print 'INICIO qrecordsEtapaCierre(tipopadron)'
    #print qrecordsEtapaCierre(tipopadron)
    #print mun
    #print qrecordsEtapaCierre(tipopadron).filter(CD_ENT_PAGO__CD_ENT=27).filter(CD_MUN_PAGO__CV_MUN=mun)
    #print 'FIN qrecordsEtapaCierre(tipopadron)'
    #print '**'
    if tipopadron == 'AS' or tipopadron == 'PF':
        qrecords = qrecordsEtapaCierre(tipopadron).filter(CD_ENT_PAGO__CD_ENT=27).filter(CD_MUN_PAGO__CV_MUN=mun)
    elif tipopadron == 'PB':
        qrecords = qrecordsEtapaCierre(tipopadron).filter(NOM_MUN_CV_MUN=mun, NOM_ENT__CD_ENT=27)


    #print 'qrecords --' + str(qrecords)

    if cd_padron != 0:
        qrecordsxmun = qrecords.filter(CD_PADRON__CD_PROGRAMA__CD_PROGRAMA=cd_padron)
    else:
        qrecordsxmun = qrecords

    #print 'cd_padron: ' + str(cd_padron)
    #print qrecordsxmun

    return qrecordsxmun


def qrecordsXlocalidad (tipopadron, mun='000', loc='0000', cd_padron=0):
    qrecords=''
    if mun != '000' and loc != '0000':
        qrecords = qrecordsXmunicipio(tipopadron, mun, cd_padron).filter(CD_LOC_PAGO=loc)

    if cd_padron != 0:
        qrecordsxloc = qrecords.filter(CD_PADRON__CD_PROGRAMA=cd_padron)
    else:
        qrecordsxloc = qrecords

    return qrecordsxloc


# Devuelve un diccionario con cantidad de registro por programa del municipio solicitado
def registrosXmunicipio(tipopadron, mun):
    ListaProgramas= lprogsxpadron(tipopadron)
    # print '----- Inicia Lista de programas -----'
    # print ListaProgramas
    # print '----- Termina Lista de programas -----'
    tabla = {}

    print '----- registrosXmunicipio(' + str(tipopadron) + ', ' + str(mun) + ') -----'

    for prog in ListaProgramas:
        #print 'prog[NB_PROGRAMA]: ' + (prog['NB_PROGRAMA'])
        #print 'prog[CD_PROGRAMA]: ' + str(prog['CD_PROGRAMA'])
        tabla[prog['NB_PROGRAMA']] = qrecordsXmunicipio(tipopadron, mun, prog['CD_PROGRAMA']).count()

    #print 'tabla -----'
    print tabla

    return tabla


# Create your views here.
def homemain(request):
    usuario_actual = request.user

    userData = {
        'user': usuario_actual,
        'actorescount': qrecordsEtapaCierre('AS').count(),
        'personascount': qrecordsEtapaCierre('PF').count(),
        'poblacioncount': qrecordsEtapaCierre('PB').count(),
        'padronesAS': cprogsxpadron('AS'),
        'padronesPF': cprogsxpadron('PF'),
        'padronesPB': cprogsxpadron('PB')
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
        print qrecordsEtapaCierre('PB')
        print qrecordsXmunicipio('PB', mun='001')
        print lprogsxpadron('PB')


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
    usuario_actual = request.user

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
    rmetodo = request.method
    dependencia = HttpResponse()
    nombredependencia = ''
    regsXmunicipio = {}
    ListaMunicipios = lmunicipios(27)
    ListaProgramas = lprogsxpadron('PF')

    for muni in ListaMunicipios:
        #print '--'
        #print '----- Inicia ' + str(muni['NO_MUN']) + '-----'
        regsXmunicipio[muni['NO_MUN']] = registrosXmunicipio('PF', muni['CV_MUN'])
        #print '----- Termina ' + str(muni['NO_MUN']) + '-----'

    usuario_actual = request.user
    dependencias = selectDependenciaPoblacion

    data = {
        'user': usuario_actual,
        'listaprogs': ListaProgramas,
        'listamunicipios': ListaMunicipios,
        'registrosxmunicipio': regsXmunicipio,
        'rmetodo': rmetodo,
        'nombredependencia': nombredependencia,
        'dependencias': dependencias,
    }

    return render_to_response('showpoblacion.html', data, context_instance=RequestContext(request))


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


def NuevaInstanciaPadron(trabajo, UAdmin):
    if trabajo.TipoPadron_id == 1:
        formulario = nuevoRegistroActorSocial(
            initial={'trabajo': trabajo.pk, 'CD_DEPENDENCIA': UAdmin.pk}
            )
        print '(NuevaInstancia) - Padron 1'
    elif trabajo.TipoPadron_id == 2:
        formulario = nuevoRegistroPersona(
            initial={'trabajo': trabajo.pk, 'CD_DEPENDENCIA': UAdmin.pk, 'CD_ENT_PAGO': 27, 'NOM_ENT': 27}
            )
        print '(NuevaInstancia)  - Padron 2'
    elif trabajo.TipoPadron_id == 3:
        formulario = nuevoRegistroPoblacion(
            initial={'trabajo': trabajo.pk, 'CD_DEPENDENCIA': UAdmin.pk}
            )
        print '(NuevaInstancia) - Padron 3'
    return formulario


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
            if 'guarda' in request.POST:
                return HttpResponseRedirect('/validador/validar/'+str(trabajo.pk))
            elif 'guardayagrega' in request.POST:
                formulario = NuevaInstanciaPadron(trabajo, UAdmin)


    elif request.method == 'GET':
        formulario = NuevaInstanciaPadron(trabajo, UAdmin)

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


def reporte_cierre(request, trabajo_id):

    myimage = Image.open('static/assets/images/logo-SDS-cEscudo.png')


    ElTrabajo = TrabajosRealizados.objects.get(pk = trabajo_id)
    tipopadronid = ElTrabajo.TipoPadron_id

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'


    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    texto_inicio = 'Reporte de entrega de formato'
    IdTrabajo = 'Identificador del trabajo:' + str(ElTrabajo.pk)
    Dependencia = 'Dependencia a la que pertenece:' + ElTrabajo.Usuario.enlace.unidadAdministrativa.NB_DEPENDENCIA
    Persona = 'Persona que lo envia: ' + ElTrabajo.Usuario.first_name + ' ' + ElTrabajo.Usuario.last_name
    FechaEnvio = 'Fecha de envio: ' + str(ElTrabajo.UltimaActualizacion)
    TipoPadron = 'Tipo de Padron: ' + ElTrabajo.TipoPadron.nombrePadron
    Ejercicio = 'Ejercicio: ' + str(ElTrabajo.AnioEjercicio)
    Trimestre = 'Trimestre: ' + ElTrabajo.Trimestre.nombrePeriodo

    if tipopadronid == 1:  # Actor Social
        registros = EstructuraActorSocial.objects.filter(trabajo=trabajo_id).order_by('pk')
    elif tipopadronid == 2:  # Personas
        registros = EstructuraPersonas.objects.filter(trabajo=trabajo_id).order_by('pk')
    elif tipopadronid == 3:  # Poblacion
        registros = EstructuraPoblacion.objects.filter(trabajo=trabajo_id).order_by('pk')

    Registros = 'Cantidad de registros: ' + str(registros.count())

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    p.setPageSize(letter)

    p.drawString(50, 640, texto_inicio)
    p.drawString(50, 640, IdTrabajo)
    p.drawString(50, 620, Dependencia)
    p.drawString(50, 600, Persona)
    p.drawString(50, 580, FechaEnvio)
    p.drawString(50, 560, TipoPadron)
    p.drawString(50, 540, Ejercicio)
    p.drawString(50, 520, Trimestre)
    p.drawString(50, 500, Registros)
    p.drawInlineImage(myimage,50,710, 140, 50)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response