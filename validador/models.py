# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# from validators import FileValidator

# Create your models here.
SINO_CHOICES = (
    ('', '------'),
    ('1', 'Sí'),
    ('0', 'No'),
)

HM_CHOICES = (
    ('', '------'),
    ('H', 'Hombre'),
    ('M', 'Mujer'),
)

NBORIG_CHOICES = (
    ('', '------'),
    ('FED', 'Federal'),
    ('EST', 'Estatal'),
    ('MUN', 'Municipal'),
    ('PRIV', 'Privada'),
)


# Extendiendo el modelo de usuario
class Enlace(models.Model):
    user = models.OneToOneField(User)
    unidadAdministrativa = models.ForeignKey('C_DEPENDENCIA')


# Catálogos

# Tipo de Padrón
class Cat_TipoPadron(models.Model):
    nombrePadron = models.CharField(max_length=15)

    def __unicode__(self):
        return '%s | %s' % (self.pk, self.nombrePadron)


# Año de ejercicio
class Cat_AnioEjercicio(models.Model):
    AnioEjercicio = models.CharField(max_length=4, default='')

    def __unicode__(self):  # __str__ en Python 3
        return self.AnioEjercicio


# Catalogo de periodos
class Cat_Periodos(models.Model):
    identPeriodo = models.CharField(max_length=2)
    nombrePeriodo = models.CharField(max_length=20)
    # mes = models.ManyToManyField(Cat_Mes)

    def __unicode__(self):
        return '%s | %s' % (self.identPeriodo, self.nombrePeriodo)


# Catálogo para identificar de que Estado proviene la información.
class C_ADMIN(models.Model):
    ID_ADMIN = models.IntegerField()
    CD_ADMIN = models.IntegerField()
    NB_ADMIN = models.CharField(max_length=60)
    PERIODO = models.CharField(max_length=9)

    def __unicode__(self):
        return '%s | %s' % (self.ID_ADMIN, self.NB_ADMIN)


# Catálogo de Dependencias (TODOS) SIIPPG.
class C_DEPENDENCIA(models.Model):
    NB_ORIGEN = models.CharField(max_length=12, choices=NBORIG_CHOICES)
    CD_DEPENDENCIA = models.IntegerField()
    CD_DEPENDENCIA_OFICAL = models.IntegerField()
    ID_ADMIN = models.CharField(max_length=2, blank=True) #models.ForeignKey('C_ADMIN', blank=True)
    NB_DEPENDENCIA = models.CharField(max_length=150, default="")
    NB_DEPEN_CORTO = models.CharField(max_length=15)
    SECTOR = models.CharField(max_length=25)
    LAST = models.CharField(max_length=5, blank=True)

    def __unicode__(self):
        return '%s | %s' % (self.NB_DEPEN_CORTO, self.NB_DEPENDENCIA)


# Catálogo de las unidades administrativa responsables de operar programas (TODOS).
class C_UR(models.Model):
    CD_INSTITUCION = models.CharField(max_length=60)
    CD_DEPENDENCIA = models.IntegerField()
    CD_U_R = models.CharField(max_length=20)
    CD_U_R_OFICIAL = models.CharField(max_length=20)
    ID_ADMIN = models.IntegerField()
    NB_UR = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s | %s | %s' % (self.CD_INSTITUCION, self.CD_DEPENDENCIA, self.CD_U_R)


# Catálogo de tipos de subprograma  o proyecto que se genere de un programa (TODOS).
class C_INTRAPROGRAMAS(models.Model):
    CD_INTRAPROGRAMA = models.IntegerField()
    CVE_INTRAPROGRAMA = models.IntegerField(blank=True)
    NB_INTRAPROGRAMA = models.CharField(max_length=150)
    TP_INTRAPROGRAMA = models.CharField(max_length=60, blank=True)
    NB_DEPENDENCIA = models.CharField(max_length=60, blank=True)
    NB_UR = models.CharField(max_length=60, blank=True)
    NB_PROGRAMA = models.CharField(max_length=60, blank=True)

    def __unicode__(self):
        return '%s | %s' % (self.CD_INTRAPROGRAMA, self.NB_INTRAPROGRAMA)


# Catálogo del Tipo de vialidad (TODOS) INEGI.
class C_TP_VIALIDAD(models.Model):
    CD_TIPO_VIALIDAD = models.IntegerField()
    NB_TIPO_VIALIDAD = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s' % ( self.NB_TIPO_VIALIDAD )


# Catálogo del Tipo de asentamiento humano (TODOS) INEGI.
class C_TP_ASENTAMIENTO(models.Model):
    CD_TIPO_ASENTAMIENTO = models.IntegerField()
    NB_TIPO_ASENTAMIENTO = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s' % (self.NB_TIPO_ASENTAMIENTO)


# Catálogo de entidades de nacimiento (TODOS) INEGI, RENAPO.
class C_ENTIDAD(models.Model):
    CD_ENT = models.IntegerField()
    NB_ENTIDAD = models.CharField(max_length=60)
    CD_ENT_RENAPO = models.CharField(max_length=60)
    NB_ENT = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s | %s' % ( self.CD_ENT, self.NB_ENTIDAD )


class C_MUNICIPIO(models.Model):
    CV_MUN = models.CharField(max_length=3)
    NO_MUN = models.CharField(max_length=255)
    CVE_ENT = models.ForeignKey(C_ENTIDAD)

    def __unicode__(self):
        return '%s | %s ' % (self.CVE_ENT.NB_ENT, self.NO_MUN)


class C_LOCALIDAD(models.Model):
    CV_LOC = models.IntegerField()
    NO_LOC = models.CharField(max_length=255)
    CVE_MUN = models.ForeignKey(C_MUNICIPIO)

    def __unicode__(self):
        return '%s | %s | %s' % (self.CVE_MUN_id, self.CV_LOC, self.NO_LOC)


# Catálogo de Programa Social (PB) AP.
class C_PROGRAMA_DGTIC(models.Model):
    CVEPROGRAMA = models.IntegerField()
    C_PROGRAMA = models.IntegerField()
    CVE_PROGRAMA = models.CharField(max_length=60)
    NB_PROGRAMA = models.CharField(max_length=150)
    FH_INICIO = models.DateField()  # Fecha

    def __unicode__(self):
        return '%s' % (self.NB_PROGRAMA)


# Catálogo del Subprograma que pertenece al Programa Social (PB) AP.
class C_A_SUBPROG(models.Model):
    CD_AP_SUBPROG = models.IntegerField()
    C_SUBPROGRAMA = models.IntegerField()
    CVE_SUBPROGRAMA = models.CharField(max_length=5)
    C_PROGRAMA = models.IntegerField()
    CVE_PROGRAMA = models.CharField(max_length=60)
    NB_AP_SUBPROG = models.CharField(max_length=120)
    FH_INICIO = models.DateField()  # Fecha

    def __unicode__(self):
        return '%s' % (self.NB_AP_SUBPROG)


