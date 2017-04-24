#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.extras import SelectDateWidget
from validador.models import TrabajosRealizados, EstructuraActorSocial, \
    EstructuraPersonas, EstructuraPoblacion, C_DEPENDENCIA, C_MUNICIPIO, C_LOCALIDAD
from validador.misfunciones import DeIterableADict

# from consultaCatalogos.models import *
import os.path


CAT_MUNICIPIOS = DeIterableADict(C_MUNICIPIO.objects.filter( CVE_ENT__CD_ENT=27 ).order_by('CV_MUN'),1,1)
# CAT_MUNICIPIOS = # .values('CVE_ENT__NB_ENT','NO_MUN')
print CAT_MUNICIPIOS

ANIOS = {1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917,1918,1919,
         1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937,1938,1939,
         1940,1941,1942,1943,1944,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,
         1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,
         1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,
         2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017}

MESES = {
    1:('Enero'), 2:('Febrero'), 3:('Marzo'), 4:('Abril'),
    5:('Mayo'), 6:('Junio'), 7:('Julio'), 8:('Agosto'),
    9:('Septiembre'), 10:('Octubre'), 11:('Noviembre'), 12:('Diciembre')
}
#print MESES

REGEX_CURP = r'^[A-Z]{1}[AEIOU]{1}[A-Z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM]{1}' \
             '(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)' \
             '[B-DF-HJ-NP-TV-Z]{3}[0-9A-Z]{1}[0-9]{1}$'

class nuevoTrabajoForm(ModelForm):
    class Meta:
        model = TrabajosRealizados
        fields = ['TipoPadron','AnioEjercicio','Trimestre', 'Etapa', 'Usuario']
        widgets = {
            'Etapa': forms.HiddenInput,
            'Usuario':forms.HiddenInput,
            'TipoPadron':forms.Select,
            'AnioEjercicio':forms.Select,
            'Trimestre':forms.Select,
        }


