from django.db import models

# Create your models here.
class Usuario(models.Model):
    idusuario= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45,null=True)
    apellido=models.CharField(max_length=45,default='S/A')
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Personas(models.Model):
    idpersona= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45,null=True)
    apellido=models.CharField(max_length=45,default='S/A')
    direccion=models.CharField(max_length=200,default='S/D')
    edad = models.IntegerField()
    telefono=models.CharField(max_length=45,null=True)

    def __str__(self):
        return self.nombre
