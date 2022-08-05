from django.db import models

# Creando tablas por asi decirlo o SCHEMAS

class Component(models.Model):
  typeComponent = models.CharField(max_length=50)

  def __str__(self):
    return self.typeComponent

  class Meta:
    abstract = True


class DispEntry(Component):
  trademark = models.CharField(max_length=50)
  cost = models.IntegerField(null=True, blank=True)

  def __str__(self):
    return f'{self.typeEntry} - {self.trademark}' # Para poder recuperar datos
  
class DispOutput(Component):
  trademark = models.CharField(max_length=50)
  cost = models.IntegerField(null=True, blank=True)

  def __str__(self):
    return f'{self.trademark} - {self.cost}'

class Mouse(DispEntry): 
  """
  Al heredar models de Django nos da automaticamente un ID por eso no lo declaro aca
  """
  description = models.CharField(max_length=50) # ORM de Django
  status = models.BooleanField(default=True)
  quantity = models.IntegerField(default=1)

  def __str__(self):
    return f'{self.description} - {self.trademark} - stock:{self.quantity}' # Para poder recuperar datos

class Keyboard(DispEntry):    
  description = models.CharField(max_length=50) # PRIMERO VAN LAS CLASES QUE NO TIENEN DEPENDENCIAS DE OTRAS
  status = models.BooleanField(default=True)
  quantity = models.IntegerField(default=1)

  def __str__(self):
    return f'{self.description} - {self.trademark} - stock:{self.quantity}' # Para poder recuperar datos y los datos que llamemos metodo 3 de serializers.py


class Monitor(DispOutput):    
  description = models.CharField(max_length=50) # PRIMERO VAN LAS CLASES QUE NO TIENEN DEPENDENCIAS DE OTRAS
  status = models.BooleanField(default=True)
  quantity = models.IntegerField(default=1)

  def __str__(self):
    return f'{self.description} - {self.trademark} - stock:{self.quantity}'

class Speaker(DispOutput):
  description = models.CharField(max_length=50)
  quantity = models.IntegerField(default=1)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.description} - stock:{self.quantity}'

class InternalDevice(Component):
  trademark = models.CharField(max_length=50)
  cost = models.IntegerField(null=True, blank=True)

  def __str__(self):
    return f'{self.trademark} - {self.cost}'

class Motherboard(InternalDevice):
  description = models.CharField(max_length=50)
  quantity = models.IntegerField(default=1)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.description} - stock:{self.quantity}'

class Processor(InternalDevice):
  description = models.CharField(max_length=50)
  quantity = models.IntegerField(default=1)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.description} - stock:{self.quantity}'