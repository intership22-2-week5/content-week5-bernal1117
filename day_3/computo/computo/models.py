
from unicodedata import name
from django.db import models

# Creando tablas por asi decirlo o SCHEMAS
class DispEntry(models.Model):
  typeEntry = models.CharField(max_length=50)
  trademark = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.typeEntry} - {self.trademark}' # Para poder recuperar datos

class Mouse(DispEntry): 
  """
  Al heredar models de Django nos da automaticamente un ID por eso no lo declaro aca
  """
  name = models.CharField(max_length=50) # ORM de Django
  status = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.name} - {self.trademark}' # Para poder recuperar datos

class Keyboard(DispEntry):    
  name = models.CharField(max_length=50) # PRIMERO VAN LAS CLASES QUE NO TIENEN DEPENDENCIAS DE OTRAS
  status = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.name} - {self.trademark}' # Para poder recuperar datos y los datos que llamemos metodo 3 de serializers.py


class Monitor(models.Model):    
  name = models.CharField(max_length=50) # PRIMERO VAN LAS CLASES QUE NO TIENEN DEPENDENCIAS DE OTRAS
  trademark = models.CharField(max_length=50)
  status = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.name} - {self.trademark}'


class Computer(models.Model):    
  name = models.CharField(max_length=50) 
  monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE) #Recibe la clase que se ponga para poder leer su id
  mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE) #Como en SQL borra los registros que tengan conexion en forma de cascada
  keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)

  # Con el metodo 3 aqui se modifica lo que se va a mostrar en el formulario desde serializers.py
  def __str__(self):
    return f'{self.name} - {self.monitor.name} - {self.mouse.name} - {self.keyboard.name}' # Para poder recuperar datos


class Order(models.Model):    
  name = models.CharField(max_length=50) 
  computer = models.ForeignKey(Computer, on_delete=models.CASCADE)


  def __str__(self):
    return f'{self.computer.name} '

#Author.objects.all()
#Author.objects.create('atributos de la clase o modelo')
#Author.objects.filter(firs_name='John ') 

"""def __str__(self):
    return self.name
  
  def __unicode__(self):
    return self.name"""