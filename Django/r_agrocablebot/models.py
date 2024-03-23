from django.db import models
from django.conf import settings 
from .choices import unidadMedida,estadoSalud, SioNO, repeticionChoices
#from imacuna import models
# Create your models here.


#ACCIONES 

class acciones(models.Model):
    nombre=models.CharField(max_length= 100, verbose_name='Nombre', unique=True)
    descripcion=models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Acción'
        verbose_name_plural = 'Acciones'
        db_table = 'acciones'
        ordering = ['id']


class tipoSensor(models.Model):
    nombre=models.CharField(max_length= 100, verbose_name='Nombre', unique=True)
    unidadMedida = models.CharField(max_length=100, choices=unidadMedida, default='m')
    descripcion=models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de sensor'
        verbose_name_plural = 'Tipos de sensores'
        db_table = 'tipos_sensores'
        ordering = ['id']


class tipoCultivo(models.Model):
    nombre=models.CharField(max_length= 100, verbose_name='Nombre', unique=True)
    descripcion=models.TextField(blank=True,verbose_name='Descripción', null= True)
    preparacionSuelo=models.TextField(blank=True,verbose_name='Preparación del suelo', null= True)
    riego=models.TextField(blank=True,verbose_name='Riego', null= True)
    controlMalezas=models.TextField(blank=True,verbose_name='Control de Malezas', null= True)
    controlPlagasyEnfermedades=models.TextField(blank=True,verbose_name='Control de Plagas y Enfermedades', null= True)
    fertilizacion=models.TextField(blank=True,verbose_name='Fertilización', null= True)
    moniteroRegistro=models.TextField(blank=True,verbose_name='Monitoreo y Registro', null= True)
    estimadoGerminacionMin=models.PositiveIntegerField(blank=True,verbose_name='Estimado mínimo para germinación [días]', null= True)
    estimadoGerminacionMax=models.PositiveIntegerField(blank=True,verbose_name='Estimado máximo para germinación [días]', null= True)
    estimadoCosechaMin=models.PositiveIntegerField(blank=True,verbose_name='Estimado mínimo para cosechar [días]', null= True)
    estimadoCosechaMax=models.PositiveIntegerField(blank=True,verbose_name='Estimado máximo para cosechar [días]', null= True)
    temperaturaOptimaMin=models.PositiveIntegerField(blank=True,verbose_name='Temperatura mínima [°C]', null= True)
    temperaturaOptimaMax=models.PositiveIntegerField(blank=True,verbose_name='Temperatura máxima [°C]', null= True)
    profundidadSiembra=models.DecimalField(max_digits=10,decimal_places=3,blank=True,verbose_name='Profundidad de siembra', null= True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de cultivo'
        verbose_name_plural = 'Tipos de cultivos'
        db_table = 'tipos_cultivos'
        ordering = ['id']

class sensor(models.Model):
    nombre=models.CharField(max_length= 100, verbose_name='Nombre', unique=True)
    valorDecimal=models.DecimalField( max_digits=10,decimal_places=3,blank=True,verbose_name='Valor del sensor decimal')
    #valorSTR=models.CharField(max_length=50, verbose_name='Valor del sensor String')
    coordenadaX=models.DecimalField(max_digits=10,decimal_places=3,blank=True,verbose_name='Coordenada en el eje X')
    coordenadaY=models.DecimalField(max_digits=10,decimal_places=3,blank=True,verbose_name='Coordenada en el eje Y')
    coordenadaZ=models.DecimalField(max_digits=10,decimal_places=3,blank=True,verbose_name='Coordenada en el eje Z')
    fecha_creado = models.DateTimeField(auto_now_add=True)
    tipoSensor=models.ForeignKey(tipoSensor, null=True,blank=True,on_delete=models.CASCADE,verbose_name='Tipo sensor')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensores'
        db_table = 'sensores'
        ordering = ['id']


class cultivo(models.Model):
    nombre=models.CharField(max_length= 100, verbose_name='Nombre')
    cantidad= models.PositiveSmallIntegerField(blank=True,verbose_name='Cantidad de plantas')
    iconosPlantas=models.ImageField(upload_to='iconos/iconosPlantas/', verbose_name="Icono de la planta", null= True )
    responsable= models.CharField(max_length=100)
    correo=models.CharField(max_length= 100, verbose_name='Correo Electrónico')
    fechaSiembra = models.DateField(verbose_name='Fecha de siembra')
    tipoCultivo=models.ForeignKey(tipoCultivo, null=True,blank=True,on_delete=models.CASCADE)
    sensores=models.ManyToManyField(sensor, verbose_name="Sensores",blank=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cultivo'
        verbose_name_plural = 'Cultivos'
        db_table = 'cultivos'
        ordering = ['id']

class plantas(models.Model):
    nombre=models.CharField(max_length= 100, verbose_name='Nombre', unique=True)
    numeroPlanta= models.PositiveSmallIntegerField(blank=True,verbose_name='Numero de Planta',unique=True)
    coordenadaX=models.DecimalField(max_digits=10,decimal_places=3,blank=True,verbose_name='Coordenada en el eje X')
    coordenadaY=models.DecimalField(max_digits=10,decimal_places=3,blank=True,verbose_name='Coordenada en el eje Y')
    estadoSalud = models.CharField(max_length=1, choices=estadoSalud, default='S')
    cultivo=models.ForeignKey(cultivo, null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Planta'
        verbose_name_plural = 'Plantas'
        db_table = 'plantas'
        ordering = ['id']



class imagenesxPlanta(models.Model):
    nombre=models.CharField(max_length= 100, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='cultivo/plantas/', verbose_name="Imagen", null= True ,blank=True)
    descripcion=models.TextField(blank=True, verbose_name="Descripcion")
    plantas=models.ForeignKey(plantas, null=True,blank=True,on_delete=models.CASCADE, verbose_name="Plantas")
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Imagen por planta'
        verbose_name_plural = 'Imagenes por planta'
        db_table = 'imagenes_plantas'
        ordering = ['id']

# class tablasEstadisticas(models.Model):
#     nombre=models.CharField(max_length= 100, verbose_name='Nombre', unique=True)
#     descripcion=models.TextField(blank=True)
#     sensor=models.ForeignKey(sensor, null=True,blank=True,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nombre

#     class Meta:
#         verbose_name = 'Tabla de estadísticas'
#         verbose_name_plural = 'Tablas de estadísticas'
#         db_table = 'tablas_estadisticas'
#         ordering = ['id']

# class graficos(models.Model):
#     nombre=models.CharField(max_length= 100, verbose_name='Nombre', unique=True)
#     descripcion=models.TextField(blank=True)
#     sensor=models.ForeignKey(sensor, null=True,blank=True,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nombre

#     class Meta:
#         verbose_name = 'Gráfico'
#         verbose_name_plural = 'Gráficos'
#         db_table = 'graficos'
#         ordering = ['id']


# class estadisticas(models.Model):
#     nombre=models.CharField(max_length= 100, verbose_name='Nombre', unique=True)
#     tablasEstadisticas=models.ForeignKey(tablasEstadisticas, null=True,blank=True,on_delete=models.CASCADE)
#     graficos=models.ForeignKey(graficos, null=True,blank=True,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nombre

#     class Meta:
#         verbose_name = 'Estadística'
#         verbose_name_plural = 'Estadísticas'
#         db_table = 'estadisticas'
#         ordering = ['id']

class calendarios(models.Model):
    nombre=models.CharField(max_length= 100, verbose_name='Nombre', unique=True)
    acciones=models.ForeignKey(acciones, null=True,blank=True,on_delete=models.CASCADE,verbose_name='Acciones')
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    repeticion= models.CharField(max_length=1, choices=repeticionChoices, default='D') # Ej: 'diaria', 'semanal', 'mensual'
    intervalo = models.IntegerField(null=True, blank=True)  # Número de días, semanas o meses dependiendo de la repeticion
    todoCultivo= models.CharField(max_length=1, choices=SioNO, default='S')
    hora_repeticion_1 = models.TimeField(null=True, blank=True)  # Hora de la primera repetición diaria
    hora_repeticion_2 = models.TimeField(null=True, blank=True)  # Hora de la segunda repetición diaria
    hora_repeticion_3 = models.TimeField(null=True, blank=True)
    cultivo=models.ManyToManyField(cultivo, verbose_name="Cultivos",blank=True)
    plantas=models.ManyToManyField(plantas, verbose_name="Plantas",blank=True)
    


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Calendario'
        verbose_name_plural = 'Calendarios'
        db_table = 'calendarios'
        ordering = ['id']

class eventosCalendarios(models.Model):
    
    title = models.CharField(max_length=100)
    start = models.DateTimeField()
    calendario = models.ForeignKey(calendarios, on_delete=models.CASCADE)
    allDay = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
 
    class Meta:
        verbose_name = 'Evento calendario'
        verbose_name_plural = 'Eventos calendarios'
        db_table = 'eventos_calendarios'
        ordering = ['id']


# class mo_agroCableBot(models.Model):
#     descripcion=models.TextField(blank=True)
#     proyectos=models.ForeignKey(models.proyectos, null=True,blank=True,on_delete=models.CASCADE)
#     integrantes=models.ForeignKey(models.integrante, null=True,blank=True,on_delete=models.CASCADE)
#     estadisticas=models.ForeignKey(estadisticas, null=True,blank=True,on_delete=models.CASCADE)


#     def __str__(self):
#         return self.nombre

#     class Meta:
#         verbose_name = 'Tipo de sensor'
#         verbose_name_plural = 'Tipos de sensores'
#         db_table = 'tipos_sensores'
#         ordering = ['id']

class Mensaje (models.Model):
    topic = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)


class Sensor_MQTT(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    acelerometro_roll = models.FloatField()
    acelerometro_pitch = models.FloatField()
    acelerometro_yaw = models.FloatField()
    giroscopio_roll = models.FloatField()
    giroscopio_pitch = models.FloatField()
    giroscopio_yaw = models.FloatField()
    magnetometro_x = models.FloatField()
    magnetometro_y = models.FloatField()
    magnetometro_z = models.FloatField()
    orientacion_roll = models.FloatField()
    orientacion_pitch = models.FloatField()
    orientacion_yaw = models.FloatField()
    humedad = models.FloatField()
    presion = models.FloatField()
    temperatura = models.FloatField()

    # def __str__(self):
    #     return self.temperatura

    # class Meta:
    #     verbose_name = 'Sensor'
    #     verbose_name_plural = 'Sensores'
    #     db_table = 'Sensores'
    #     ordering = ['id']


class RutinaCodigoG(models.Model):
    nombre = models.CharField(max_length=100)
    codigo_g = models.TextField()

    def _str_(self):
        return self.nombre

    class Meta:
        verbose_name = 'Rutina G'
        verbose_name_plural = 'Rutinas G'
        db_table = 'rutinas_g'
        ordering = ['id']