from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from validador.models import *
from validador.models import Enlace


# Register your models here.

## Extension del modelo de usuario
#Define un descriptor Inline para el modelo Enlace
class EnlaceInline(admin.StackedInline):
    model = Enlace
    can_delete = False
    verbose_name = 'enlace'

#Define un nuevo usuario Admin
class UserAdmin(BaseUserAdmin):
    inlines = (EnlaceInline,)

#Re-registrando el UserAdmin
admin.site.unregister(User)
admin.site.register(User,UserAdmin)


## Catalogos comunes
admin.site.register(C_DEPENDENCIA)
admin.site.register(C_ENTIDAD)
admin.site.register(C_INTRAPROGRAMAS)
admin.site.register(C_MET_PAGO)
admin.site.register(C_PADRON)
admin.site.register(C_PROGRAMA)
admin.site.register(C_TP_ASENTAMIENTO)
admin.site.register(C_TP_BENEFICIO)
admin.site.register(C_TP_VIALIDAD)
admin.site.register(C_UR)


## Catalogos de Actor Social


## Catalogos de Persona Fisica
admin.site.register(C_BENEFICIO)
admin.site.register(C_CORRESP)
admin.site.register(C_ESTATUS_BEN)
admin.site.register(C_ESTATUS_HOG)
admin.site.register(C_EDO_CIVIL)
admin.site.register(C_PARENTESCO)
admin.site.register(C_TP_BEN)
admin.site.register(C_TP_BEN_DET)
admin.site.register(C_TP_EXPEDICION)


## Catalogos de Poblacion Beneficiaria

# Cat monterrubio
admin.site.register(C_ADMIN)
admin.site.register(C_PROGRAMA_DGTIC)
admin.site.register(C_A_SUBPROG)
admin.site.register(C_AP_DESC)
admin.site.register(C_AP_BEN_OB)
admin.site.register(C_AP_PROG)
admin.site.register(C_STATUS)
admin.site.register(C_BENEFICIO_OB)
admin.site.register(C_TP_INSTANCIA)
admin.site.register(C_EJECUTOR)
admin.site.register(C_TP_INTERV)
admin.site.register(C_TIPO_EJEC)
admin.site.register(C_ACTIVIDADES)
admin.site.register(C_ID_GRUPO)
admin.site.register(C_TP_ACT_SOC)
admin.site.register(C_CARGO)
admin.site.register(C_BENEFICIO_AS)
admin.site.register(C_PERIODO)
admin.site.register(C_BENEFICIO_PROG)
admin.site.register(C_TP_BENEFICIO_PROG)
admin.site.register(C_TP_BEN_DET_PROG)
admin.site.register(C_BENEFICIO_AS_PROG)
admin.site.register(C_BENEFICIO_OB_PROG)
admin.site.register(C_MUNICIPIO)
admin.site.register(C_LOCALIDAD)

## Estructuras
admin.site.register(EstructuraPersonas)
admin.site.register(EstructuraActorSocial)
admin.site.register(EstructuraPoblacion)

##
admin.site.register(EtapasTrabajos)
admin.site.register(Cat_TipoPadron)
admin.site.register(Cat_AnioEjercicio)
admin.site.register(Cat_Periodos)
admin.site.register(TrabajosRealizados)