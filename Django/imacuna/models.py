from django.db import models
from django.conf import settings 
from .choices import sexos

#lINEAS DE INVESTIGACIÓN

class Lineas_investigacion(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 100 , verbose_name="Nombre", null=True)
    imagen = models.ImageField(upload_to='iconos/Lineas_investigacion/', verbose_name="imagen", null= True )
    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.nombre

class Servicios(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 100 , verbose_name="Nombre", null=True)
    imagen = models.ImageField(upload_to='iconos/Servicios/', verbose_name="imagen", null= True )
    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.nombre

class Roles(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 50 , verbose_name="rol" )
# Usuario de otra forma
class Usuarios(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , related_name= 'usuarios', on_delete= models.CASCADE)
    nombre = models.CharField(max_length=150)
    Completado = models.BooleanField(default=False)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.nombre

# Modelo Facultades ---------------------
class facultades(models.Model):
    nombre=models.CharField(max_length= 50, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'
        db_table = 'facultades'
        ordering = ['id']

# Modelo programas---------------------
class programa(models.Model):
    nombre=models.CharField(max_length= 50, verbose_name='Nombre', unique=True)
    facultades=models.ForeignKey(facultades,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'
        db_table = 'programa'
        ordering = ['id']

# Modelo tipo de integrante---------------------
class tipoIntegrante(models.Model):
    nombre=models.CharField(max_length= 50, verbose_name='Nombre', unique=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de Integrante'
        verbose_name_plural = 'Tipos de Integrantes'
        db_table = 'tipo_integrante'
        ordering = ['id']
# Modelo Integrantes -Equipo de trabajo ----------------
class integrante(models.Model):
    primer_apellido = models.CharField(max_length=50, verbose_name='Primer Apellido')
    segundo_apellido = models.CharField(max_length=50, verbose_name='Segundo Apellido')
    nombres = models.CharField(max_length= 50, verbose_name='Nombres')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    correo=models.CharField(max_length= 50, verbose_name='Correo Electrónico')
    sexo = models.CharField(max_length=1, choices=sexos, default='M')
    imagen = models.ImageField(upload_to='fotoPerfil/', null=True, blank=True)
    facultades=models.ForeignKey(facultades,to_field='nombre' ,null=True,blank=True,on_delete=models.CASCADE)
    programa=models.ForeignKey(programa,to_field='nombre', null=True,blank=True,on_delete=models.CASCADE)
    tipoIntegrante=models.ForeignKey(tipoIntegrante,to_field='nombre',null=True,blank=True,on_delete=models.CASCADE)
    linkedin = models.CharField(max_length=100, verbose_name='urllinkedin', null=True)
    resechgate = models.CharField(max_length=100, verbose_name='urlresechgate', null=True)

    def nombre_completo(self):
        return "{} {}, {}".format(self.primer_apellido, self.segundo_apellido, self.nombres)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name = 'Integrante'
        verbose_name_plural = 'Integrantes'
        db_table = 'integrantes'
        ordering = ['id']

# Modelo Videos_Proyectos ----------------------
class videoProyectos(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion=models.TextField(blank=True)
    archivo_video = models.FileField(upload_to='videosProyectos/', unique=True )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Video proyecto'
        verbose_name_plural = 'Videos Proyectos'
        db_table = 'videos_proyecto'
        ordering = ['id']   

# Modelo imagenes_Proyectos ----------------------
class imagenesProyectos(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion=models.TextField(blank=True)
    imagen = models.ImageField(upload_to='imagenesProyectos/',verbose_name='imagen', null=True, blank=True, unique=True )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Imágen proyecto'
        verbose_name_plural = 'Imágenes Proyectos'
        db_table = 'imagenes_proyecto'
        ordering = ['id']   

# Modelo Proyectos ----------------------
class proyectos(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    integrante=models.ManyToManyField(integrante, verbose_name="Integrantes",blank=True)
    videoProyectos=models.ManyToManyField(videoProyectos,verbose_name="Videos",blank=True)
    imagenesProyectos=models.ManyToManyField(imagenesProyectos, verbose_name="Imágenes",blank=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        db_table = 'proyecto'
        ordering = ['id']


        