class nuevoRegistroPersona(ModelForm):
    CD_MUN_PAGO = forms.ModelChoiceField(
        queryset= C_MUNICIPIO.objects.filter( CVE_ENT__CD_ENT=27 ).order_by('CV_MUN'),
        label='Municipio de Pago',
        empty_label= u'----------',
        to_field_name= 'CV_MUN'
    )
    CD_LOC_PAGO = forms.ModelChoiceField(
        queryset= C_LOCALIDAD.objects.all().order_by('CVE_MUN_id'),
        label='Localidad de Pago',
        empty_label=u'----------'
    )
    CVE_MUN = forms.ModelChoiceField(
        queryset= C_MUNICIPIO.objects.filter( CVE_ENT__CD_ENT=27 ).order_by('CV_MUN'),
        label='Nombre del Municipio',
        empty_label= u'----------',
        to_field_name= 'CV_MUN'
    )
    CVE_LOC = forms.ModelChoiceField(
        queryset= C_LOCALIDAD.objects.all().order_by('CVE_MUN_id'),
        label='Nombre de la Localidad',
        empty_label=u'----------'
    )
    class Meta:
        model = EstructuraPersonas
        fields = (
            # Datos de la persona
            'ID_HOGAR', 'ID_PERSONA', 'NB_PRIMER_AP', 'NB_SEGUNDO_AP', 'NB_NOMBRE',
            'FH_NACIMIENTO', 'CD_SEXO', 'CD_EDO_NAC', 'NB_CURP', 'IN_HUELLA',
            'IN_IRIS', 'CD_EDO_CIVIL',
            # Datos de la institucion o padron
            'CD_INSTITUCION', 'CD_PADRON', 'CD_INTRAPROGRAMA', 'FH_ALTA',
            # Datos del beneficiario
            'CD_ESTATUS_BEN', 'CD_ESTATUS_HOG', 'CD_MUN_PAGO', 'CD_LOC_PAGO', 'NB_PERIODO_CORRES',
            'CD_TP_BENEFICIO', 'CD_TP_EXPEDICION', 'IN_TITULAR', 'CD_PARENTESCO', 'CD_TP_BEN_DET',
            'NU_BENEFICIOS', 'CD_BENEFICIO', 'NU_IMP_MONETARIO', 'NU_MES_PAGO', 'CD_MET_PAGO',
            'ID_AGRUPADOR', 'IN_CORRESP',
            # Datos del domicilio geografico
            'TIPOVIAL', 'NOMVIAL', 'CARRETERA', 'CAMINO', 'NUMEXTNUM1',
            'NUMEXTNUM2', 'NUMEXTALF1', 'NUMEXTANT', 'NUMINTNUM', 'NUMINTALF', 'TIPOASEN',
            'NOMASEN', 'CP', 'CVE_MUN', 'CVE_LOC', 'TIPOREF1', 'NOMREF1', 'TIPOREF2',
            'NOMREF2', 'TIPOREF3', 'NOMREF3', 'DESCRUBIC', 'AGEB', 'CLAVE_MZNA', 'LONGITUD', 'LATITUD',
            # Hidden Fields
            'CD_DEPENDENCIA', 'CD_ENT_PAGO', 'NOM_ENT','trabajo'
            )
        error_messages = {
            'ID_HOGAR': {'required': 'Este campo es obligatorio'},
            'ID_PERSONA': {'required': 'Este campo es obligatorio'},
            'NB_PRIMER_AP': {'required': 'Este campo es obligatorio'},
            'NB_SEGUNDO_AP': {'required': 'Este campo es obligatorio'},
            'NB_NOMBRE': {'required': 'Este campo es obligatorio'},
            'NB_CURP':  {'required': 'Este campo es obligatorio'},
            'FH_NACIMIENTO': {'required': 'Este campo es obligatorio'},
            'CD_SEXO': {'required': 'Este campo es obligatorio'},
            'CD_EDO_NAC': {'required': 'Este campo es obligatorio'},
            'CD_EDO_CIVIL': {'required': 'Este campo es obligatorio'},
            'IN_HUELLA': {'required': 'Este campo es obligatorio'},
            'IN_IRIS': {'required': 'Este campo es obligatorio'},
            'FH_ALTA': {'required': 'Este campo es obligatorio'},
        }
        labels = {
            'FH_ALTA':'Fecha de alta del beneficiario',
        }
        widgets = {
            'ID_HOGAR': forms.TextInput(attrs={'placeholder': '0000','required': True}),
            'NB_CURP': forms.TextInput(attrs={'placeholder': '0000','required': True}),
            'ID_PERSONA': forms.TextInput(attrs={'placeholder': '0000','required': True}),
            'NB_PRIMER_AP': forms.TextInput(attrs={'placeholder': 'PRIMER APELLIDO','required': True}),
            'NB_SEGUNDO_AP': forms.TextInput(attrs={'placeholder': 'SEGUNDO APELLIDO'}),
            'NB_NOMBRE': forms.TextInput(attrs={'placeholder': 'NOMBRE(S)','required': True}),
            'FH_NACIMIENTO': SelectDateWidget(attrs={'style':'display:inline; width:20%; min-width:90px','required': True},
                                            months = MESES, years = ANIOS),
            'CD_SEXO': forms.Select(attrs={'required': True}),
            'CD_EDO_NAC': forms.Select(attrs={'required': True}),
            'CD_EDO_CIVIL': forms.Select(attrs={'required': True}),
            'IN_HUELLA': forms.Select(attrs={'required': True}),
            'IN_IRIS': forms.Select(attrs={'required': True}),
            'FH_ALTA': SelectDateWidget(attrs={'style':'display:inline; width:20%; min-width:90px'},
                                        months=MESES, years=ANIOS),
            'NB_PERIODO_CORRES': forms.TextInput(attrs={'placeholder': 'AAM_AAM','required': True}),
            # Hidden widgets
            'CD_DEPENDENCIA': forms.HiddenInput,
            'CD_ENT_PAGO': forms.HiddenInput,
            'NOM_ENT': forms.HiddenInput,
            'trabajo': forms.HiddenInput
        }


class nuevoRegistroActorSocial(ModelForm):
    class Meta:
        model = EstructuraActorSocial
        fields = '__all__'
        widgets = {
            'FH_CONSTITUCION': forms.DateInput(attrs={'placeholder': 'aaaa-mm-dd'}),
            'FH_NACIMIENTO': forms.DateInput(attrs={'placeholder': 'aaaa-mm-dd'}),
            'FH_ALTA': forms.DateInput(attrs={'placeholder': 'aaaa-mm-dd'}),
            'trabajo': forms.HiddenInput
        }


