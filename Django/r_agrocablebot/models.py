from django.db import models
from django.conf import settings 
from .choices import unidadMedida,estadoSalud, SioNO
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
    descripcion=models.TextField(blank=True,verbose_name='Descripción')
    preparacionSuelo=models.TextField(blank=True,verbose_name='Preparación del suelo')
    riego=models.TextField(blank=True,verbose_name='Riego')
    controlMalezas=models.TextField(blank=True,verbose_name='Control de Malezas')
    controlPlagasyEnfermedades=models.TextField(blank=True,verbose_name='Control de Plagas y Enfermedades')
    fertilizacion=models.TextField(blank=True,verbose_name='Fertilización')
    moniteroRegistro=models.TextField(blank=True,verbose_name='Monitoreo y Registro')
    estimadoGerminacionMin=models.PositiveIntegerField(blank=True,verbose_name='Estimado mínimo para germinación [días]')
    estimadoGerminacionMax=models.PositiveIntegerField(blank=True,verbose_name='Estimado máximo para germinación [días]')
    estimadoCosechaMin=models.PositiveIntegerField(blank=True,verbose_name='Estimado mínimo para cosechar [días]')
    estimadoCosechaMax=models.PositiveIntegerField(blank=True,verbose_name='Estimado máximo para cosechar [días]')
    temperaturaOptimaMin=models.PositiveIntegerField(blank=True,verbose_name='Temperatura mínima [°C]')
    temperaturaOptimaMax=models.PositiveIntegerField(blank=True,verbose_name='Temperatura máxima [°C]')
    profundidadSiembra=models.PositiveIntegerField(blank=True,verbose_name='Profundidad de siembra [cm]')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de cultivo'
        verbose_name_plural = 'Tipos de cultivos'
        db_table = 'tipos_cultivos'
        ordering = ['id']

class sensor(models.Model):
    valorDecimal=models.DecimalField( max_digits=3,decimal_places=3,blank=True,verbose_name='Valor del sensor decimal')
    #valorSTR=models.CharField(max_length=50, verbose_name='Valor del sensor String')
    coordenadaX=models.DecimalField(max_digits=3,decimal_places=3,blank=True,verbose_name='Coordenada en el eje X')
    coordenadaY=models.DecimalField(max_digits=3,decimal_places=3,blank=True,verbose_name='Coordenada en el eje Y')
    coordenadaZ=models.DecimalField(max_digits=3,decimal_places=3,blank=True,verbose_name='Coordenada en el eje Z')
    fecha_creado = models.DateTimeField(auto_now_add=True)
    tipoSensor=models.ForeignKey(tipoSensor, null=True,blank=True,on_delete=models.CASCADE)

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
    responable= models.CharField(max_length=100)
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
    numeroPlanta= models.PositiveSmallIntegerField(blank=True,verbose_name='Numero de Planta')
    coordenadaX=models.DecimalField(max_digits=3,decimal_places=3,blank=True,verbose_name='Coordenada en el eje X')
    coordenadaY=models.DecimalField(max_digits=3,decimal_places=3,blank=True,verbose_name='Coordenada en el eje Y')
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
    imagen = models.ImageField(upload_to='iconos/plantas/', verbose_name="imagen", null= True ,blank=True)
    descripcion=models.TextField(blank=True)
    plantas=models.ForeignKey(plantas, null=True,blank=True,on_delete=models.CASCADE)
    
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
    recuerrente= models.CharField(max_length=1, choices=SioNO, default='S')
    todoCultivo= models.CharField(max_length=1, choices=SioNO, default='S')
    fecha=models.DateField()
    hora=models.TimeField()
    cultivo=models.ForeignKey(cultivo, null=True,blank=True,on_delete=models.CASCADE)
    plantas=models.ForeignKey(plantas, null=True,blank=True,on_delete=models.CASCADE)
    


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Calendario'
        verbose_name_plural = 'Calendarios'
        db_table = 'calendarios'
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