# Catálogo de la descripción al que pertenece el subprograma : Inciso (PB) AP.
class C_AP_DESC(models.Model):
    CD_AP_DESCRIPCION = models.IntegerField()
    C_ISUBPROGRAMA = models.IntegerField()
    CVE_ISUBPROGRAMA = models.CharField(max_length=60)
    C_SUBPROGRAMA = models.IntegerField()
    CVE_SUBPROGRAMA = models.IntegerField()
    CVE_PROGRAMA = models.CharField(max_length=60)
    NB_ISUBPROGRAMA = models.CharField(max_length=255)
    FH_INICIO = models.DateField()  # Fecha

    def __unicode__(self):
        return '%s | %s' % (self.CD_AP_DESCRIPCION, self.NB_ISUBPROGRAMA)
        #return '%s' % (self.NB_ISUBPROGRAMA)


# Catálogo del tipo de beneficio entregado a los poblaciones beneficiarias (PB) AP.
class C_AP_BEN_OB(models.Model):
    CD_AP_BENEFICIO_OBRA = models.IntegerField()
    C_UNIDAD_MEDIDA = models.IntegerField()
    CVE_UNIDAD_MEDIDA = models.CharField(max_length=60)
    NB_UNIDAD_MEDIDA = models.CharField(max_length=60)
    FH_INICIO = models.DateField()  # Fecha

    def __unicode__(self):
        return '%s | %s' % (self.CD_AP_BENEFICIO_OBRA, self.NB_UNIDAD_MEDIDA)


# Catálogo del tipo de beneficiario del programa (PB). AP
class C_AP_PROG(models.Model):
    CD_AP_TP_BENEFICIARIO = models.IntegerField()
    NB_AP_TP_BENEFICIARIO = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s' % (self.NB_AP_TP_BENEFICIARIO)


# Catálogo del Estatus que tiene la obra al concluir el proyecto (PB).
# Aplica a padrones de periodo no mayor a 2012.
class C_STATUS(models.Model):
    CD_STATUS_OB = models.IntegerField()
    NB_STATUS_OB = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s' % (self.NB_STATUS_OB)


# Catálogo de las descripciones de los beneficios entregados (PB). Aplica a padrones de periodo no mayor a 2012.
class C_BENEFICIO_OB(models.Model):
    CD_BENEFICIO_OB = models.IntegerField()
    NB_BENEFICIO_OB = models.CharField(max_length=120)

    def __unicode__(self):
        return '%s' % (self.NB_BENEFICIO_OB)


# Catálogo del Tipo de instancia ejecutora (PB).
class C_TP_INSTANCIA(models.Model):
    CD_TP_INST_EJEC = models.IntegerField()
    NB_TP_INST_EJEC = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s' % (self.NB_TP_INST_EJEC)


# Catálogo de ejecutores de obras (PB).
class C_EJECUTOR(models.Model):
    ID_EJECUTOR = models.IntegerField()
    RFC_EJECUTOR = models.CharField(max_length=60)
    NB_EJECUTOR = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s | %s' % (self.ID_EJECUTOR, self.NB_EJECUTOR)


# Catálogo del Tipo de intervención del programa en el espacio público (PB).
class C_TP_INTERV(models.Model):
    TIPO_INTERV = models.IntegerField()
    NB_TP_INTERVENCION = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s | %s' % (self.TIPO_INTERV, self.NB_TP_INTERVENCION)


# Catálogo de modalidades de ejecución (PB).
class C_TIPO_EJEC(models.Model):
    CD_TP_MOD_EJEC = models.IntegerField()
    NB_TP_MOD_EJEC = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s | %s' % (self.CD_TP_MOD_EJEC, self.NB_TP_MOD_EJEC)


# Catálogo de Actividades Económicas (AS) SIIPPG.
class C_ACTIVIDADES(models.Model):
    CD_ACT_ECO = models.IntegerField()
    NB_ACTIV_ECONO = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % (self.NB_ACTIV_ECONO)


# Catálogo de Grupos de identificación si no cuenta con RFC (AS) SIIPPG.
class C_ID_GRUPO(models.Model):
    CD_GRUPO_ID = models.IntegerField()
    NB_GRUPO_ID = models.CharField(max_length=120)

    def __unicode__(self):
        return '%s' % (self.NB_GRUPO_ID)


# Catálogo de tipos de actor social, ya sea beneficiario o intermediario (AS).
class C_TP_ACT_SOC(models.Model):
    TP_ACTOR_SOCIAL = models.IntegerField()
    NB_TP_AS = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s' % (self.NB_TP_AS)


# Catálogo de los cargos que puede tener  la persona descrita dentro de la Asociación Social (AS).
class C_CARGO(models.Model):
    CD_TP_CARGO_AS = models.IntegerField()
    NB_TP_CARGO_AS = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s'% (self.NB_TP_CARGO_AS)


# Catálogo de las descripciones de los beneficios entregados (AS).
class C_BENEFICIO_AS(models.Model):
    CD_BENEFICIO_AS = models.IntegerField()
    NB_BENEFICIO_AS = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % (self.NB_BENEFICIO_AS)


# Catálogo de tipos de beneficiario (PF). Para información anterior a 2012.
class C_TP_BEN(models.Model):
    CD_TP_BEN = models.CharField(max_length=60)
    NB_TP_BEN = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s'%(self.NB_TP_BEN)


# Catálogo del estado Civil (PF).
class C_EDO_CIVIL(models.Model):
    CD_EDO_CIVIL = models.IntegerField()
    NB_EDO_CIVIL = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s'%(self.NB_EDO_CIVIL)


# Catálogo de parentescos de los integrantes de los hogares con el jefe de familia (PF).
class C_PARENTESCO(models.Model):
    CD_PARENTESCO = models.IntegerField()
    NB_PARENTESCO = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s'%(self.NB_PARENTESCO)


# Tipos de beneficios, de acuerdo con la forma en que los otorgan los programas (PF, AS).
# Nota: Los tipos de beneficio que no tienen indicación como "Rexpedición" o "Extemporáneo"
# se refiere a emisiones normales de recursos para apoyos.
class C_TP_BENEFICIO(models.Model):
    CD_TP_BENEFICIO = models.IntegerField()
    NB_TP_BENEFICIO = models.CharField(max_length=60)
    SEUSAEN = models.CharField(max_length=60, blank=True)

    def __unicode__(self):
        return '%s' % (self.NB_TP_BENEFICIO)


# Catálogo de tipos de beneficiario, relacionados a los motivos por los cuales los programas
# asignan beneficios a las personas (PF).
class C_TP_BEN_DET(models.Model):
    CD_TP_BEN_DET = models.IntegerField()
    NB_TP_BEN_DET = models.CharField(max_length=120)
    SEUSAEN = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s' % (self.NB_TP_BEN_DET)


