#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.extras import SelectDateWidget
from validador.models import TrabajosRealizados, EstructuraActorSocial, EstructuraPersonas, EstructuraPoblacion, C_DEPENDENCIA
# from consultaCatalogos.models import *
import os.path


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
    class Meta:
        model = EstructuraPersonas
        fields = '__all__'
        widgets = {
            'FH_LEVANTAMIENTO': forms.DateInput(attrs={'placeholder': 'aaaa-mm-dd'}),
            'FH_NACIMIENTO': forms.DateInput(attrs={'placeholder': 'aaaa-mm-dd'}),
            'FH_ALTA': forms.DateInput(attrs={'placeholder': 'aaaa-mm-dd'}),
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
        help_texts = {
            'CD_DEPENDENCIA': ('Some useful help text.'),
            'CD_INSTITUCION': ('Some useful help text.')
        }
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