class nuevoRegistroPoblacion (ModelForm):
    class Meta:
        model = EstructuraPoblacion
        fields = '__all__'
        error_messages = {
            'CD_DEPENDENCIA': {'required': 'Este campo es obligatorio'},
            'CD_INSTITUCION': {'required': 'Este campo es obligatorio'},
            'CD_PADRON': {'required': 'Este campo es obligatorio'},
            'CVEPROGRAMA': {'required': 'Este campo es obligatorio'},
            'CD_AP_SUBPROG': {'required': 'Este campo es obligatorio'},
            'CD_AP_DESCRIPCION': {'required': 'Este campo es obligatorio'},
            'NU_BENEFICIOS': {'required': 'Este campo es obligatorio'},
            'CD_AP_BENEFICIO_OBRA': {'required': 'Este campo es obligatorio'},
            'CD_AP_TP_BENEFICIARIO': {'required': 'Este campo es obligatorio'},
            'NU_BENEF': {'required': 'Este campo es obligatorio'},
            'NU_BENEF_HOM': {'required': 'Este campo es obligatorio'},
            'NU_BENEF_MUJ': {'required': 'Este campo es obligatorio'},
            'NU_VIVIENDAS': {'required': 'Este campo es obligatorio'},
            'CD_INTRAPROGRAMA': {'required': 'Este campo es obligatorio'},
            'CD_TP_INST_EJEC': {'required': 'Este campo es obligatorio'},
            'ID_EJECUTOR': {'required': 'Este campo es obligatorio'},
            'RFC_EJECUTOR': {'required': 'Este campo es obligatorio'},
            'CD_TP_MOD_EJEC': {'required': 'Este campo es obligatorio'},
            'ID_OBRA': {'required': 'Este campo es obligatorio'},
            'NB_OBRA': {'required': 'Este campo es obligatorio'},
            'NU_INV_TOT_EJE': {'required': 'Este campo es obligatorio'},
            'NU_INV_FED_EJE': {'required': 'Este campo es obligatorio'},
            'NU_INV_EST_EJE': {'required': 'Este campo es obligatorio'},
            'NU_INV_MUN_EJE': {'required': 'Este campo es obligatorio'},
            'NU_INV_OTRAS_EJE': {'required': 'Este campo es obligatorio'},
            'NB_INV_OTRAS_EJE': {'required': 'Este campo es obligatorio'},
            'FH_INICIO': {'required': 'Este campo es obligatorio'},
            'FH_TERMINO': {'required': 'Este campo es obligatorio'},
            'TIPO_INTERV': {'required': 'Este campo es obligatorio'},
            'TIPOVIAL': {'required': 'Este campo es obligatorio'},
            'NOMVIAL': {'required': 'Este campo es obligatorio'},
            'CARRETERA': {'required': 'Este campo es obligatorio'},
            'CAMINO': {'required': 'Este campo es obligatorio'},
            'NUMEXTNUM1': {'required': 'Este campo es obligatorio'},
            'NUMEXTNUM2': {'required': 'Este campo es obligatorio'},
            'NUMEXTALF1': {'required': 'Este campo es obligatorio'},
            'NUMEXTANT': {'required': 'Este campo es obligatorio'},
            'NUMINTNUM': {'required': 'Este campo es obligatorio'},
            'NUMINTALF': {'required': 'Este campo es obligatorio'},
            'TIPOASEN': {'required': 'Este campo es obligatorio'},
            'NOMASEN': {'required': 'Este campo es obligatorio'},
            'CP': {'required': 'Este campo es obligatorio'},
            'NOM_LOC': {'required': 'Este campo es obligatorio'},
            'NOM_MUN': {'required': 'Este campo es obligatorio'},
            'NOM_ENT': {'required': 'Este campo es obligatorio'},
            'TIPOREF1': {'required': 'Este campo es obligatorio'},
            'NOMREF1': {'required': 'Este campo es obligatorio'},
            'TIPOREF2': {'required': 'Este campo es obligatorio'},
            'NOMREF2': {'required': 'Este campo es obligatorio'},
            'TIPOREF3': {'required': 'Este campo es obligatorio'},
            'NOMREF3': {'required': 'Este campo es obligatorio'},
            'DESCRUBIC': {'required': 'Este campo es obligatorio'},
            'LONGITUD': {'required': 'Este campo es obligatorio'},
            'LATITUD': {'required': 'Este campo es obligatorio'}
        }
        widgets = {
            # 'CD_DEPENDENCIA': forms.DateInput(attrs={'class': 'col-xs-4'}),
            'FH_INICIO': forms.DateInput(attrs={'placeholder': 'aaaa-mm-dd'}),
            'FH_TERMINO': forms.DateInput(attrs={'placeholder': 'aaaa-mm-dd'}),
            'trabajo': forms.HiddenInput
        }


class selectDependenciaPoblacion(forms.Form):
    dependencia = forms.ModelChoiceField(queryset=C_DEPENDENCIA.objects.all(),
                                         empty_label='----------',
                                         label= 'Selecciona la dependencia',
                                         widget=forms.Select(attrs={'style':'width:100%'})
                                         )


class selectlocalidad(forms.Form):
    municipio = forms.ModelChoiceField(queryset=C_MUNICIPIO.objects.filter(CVE_ENT=27))
    localidad = forms.ChoiceField()