# Catálogo de beneficios entregados a personas (PF).
class C_BENEFICIO(models.Model):
    CD_BENEFICIO = models.IntegerField()
    NB_BENEFICIO = models.CharField(max_length=200)
    SEUSAEN = models.CharField(max_length=150)

    def __unicode__(self):
        return '%s' % (self.NB_BENEFICIO)


# Catálogo de indicador de corresponsabilidad (PF).
class C_CORRESP(models.Model):
    IN_CORRESP = models.IntegerField()
    NB_CORRESP = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s'%(self.NB_CORRESP)


# Catálogo de Programas de Desarrollo Social que aportan información
# para la integración del Padrón Único de Beneficiarios (TODOS).
class C_PROGRAMA(models.Model):
    CD_PROGRAMA = models.CharField(max_length=10)
    CD_PROG_OFICIAL = models.CharField(max_length=60)
    ANIO = models.IntegerField()
    CD_INSTITUCION = models.CharField(max_length=60)
    CD_PROG_DGGPB = models.CharField(max_length=60)
    NB_ORIGEN = models.CharField(max_length=60)
    TP_BENEFICIARIO = models.CharField(max_length=60)
    NB_PROGRAMA = models.CharField(max_length=150)
    CVE_SUBP1 = models.IntegerField()
    NB_SUBP1 = models.CharField(max_length=150)
    NB_SUBP2 = models.CharField(max_length=150)
    NB_PROG = models.CharField(max_length=150)
    # NB_RUTA = models.CharField(max_length=60)
    # NB_RESP = models.CharField(max_length=60)
    # CD_DEPENDENCIA = models.IntegerField()
    # ID_ADMIN = models.IntegerField()
    # NB_DEP = models.CharField(max_length=60)
    # LAST = models.CharField(max_length=60)
    # USER
    # SAPUB = models.CharField(max_length=60)
    # CNcH = models.IntegerField()
    # FH_ACT = models.IntegerField()
    def __unicode__(self):
        return '%s' % (self.NB_PROGRAMA)


# Catálogo de Programas de Desarrollo Social que aportan información al Estado de Cuenta Social.
class C_PERIODO(models.Model):
    CD_PROGRAMA = models.CharField(max_length=60)
    ANIO = models.IntegerField()
    PERIODICIDAD = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s | %s | %s' % (self.CD_PROGRAMA, self.ANIO, self.PERIODICIDAD)


# Catálogo de códigos de beneficio de utilizados por Programa.  (PF)
class C_BENEFICIO_PROG(models.Model):
    CD_BENEFICIO = models.IntegerField()
    NB_BENEFICIO = models.CharField(max_length=200)
    ANIO = models.IntegerField()
    # SEUSAEN = models.CharField(max_length=60)
    CD_PROG_DGGPB = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s | %s'%(self.CD_BENEFICIO, self.NB_BENEFICIO)


# Catálogo de códigos de programa que utilizan el código de tipo de beneficio
class C_TP_BENEFICIO_PROG(models.Model):
    CD_TP_BENEFICIO = models.IntegerField()
    NB_TP_BENEFICIO = models.CharField(max_length=60)
    ANIO = models.IntegerField()
    SEUSAEN = models.CharField(max_length=60)
    CD_PROG_DGGPB = models.CharField(max_length=70)

    def __unicode__(self):
        return '%s' % (self.NB_TP_BENEFICIO)


# Catálogo de tipos de beneficiario, relacionados a los motivos
# por los cuales los programas asignan beneficios a las personas (PF).
class C_TP_BEN_DET_PROG(models.Model):
    CD_TP_BEN_DET = models.IntegerField()
    NB_TP_BEN_DET = models.CharField(max_length=120)
    ANIO = models.IntegerField()
    CD_PROG_DGGPB = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s | %s' % (self.CD_TP_BEN_DET, self.NB_TP_BEN_DET)


# Catálogo de códigos de beneficio de Actor Social utilizados por Programa.  (AS)
class C_BENEFICIO_AS_PROG(models.Model):
    CD_BENEFICIO_AS = models.IntegerField()
    NB_BENEFICIO_AS = models.CharField(max_length=150)
    ANIO = models.IntegerField()
    CD_PROG_DGGPB = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s | %s' % (self.CD_BENEFICIO_AS, self.NB_BENEFICIO_AS)


# Catálogo de códigos de beneficio de Obras y Servicios utilizados por Programa.  (PB)
class C_BENEFICIO_OB_PROG(models.Model):
    CD_BENEFICIO_OB = models.IntegerField()
    NB_BENEFICIO_OB = models.CharField(max_length=120)
    ANIO = models.IntegerField()
    CD_PROG_DGGPB = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s'%(self.NB_BENEFICIO_OB)


class C_PADRON(models.Model):
    CV_PADRON = models.CharField(max_length=12)
    NB_PADRON = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % (self.NB_PADRON)


class C_ESTATUS_BEN(models.Model):
    NB_ESTATUS = models.CharField(max_length=25)

    def __unicode__(self):
        return '%s' % (self.NB_ESTATUS)


class C_ESTATUS_HOG(models.Model):
    NB_ESTATUS = models.CharField(max_length=25)

    def __unicode__(self):
        return '%s' % (self.NB_ESTATUS)


class C_TP_EXPEDICION(models.Model):
    NB_TP = models.CharField(max_length=25)

    def __unicode__(self):
        return '%s' % (self.NB_TP)


class C_MET_PAGO(models.Model):
    NB_MET = models.CharField(max_length=25)

    def __unicode__(self):
        return '%s' % (self.NB_MET)


class C_CORRESPONSABILIDAD(models.Model):
    NB_CORR = models.CharField(max_length=25)

    def __unicode__(self):
        return '%s' % (self.NB_CORR)


class C_AGEB(models.Model):
    NB_AGEB = models.CharField(max_length=25)

    def __unicode__(self):
        return '%s' % (self.NB_AGEB)


class C_MANZANA(models.Model):
    NB_MANZANA = models.CharField(max_length=25)

    def __unicode__(self):
        return '%s' % (self.NB_MANZANA)


# Modelos principales
class EstructuraPersonas(models.Model):
    # ID_REGISTRO = models.CharField(max_length=40,default='')
    ID_HOGAR = models.CharField(max_length=30,
                                default='',
                                verbose_name='ID del hogar')
    ID_CUIS_PS = models.CharField(max_length=40,
                                  default='',
                                  verbose_name='ID CUIS')
    ID_CUIS_SEDESOL = models.CharField(max_length=40,
                                       verbose_name='ID CUIS SEDESOL')
    FH_LEVANTAMIENTO = models.DateField(verbose_name='Fecha de levantamiento')
    ID_PERSONA = models.CharField(max_length=40,
                                  default='',
                                  verbose_name='ID de Persona')
    NB_PRIMER_AP = models.CharField(max_length=50,
                                    default='',
                                    verbose_name='Primer apellido')
    NB_SEGUNDO_AP = models.CharField(max_length=50,
                                     default='',
                                     blank=True,
                                     verbose_name='Segundo apellido')
    NB_NOMBRE = models.CharField(max_length=50,
                                 default='',
                                 verbose_name='Nombre')
    FH_NACIMIENTO = models.DateField(verbose_name='Fecha de nacimiento')
    CD_SEXO = models.CharField(max_length=1,
                               default=None,
                               choices=HM_CHOICES,
                               verbose_name='Sexo')
    CD_EDO_NAC = models.ForeignKey('C_ENTIDAD',
                                   related_name='edonac1',
                                   verbose_name='Estado de nacimiento')
    NB_CURP = models.CharField(max_length=18,
                               default='',
                               verbose_name='C.U.R.P.')
    IN_HUELLA = models.CharField(max_length=1,
                                 choices=SINO_CHOICES,
                                 default=None,
                                 verbose_name='Registro de Huella digital')
    IN_IRIS = models.CharField(max_length=1,
                               choices=SINO_CHOICES,
                               default=None,
                               verbose_name='Registro del Iris')
    CD_EDO_CIVIL = models.ForeignKey('C_EDO_CIVIL',
                                     verbose_name='Estado Civil')
    CD_DEPENDENCIA = models.ForeignKey('C_DEPENDENCIA',
                                       verbose_name='Dependencia')
    CD_INSTITUCION = models.ForeignKey('C_UR',
                                       max_length=5,
                                       default='',
                                       verbose_name='Institución')
    CD_PADRON = models.ForeignKey('C_PADRON',
                                  max_length=4,
                                  default='',
                                  verbose_name='Padrón')
    CD_INTRAPROGRAMA = models.ForeignKey('C_INTRAPROGRAMAS',
                                         verbose_name='Clave del Subprograma')
    NB_SUBPROGRAMA = models.CharField(max_length=60,
                                      default='',
                                      blank=True,
                                      verbose_name='Nombre del Subprograma')
    FH_ALTA = models.DateField(verbose_name='Fecha de alta')
    CD_ESTATUS_BEN = models.ForeignKey('C_ESTATUS_BEN',
                                       verbose_name='Estatus del beneficiario')
    CD_ESTATUS_HOG = models.ForeignKey('C_ESTATUS_HOG',
                                       verbose_name='Estatus del hogar')
    CD_ENT_PAGO = models.ForeignKey('C_ENTIDAD',
                                    related_name='cdentpago',
                                    verbose_name='Entidad Federativa de pago')
    CD_MUN_PAGO = models.ForeignKey('C_MUNICIPIO',
                                    related_name='cdmunpago',
                                    verbose_name='Municipio de pago')
    CD_LOC_PAGO = models.ForeignKey('C_LOCALIDAD',
                                    related_name='cdlocpago',
                                    verbose_name='Localidad de pago')
    NB_PERIODO_CORRES = models.CharField(max_length=7,
                                         default='',
                                         verbose_name='Periodo correspondiente a los apoyos pagados')
    CD_TP_BENEFICIO = models.ForeignKey('C_TP_BENEFICIO',
                                        verbose_name='Tipo de beneficio')
    CD_TP_EXPEDICION = models.ForeignKey('C_TP_EXPEDICION', verbose_name='Tipo de expedición del apoyo')
    IN_TITULAR = models.CharField(max_length=1,
                                  choices=SINO_CHOICES,
                                  default=None,
                                  verbose_name='Indica si la persona es titular del Beneficio')
    CD_PARENTESCO = models.ForeignKey('C_PARENTESCO',
                                      verbose_name='Parentesco de la Persona con el Jefe del Hogar')
    CD_TP_BEN_DET = models.ForeignKey('C_TP_BEN_DET',
                                      verbose_name='Clave del tipo de Beneficiario, afín con el motivo por el cual se otorga el Beneficio')
    NU_BENEFICIOS = models.DecimalField(max_digits=10,
                                        decimal_places=2,
                                        verbose_name='Cantidad total de Beneficios entregados')
    CD_BENEFICIO = models.ForeignKey('C_BENEFICIO',
                                     verbose_name='Clave del Beneficio entregado')
    NU_IMP_MONETARIO = models.DecimalField(max_digits=10,
                                           decimal_places=2,
                                           blank=True,
                                           verbose_name='Importe total en pesos que representa(n) el (los) Beneficio(s) entregado(s)')
    NU_MES_PAGO = models.IntegerField(verbose_name='Mes en que se entregó el (los) Beneficio(s)')
    CD_MET_PAGO = models.ForeignKey('C_MET_PAGO',
                                    max_length=2,
                                    default='',
                                    verbose_name='Clave del método de pago')
    ID_AGRUPADOR = models.CharField(max_length=20, default='',
                                    verbose_name='ID Agrupador')
    IN_CORRESP = models.ForeignKey('C_CORRESP',
                                   verbose_name='Indicador del cumplimiento de la corresponsabilidad')
    TIPOVIAL = models.ForeignKey('C_TP_VIALIDAD',
                                 related_name='tipovial',
                                 verbose_name='Tipo de vialidad')
    NOMVIAL = models.CharField(max_length=255,
                               default='',
                               verbose_name='Nombre de la vialidad')
    CARRETERA = models.CharField(max_length=255,
                                 default='',
                                 verbose_name='Nombre compuesto de la carretera del Domicilio Geográfico del Beneficiario')
    CAMINO = models.CharField(max_length=255,
                              default='',
                              verbose_name='Nombre compuesto del camino del Domicilio Geográfico del Beneficiario')
    NUMEXTNUM1 = models.IntegerField(blank=True,
                                     verbose_name='Número exterior del Domicilio Geográfico del Beneficiario')
    NUMEXTNUM2 = models.IntegerField(blank=True,
                                     verbose_name='Número exterior del Domicilio Geográfico del Beneficiario')
    NUMEXTALF1 = models.CharField(max_length=35,
                                  default='',
                                  verbose_name='Parte alfanumérica del número exterior del Domicilio Geográfico del Beneficiario')
    NUMEXTANT = models.CharField(max_length=35,
                                 default='',
                                 blank=True,
                                 verbose_name='Parte alfanumérica del número exterior anterior del Domicilio Geográfico del Beneficiario')
    NUMINTNUM = models.IntegerField(blank=True,
                                    verbose_name='Número interior del Domicilio Geográfico del Beneficiario')
    NUMINTALF = models.CharField(max_length=35,
                                 default='',
                                 verbose_name='Parte alfanumérica del número interior del Domicilio Geográfico del Beneficiario')
    TIPOASEN = models.ForeignKey('C_TP_ASENTAMIENTO',
                                 verbose_name='Tipo de Asentamiento humano del Domicilio Geográfico del Beneficiario' )
    NOMASEN = models.CharField(max_length=255,
                               default='',
                               verbose_name='Nombre del Asentamiento humano del Domicilio Geográfico del Beneficiario')
    CP = models.CharField(max_length=5,
                          default='',
                          verbose_name='Código Postal del Domicilio Geográfico del Beneficiario')
    NOM_LOC = models.ForeignKey('C_LOCALIDAD',
                                related_name='nomloc',
                                verbose_name='Nombre de la localidad del Domicilio Geográfico del Beneficiario')
    CVE_LOC = models.ForeignKey('C_LOCALIDAD',
                                related_name='cveloc',
                                verbose_name='Clave de la localidad del Domicilio Geográfico del Beneficiario')
    NOM_MUN = models.ForeignKey('C_MUNICIPIO',
                                related_name='nommun',
                                verbose_name='Nombre del municipio del Domicilio Geográfico del Beneficiario')
    CVE_MUN = models.ForeignKey('C_MUNICIPIO',
                                related_name='cvemun',
                                verbose_name='Clave del municipio del Domicilio Geográfico del Beneficiario')
    NOM_ENT = models.ForeignKey('C_ENTIDAD',
                                related_name='noment',
                                verbose_name='Nombre de la Entidad Federativa del Domicilio Geográfico del Beneficiario')
    # CVE_ENT = models.ForeignKey('C_ENTIDAD',
    #                             related_name='cvent',
    #                             verbose_name='Clave de la Entidad Federativa del Domicilio Geográfico del Beneficiario')
    TIPOREF1 = models.ForeignKey('C_TP_VIALIDAD',
                                 related_name='tiporef1',
                                 verbose_name='Tipo de la primera de las entre-vialidades de referencia del Domicilio Geográfico del Beneficiario')
    NOMREF1 = models.CharField(max_length=255,
                               default='',
                               verbose_name='Nombre de la primera de las entre-vialidades de referencia del Domicilio Geográfico del Beneficiario')
    TIPOREF2 = models.ForeignKey('C_TP_VIALIDAD',
                                 related_name='tiporef2',
                                 verbose_name='Tipo de la segunda de las entre-vialidades de referencia del Domicilio Geográfico del Beneficiario')
    NOMREF2 = models.CharField(max_length=255,
                               default='',
                               verbose_name='Nombre de la segunda de las entre-vialidades de referencia del Domicilio Geográfico del Beneficiario' )
    TIPOREF3 = models.ForeignKey('C_TP_VIALIDAD',
                                 related_name='tiporef3',
                                 verbose_name='Tipo de la vialidad ubicada en la parte posterior del Domicilio Geográfico del Beneficiario')
    NOMREF3 = models.CharField(max_length=255,
                               default='',
                               verbose_name='Nombre de la vialidad que se ubica en la parte posterior del Domicilio Geográfico del Beneficiario')
    DESCRUBIC = models.CharField(max_length=255,
                                 default='',
                                 verbose_name='Descripción de la ubicación')
    AGEB = models.ForeignKey('C_AGEB',
                             related_name='EPER_ageb',
                             verbose_name='Clave del Área Geográfica Estadística Básica')
    CLAVE_MZNA = models.ForeignKey('C_MANZANA',
                                   max_length=3,
                                   default='',
                                   verbose_name='Clave de manzana')
    LONGITUD = models.DecimalField(max_digits=11,
                                   decimal_places=6,
                                   verbose_name='Longitud')
    LATITUD = models.DecimalField(max_digits=9,
                                  decimal_places=6,
                                  verbose_name='Latitud')
    trabajo = models.ForeignKey('TrabajosRealizados')

    def __unicode__(self):
        return 'IDR: %s | ID_PERSONA: %s | Nombre: %s %s %s' % (self.pk,
                                                               self.ID_PERSONA,
                                                               self.NB_PRIMER_AP,
                                                               self.NB_SEGUNDO_AP,
                                                               self.NB_NOMBRE
                                                               )


class EstructuraActorSocial(models.Model):
    # ID_REGISTRO = models.CharField(max_length=40,default='')
    ID_ACTOR_SOCIAL = models.CharField(max_length=50,
                                       default='',
                                       blank=True,
                                       verbose_name='ID del Actor Social')
    TP_ACTOR_SOCIAL = models.ForeignKey('C_TP_ACT_SOC',
                                        verbose_name='Clave de Tipo de Actor Social')
    NB_RAZON_SOCIAL = models.CharField(max_length=255,
                                       default='',
                                       verbose_name='Razón social del Actor Social')
    NB_RFC_AS = models.CharField(max_length=13,
                                 default='',
                                 verbose_name='Registro Federal de Contribuyentes del Actor Social')
    NB_CLUNI = models.CharField(max_length=14,
                                default='',
                                blank=True,
                                verbose_name='Clave Inscripción en el Registro Federal de las Organizaciones de la Sociedad Civil')
    FH_CONSTITUCION = models.DateField(verbose_name='Fecha de Constitución del Actor Social')
    CD_GRUPO_ID = models.ForeignKey('C_ID_GRUPO',
                                    blank=True,
                                    verbose_name='Tipo de Agrupación')
    CD_ACT_ECO = models.ForeignKey('C_ACTIVIDADES',
                                   blank=True,
                                   verbose_name='Clave de la actividad económica')
    NB_PRIMER_AP = models.CharField(max_length=50,
                                    default='',
                                    verbose_name='Primer apellido del integrante del Actor Social Beneficiario')
    NB_SEGUNDO_AP = models.CharField(max_length=50,
                                     default='',
                                     blank=True,
                                     verbose_name='Segundo apellido del integrante del Actor Social Beneficiario')
    NB_NOMBRE = models.CharField(max_length=50,
                                 default='',
                                 verbose_name='Nombre del integrante del Actor Social Beneficiario')
    NB_CURP = models.CharField(max_length=18,
                               default='',
                               verbose_name='CURP del integrante del Actor Social Beneficiario')
    FH_NACIMIENTO = models.DateField(verbose_name='Fecha de nacimiento del integrante del Actor Social del Beneficiario')
    CD_SEXO = models.CharField(max_length=1,
                               default=None,
                               choices=HM_CHOICES, verbose_name='Sexo')
    CD_EDO_NAC = models.ForeignKey('C_ENTIDAD',
                                   related_name='EAS_cdedonac',
                                   verbose_name='Clave del estado de nacimiento del integrante del Actor Social Beneficiario')
    CD_TP_CARGO_AS = models.ForeignKey('C_CARGO',
                                       verbose_name='Clave del tipo de cargo que tiene el integrante dentro del Actor Social Beneficiario')
    IN_TITULAR = models.CharField(max_length=1,
                                  choices=SINO_CHOICES,
                                  verbose_name='Indica si la persona es titular del beneficio')
    CD_DEPENDENCIA = models.ForeignKey('C_DEPENDENCIA',
                                       verbose_name='Clave de la dependencia que opera el Programa de Desarrollo Social')
    CD_INSTITUCION = models.ForeignKey('C_UR',
                                       max_length=5,
                                       default='',
                                       verbose_name='Clave de la institución UAR')
    CD_PADRON = models.ForeignKey('C_PADRON',
                                  max_length=4,
                                  default='',
                                  verbose_name='Clave del Padrón')
    CD_INTRAPROGRAMA = models.ForeignKey('C_INTRAPROGRAMAS',
                                         blank=True,
                                         verbose_name='Clave del subprograma')
    NB_SUBPROGRAMA = models.CharField(max_length=60,
                                      default='',
                                      blank=True,
                                      verbose_name='Nombre del subprograma')
    FH_ALTA = models.DateField(verbose_name='Fecha en la que el Actor Social Beneficiario se incorporó al Programa de Desarrollo Social')
    #
    #  CD_ESTATUS_INT = models.ForeignKey('C_ESTATUS_INT',
    CD_ESTATUS_INT = models.IntegerField(#max_length=2,
                                       verbose_name='Estatus del integrante en el mes en que recibe el apoyo')
    #
    # CD_ESTATUS_AS = models.ForeignKey('C_ESTATUS_AS',
    CD_ESTATUS_AS = models.IntegerField(#max_length=2,
                                      verbose_name='Estatus del Actor Social en el mes en que recibe el apoyo')
    #
    # CD_TP_EXPEDICION_AS = models.ForeignKey('C_TP_EXPEDICION_AS',
    CD_TP_EXPEDICION_AS = models.IntegerField(#max_length=2,
                                            verbose_name='Tipo de expedición del apoyo del Actor Social')
    CD_TP_BENEFICIO = models.ForeignKey('C_TP_BENEFICIO',
                                        verbose_name='Clave del tipo de Beneficio')
    NU_BENEFICIOS = models.DecimalField(max_digits=10,
                                        decimal_places=2,
                                        verbose_name='Cantidad Total de Beneficios entregados, agrupados por Beneficio entregado')
    CD_BENEFICIO_AS = models.ForeignKey('C_BENEFICIO_AS',
                                        verbose_name='Clave del Beneficio entregado')
    NU_IMP_MONETARIO = models.DecimalField(max_digits=11,
                                           decimal_places=2,
                                           blank=True,
                                           verbose_name='Importe total en pesos que representa(n) el (los) Beneficio(s) entregado(s)')
    NU_MES_PAGO = models.IntegerField(verbose_name='Mes en que se entregó el (los) Beneficio(s)')
    CD_ENT_PAGO = models.ForeignKey('C_ENTIDAD',
                                    related_name='EAS_cdentpago',
                                    default='',
                                    verbose_name='Clave de la Entidad Federativa donde se entregó el Beneficio')
    CD_MUN_PAGO = models.ForeignKey('C_MUNICIPIO',
                                    max_length=3,
                                    default='',
                                    verbose_name='Clave del Municipio donde se entregó el Beneficio')
    CD_LOC_PAGO = models.ForeignKey('C_LOCALIDAD',
                                    max_length=4,
                                    default='',
                                    verbose_name='Clave de la Localidad donde se entregó el Beneficio')
    NB_PERIODO_CORRES = models.CharField(max_length=4,
                                         default='',
                                         verbose_name='Periodo correspondiente a los apoyos pagados')
    CD_MET_PAGO = models.ForeignKey('C_MET_PAGO',
                                    max_length=2,
                                    default='',
                                    verbose_name='Clave del método de pago, con el que se otorga el Beneficio')
    TIPOVIAL = models.ForeignKey('C_TP_VIALIDAD',
                                 verbose_name='Tipo de vialidad del Domicilio Domicilio Fiscal del Actor Social Beneficiario')
    NOMVIAL = models.CharField(max_length=255,
                               default='',
                               verbose_name='Nombre de la vialidad')
    CARRETERA = models.CharField(max_length=255,
                                 default='',
                                 verbose_name='Nombre compuesto de la carretera del Domicilio Fiscal del Actor Social Beneficiario')
    CAMINO = models.CharField(max_length=255,
                              default='',
                              verbose_name='Nombre compuesto del camino del Domicilio Fiscal del Actor Social Beneficiario')
    NUMEXTNUM1 = models.IntegerField( # max_length=5,
                                     blank=True,
                                     verbose_name='Número exterior del Domicilio Fiscal del Actor Social')
    NUMEXTNUM2 = models.IntegerField( # max_length=5,
                                     blank=True,
                                     verbose_name='Número exterior del Domicilio Fiscal del Actor Social')
    NUMEXTALF1 = models.CharField(max_length=35,
                                  default='',
                                  verbose_name='Parte alfanumérica del número exterior del Domicilio Geográfico del Domicilio Fiscal del Actor Social')
    NUMEXTANT = models.CharField(max_length=35,
                                 default='',
                                 blank=True,
                                 verbose_name='Número exterior anterior del Domicilio Fiscal del Actor Social')
    NUMINTNUM = models.IntegerField( # max_length=5,
                                    blank=True,
                                    verbose_name='Número interior del Domicilio Fiscal del Actor Social')
    NUMINTALF = models.CharField(max_length=35,
                                 default='',
                                 verbose_name='Parte alfanumérica del número interior del Domicilio Geográfico del Domicilio Fiscal del Actor Social')
    TIPOASEN = models.ForeignKey('C_TP_ASENTAMIENTO',
                                 verbose_name='Tipo de asentamiento humano del Domicilio Fiscal del Actor Social')
    NOMASEN = models.CharField(max_length=255,
                               default='',
                               verbose_name='Nombre del asentamiento humano del Domicilio Fiscal del Actor Social')
    CP = models.CharField(max_length=5,
                          default='',
                          verbose_name='Código Postal del Domicilio Fiscal del Actor Social')
    NOM_LOC = models.ForeignKey('C_LOCALIDAD',
                                related_name='EAS_nomloc',
                                max_length=255,
                                default='',
                                verbose_name='Nombre de la Localidad de residencia del Domicilio Fiscal del Actor Social')
    # CVE_LOC = models.ForeignKey('C_LOCALIDAD',
    #                             related_name='EAS_cveloc',
    #                             max_length=4,
    #                             default='',
    #                             verbose_name='Clave de la Localidad de residencia del Domicilio Fiscal del Actor Social')
    NOM_MUN = models.ForeignKey('C_MUNICIPIO',
                                related_name='EAS_nommun',
                                max_length=255,
                                default='',
                                verbose_name='Nombre del Municipio de residencia del Domicilio Fiscal del Actor Social')
    # CVE_MUN = models.ForeignKey('C_MUNICIPIO',
    #                             related_name='EAS_cvemun',
    #                             max_length=3,
    #                             default='',
    #                             verbose_name='Clave del Municipio de residencia del Domicilio Fiscal del Actor Social')
    NOM_ENT = models.ForeignKey('C_ENTIDAD',
                                related_name='EAS_noment',
                                default='',
                                verbose_name='Nombre de la Entidad Federativa del Domicilio Fiscal del Actor Social')
    #CVE_ENT = models.ForeignKey('C_ENTIDAD',
    #                            related_name='cveent',
    #                            default='',
    #                            verbose_name='Clave de la Entidad Federativa  del Domicilio
    # Geográfico del Domicilio Fiscal del Actor Social')
    TIPOREF1 = models.ForeignKey('C_TP_VIALIDAD',
                                 related_name='EAS_tiporef1',
                                 verbose_name='Tipo de la primera de las entre-vialidades de referencia del Domicilio Fiscal del Actor Social')
    NOMREF1 = models.CharField(max_length=255,
                               default='',
                               verbose_name='Nombre de la primera de las entre-vialidades de referencia del Domicilio Fiscal del Actor Social')
    TIPOREF2 = models.ForeignKey('C_TP_VIALIDAD',
                                 related_name='EAS_tiporef2',
                                 verbose_name='Tipo de la segunda de las entre-vialidades de referencia del Domicilio Fiscal del Actor Social')
    NOMREF2 = models.CharField(max_length=255,
                               default='',
                               verbose_name='Nombre de la segunda de las entre-vialidades de referencia del Domicilio Fiscal del Actor Social')
    TIPOREF3 = models.ForeignKey('C_TP_VIALIDAD',
                                 related_name='EAS_tiporef3',
                                 verbose_name='Tipo de la vialidad ubicada en la parte posterior del Domicilio Fiscal del Actor Social')
    NOMREF3 = models.CharField(max_length=255,
                               default='',
                               verbose_name='Nombre de la vialidad que se ubica en la parte posterior del Domicilio Fiscal del Actor Social')
    DESCRUBIC = models.CharField(max_length=255,
                                 default='',
                                 verbose_name='Descripción de la ubicación')
    AGEB = models.ForeignKey('C_AGEB',
                             related_name='EAS_ageb',
                             verbose_name='Clave del Área Geográfica Estadística Básica')
    CLAVE_MZNA = models.ForeignKey('C_MANZANA',
                                   max_length=3,
                                   default='',
                                   verbose_name='Clave de la Manzana')
    LONGITUD = models.DecimalField(max_digits=11,
                                   decimal_places=6,
                                   verbose_name='Longitud')
    LATITUD = models.DecimalField(max_digits=9,
                                  decimal_places=6,
                                  verbose_name='Latitud')
    trabajo = models.ForeignKey('TrabajosRealizados')

    def __unicode__(self):
        return 'IDR: %s | ID_ACTOR_SOCIAL: %s | TP_ACTOR_SOCIAL: %s | NB_RAZON_SOCIAL: %s' % (self.pk,
                                                                                             self.ID_ACTOR_SOCIAL,
                                                                                             self.TP_ACTOR_SOCIAL,
                                                                                             self.NB_RAZON_SOCIAL
                                                                                             )


class EstructuraPoblacion(models.Model):
    # ID_REGISTRO   Carácter(40)
    CD_DEPENDENCIA = models.ForeignKey('C_DEPENDENCIA',
                                       verbose_name='Clave de la Dependencia (Obligatorio)')
    CD_INSTITUCION = models.ForeignKey('C_UR',
                                       verbose_name='Clave de la Institución (Obligatorio)')
    CD_PADRON = models.CharField(max_length=4,
                                 default='',
                                 verbose_name='Clave del Padrón (Obligatorio)') ## GENERAR catalogo de padrones
    CVEPROGRAMA = models.ForeignKey('C_PROGRAMA_DGTIC',
                                    verbose_name='Clave del Programa de Desarrollo Social (Obligatorio)')
    CD_AP_SUBPROG = models.ForeignKey('C_A_SUBPROG',
                                      verbose_name='Clave del Subprograma (Obligatorio)')
    CD_AP_DESCRIPCION = models.ForeignKey('C_AP_DESC',
                                          verbose_name='Clave de la Descripción (Obligatorio)')
    NU_BENEFICIOS = models.DecimalField(max_digits=10,
                                        decimal_places=2,
                                        verbose_name='Cantidad de beneficios entregados (Obligatorio)')
    CD_AP_BENEFICIO_OBRA = models.ForeignKey('C_AP_BEN_OB',
                                             verbose_name='Clave del Tipo de Beneficio entregado (Obligatorio)')
    CD_AP_TP_BENEFICIARIO = models.ForeignKey('C_AP_PROG',
                                              verbose_name='Clave del Tipo de Población (Obligatorio)')
    NU_BENEF = models.IntegerField(verbose_name='Estimación del número de beneficiados (Obligatorio)')
    NU_BENEF_HOM = models.IntegerField(verbose_name='Estimación del número de hombres beneficiados (Obligatorio)')
    NU_BENEF_MUJ = models.IntegerField(verbose_name='Estimación del número de mujeres beneficiadas (Obligatorio)')
    NU_VIVIENDAS = models.IntegerField(blank=True,
                                       verbose_name='Estimación del número de viviendas beneficiadas')
    CD_INTRAPROGRAMA = models.ForeignKey('C_INTRAPROGRAMAS',
                                         ##blank=True,
                                         verbose_name='Clave del subprograma o proyecto')
    CD_TP_INST_EJEC = models.ForeignKey('C_TP_INSTANCIA',
                                        verbose_name='Clave del Tipo de Instancia Ejecutora (Obligatorio)')
    ID_EJECUTOR = models.ForeignKey('C_EJECUTOR',
                                    verbose_name='Clave del Ejecutor (Obligatorio)')
    RFC_EJECUTOR = models.CharField(max_length=13,
                                    default='',
                                    verbose_name='R.F.C. del Ejecutor (Obligatorio)')
    CD_TP_MOD_EJEC = models.ForeignKey('C_TIPO_EJEC',
                                       verbose_name='Clave de la modalidad de la ejecución (Obligatorio)')
    ID_OBRA = models.CharField(max_length=12,
                               default='',
                               verbose_name='ID de la obra (Obligatorio)')
    NB_OBRA = models.CharField(max_length=255,
                               default='',
                               verbose_name='Descripción de la obra (Obligatorio)')
    NU_INV_TOT_EJE = models.DecimalField(max_digits=10,
                                         decimal_places=2,
                                         verbose_name='Inversión Total ejercida(en pesos)(Obligatorio)')
    NU_INV_FED_EJE = models.DecimalField(max_digits=10,
                                         decimal_places=2,
                                         verbose_name='Inversión Federal(en pesos)(Obligatorio)')
    NU_INV_EST_EJE = models.DecimalField(max_digits=10,
                                         decimal_places=2,
                                         verbose_name='Inversión Estatal(en pesos)(Obligatorio)')
    NU_INV_MUN_EJE = models.DecimalField(max_digits=10,
                                         decimal_places=2,
                                         verbose_name='Inversión Municipal(en pesos)(Obligatorio)')
    NU_INV_OTRAS_EJE = models.DecimalField(max_digits=10,
                                           decimal_places=2,
                                           verbose_name='Otras inversiones(en pesos)(Obligatorio)')
    NB_INV_OTRAS_EJE = models.CharField(max_length=255,
                                        default='',
                                        blank=True,
                                        verbose_name='Descripción de otras inversiones')
    FH_INICIO = models.DateField(verbose_name='Fecha en la que la obra se inició (Obligatorio)')
    FH_TERMINO = models.DateField(verbose_name='Fecha en la que la obra fue terminada (Obligatorio)')
    TIPO_INTERV = models.ForeignKey('C_TP_INTERV',
                                    ## blank=True,
                                    verbose_name='Tipo de intervención del Programa')
    TIPOVIAL = models.ForeignKey('C_TP_VIALIDAD',
                                 related_name='TIPOVIAL',
                                 verbose_name='Tipo de vialidad donde se encuentra localizada la obra (Obligatorio)')
    NOMVIAL = models.CharField(max_length=255,
                               default='',
                               verbose_name='Nombre de la vialidad (Obligatorio)')
    CARRETERA = models.CharField(max_length=255,
                                 default='',
                                 verbose_name='Nombre de la carretera (Obligatorio)')
    CAMINO = models.CharField(max_length=255,
                              default='',
                              verbose_name='Nombre del camino donde se encuentra el domicilio (Obligatorio)')
    NUMEXTNUM1 = models.IntegerField(blank=True,
                                     verbose_name='Número exterior del domicilio (Obligatorio)')
    NUMEXTNUM2 = models.IntegerField(blank=True,
                                     verbose_name='Número exterior del domicilio 2')
    NUMEXTALF1 = models.CharField(max_length=35,
                                  default='',
                                  verbose_name='Parte alfanumérica del número exterior del domicilio')
    NUMEXTANT = models.CharField(max_length=35,
                                 default='',
                                 blank=True,
                                 verbose_name='Parte alfanumérica del número exterior anterior del domicilio')
    NUMINTNUM = models.IntegerField(blank=True,
                                    verbose_name='Número interior del domicilio')
    NUMINTALF = models.CharField(max_length=35,
                                 default='',
                                 verbose_name='Parte alfanumérica del número interior del domicilio')
    TIPOASEN = models.ForeignKey('C_TP_ASENTAMIENTO',
                                 verbose_name='Tipo de Asentamiento humano')
    NOMASEN = models.CharField(max_length=255,
                               default='',
                               verbose_name='Nombre del asentamiento humano')
    CP = models.CharField(max_length=5,
                          default='',
                          verbose_name='Código Postal')
    NOM_LOC = models.ForeignKey('C_LOCALIDAD',
                                related_name='LocalidadNombre1',
                                verbose_name='Nombre de la localidad de residencia')
    ## CVE_LOC = models.ForeignKey('C_LOCALIDAD',
    ##                             related_name='LocalidadClave1',
    ##                             verbose_name='Clave de la localidad de residencia')
    NOM_MUN = models.ForeignKey('C_MUNICIPIO',
                                related_name='MunicipioNombre1',
                                verbose_name='Nombre del Municipio de residencia')
    ## CVE_MUN = models.ForeignKey('C_MUNICIPIO',
    ##                             related_name='MunicipioClave1',
    ##                            verbose_name='Clave del Municipio de residencia')
    NOM_ENT = models.ForeignKey('C_ENTIDAD',
                                related_name='EntidadNombre1',
                                verbose_name='Nombre de la Entidad Federativa de residencia')
    ## CVE_ENT = models.ForeignKey('C_ENTIDAD',
    ##                             related_name='EntidadClave1',
    ##                             verbose_name='Clave de la Entidad Federativa de residencia')
    TIPOREF1 = models.ForeignKey('C_TP_VIALIDAD',
                                 related_name='TIPOVIAL2',
                                 verbose_name='Tipo de la primera de las entre vialidades de referencia')
    NOMREF1 = models.CharField(max_length=255,
                               default='',
                               verbose_name='Nombre de la primera de las entre vialidades de referencia')
    TIPOREF2 = models.ForeignKey('C_TP_VIALIDAD',
                                 related_name='TIPOVIAL3',
                                 verbose_name='Tipo de la segunda de las entre vialidades de referencia')
    NOMREF2 = models.CharField(max_length=255,
                               default='',
                               verbose_name='Nombre de la segunda de las entre vialidades de referencia')
    TIPOREF3 = models.ForeignKey('C_TP_VIALIDAD',
                                 related_name='TIPOVIAL4',
                                 verbose_name='Tipo de la tercera de las entre vialidades de referencia')
    NOMREF3 = models.CharField(max_length=255,
                               default='',
                               verbose_name='Nombre de la tercera de las entre vialidades de referencia')
    DESCRUBIC = models.CharField(max_length=255,
                                 default='',
                                 verbose_name='Descripción de la ubicación del domicilio')
    LONGITUD = models.DecimalField(max_digits=11,
                                   decimal_places=6,
                                   verbose_name='Longitud')
    LATITUD = models.DecimalField(max_digits=9,
                                  decimal_places=6,
                                  verbose_name='Latitud')
    trabajo = models.ForeignKey('TrabajosRealizados')

    def __unicode__(self):
        return 'IDR: %s | CD_DEPENDENCIA: %s | CD_INSTITUCION: %s | CD_PADRON: %s | CVEPROGRAMA: %s' % (
            self.pk,
            self.CD_DEPENDENCIA.NB_DEPEN_CORTO,
            self.CD_INSTITUCION,
            self.CD_PADRON,
            self.CVEPROGRAMA
        )


# Modelo de trabajos realizados
class EtapasTrabajos(models.Model):
    nombreEtapa = models.CharField(max_length=20, default='')

    def __unicode__(self):
        return self.nombreEtapa


class TrabajosRealizados(models.Model):
    Etapa = models.ForeignKey(EtapasTrabajos)
    Usuario = models.ForeignKey(User)
    FechaInicio = models.DateTimeField(auto_now_add=True)
    UltimaActualizacion = models.DateField(auto_now=True)
    TipoPadron = models.ForeignKey(Cat_TipoPadron, default=None)
    AnioEjercicio = models.ForeignKey(Cat_AnioEjercicio, default=None)
    Trimestre = models.ForeignKey(Cat_Periodos, default=None)
    CantidadRegistros = models.IntegerField(default=0)

    def __unicode__(self):
        return 'ID: %s | Usuario: %s | Etapa: %s | Padron: %s' % (self.pk, self.Usuario, self.Etapa, self.TipoPadron_id)