
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
  cost = models.IntegerField(null=False)

  def __str__(self):
    return f'{self.typeEntry} - {self.trademark}' # Para poder recuperar datos
  
class DispOutput(Component):
  trademark = models.CharField(max_length=50)
  cost = models.IntegerField(null=False)

  def __str__(self):
    return f'{self.trademark} - {self.cost}'

class Mouse(DispEntry): 
  """
  Al heredar models de Django nos da automaticamente un ID por eso no lo declaro aca
  """
  name = models.CharField(max_length=50) # ORM de Django
  status = models.BooleanField(default=True)
  quantity = models.IntegerField(default=1)

  def __str__(self):
    return f'{self.name} - {self.trademark} - stock:{self.quantity}' # Para poder recuperar datos

class Keyboard(DispEntry):    
  name = models.CharField(max_length=50) # PRIMERO VAN LAS CLASES QUE NO TIENEN DEPENDENCIAS DE OTRAS
  status = models.BooleanField(default=True)
  quantity = models.IntegerField(default=1)

  def __str__(self):
    return f'{self.name} - {self.trademark} - stock:{self.quantity}' # Para poder recuperar datos y los datos que llamemos metodo 3 de serializers.py


class Monitor(DispOutput):    
  name = models.CharField(max_length=50) # PRIMERO VAN LAS CLASES QUE NO TIENEN DEPENDENCIAS DE OTRAS
  status = models.BooleanField(default=True)
  quantity = models.IntegerField(default=1)

  def __str__(self):
    return f'{self.name} - {self.trademark} - stock:{self.quantity}'

class Speaker(DispOutput):
  description = models.CharField(max_length=50)
  quantity = models.IntegerField(default=1)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.description} - stock:{self.quantity}'

class InternalDevice(Component):
  trademark = models.CharField(max_length=50)
  cost = models.IntegerField(null=False)

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

class Computer(models.Model):    
  name = models.CharField(max_length=50) 
  monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE) #Recibe la clase que se ponga para poder leer su id
  mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE) #Como en SQL borra los registros que tengan conexion en forma de cascada
  keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)
  speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
  motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE)
  processor = models.ForeignKey(Processor, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  quantity = models.IntegerField(default=1)
  total_cost = models.FloatField(null=True, blank=True)
  
  def decrementar_cantidad(self):
    """Comprobacion del stock antes del decremento"""
    #mouse1 = Mouse.objects.filter(id=self.mouse.id).get().quantity
    mouse = Mouse.objects.filter(id=self.mouse.id)
    keyboard = Keyboard.objects.filter(id=self.keyboard.id)
    monitor = Monitor.objects.filter(id=self.monitor.id)
    speaker = Speaker.objects.filter(id=self.speaker.id)
    motherboard = Motherboard.objects.filter(id=self.motherboard.id)
    processor = Processor.objects.filter(id=self.processor.id)

    if mouse[0].quantity >= self.quantity and keyboard[0].quantity >= self.quantity and monitor[0].quantity >= self.quantity and speaker[0].quantity >= self.quantity and motherboard[0].quantity >= self.quantity and processor[0].quantity >= self.quantity: 
      """Decremento de la existencia"""
      mouse.update(quantity = models.F('quantity')- self.quantity)
      keyboard.update(quantity = models.F('quantity')-self.quantity)
      monitor.update(quantity = models.F('quantity')-self.quantity)
      speaker.update(quantity = models.F('quantity')-self.quantity)
      motherboard.update(quantity = models.F('quantity')-self.quantity)
      processor.update(quantity = models.F('quantity')-self.quantity)

      total = mouse[0].cost + keyboard[0].cost + monitor[0].cost + speaker[0].cost + motherboard[0].cost + processor[0].cost

      return total
    else:
      return 0

  def save(self,*args,**kwargs):
    result = self.decrementar_cantidad()
    if result > 0:
      self.total_cost = result
      super(Computer,self).save(*args,**kwargs)
    else:
      return False

  # Con el metodo 3 aqui se modifica lo que se va a mostrar en el formulario desde serializers.py
  def __str__(self):
    return f'{self.name} - {self.monitor.name} - {self.mouse.name} - {self.keyboard.name} - {self.motherboard.name} - {self.processor.name}' # Para poder recuperar datos


class Order(models.Model):    
  name = models.CharField(max_length=50) 
  computer = models.ForeignKey(Computer, on_delete=models.CASCADE)

  def save(self,*args,**kwargs):
    """Funcion para reducir las existencias de computers"""
    Computer.objects.filter(id=self.computer.id).update(quantity = models.F('quantity') - Computer.quantity)
    super(Order,self).save(*args,**kwargs)

  def __str__(self):
    return f'{self.computer.name} '

#Author.objects.all()
#Author.objects.create('atributos de la clase o modelo')
#Author.objects.filter(firs_name='John ') 

"""def __str__(self):
    return self.name
  
  def __unicode__(self):
    return self.name"""

"""
def save(self,*args,**kwargs):
    #Funcion para reducir el stock de varios componentes
    Monitor.objects.filter(id=self.monitor.id).update(quantity = models.F('quantity')-1)
    Mouse.objects.filter(id=self.mouse.id).update(quantity = models.F('quantity')-1)
    Keyboard.objects.filter(id=self.keyboard.id).update(quantity = models.F('quantity')-1)
    Speaker.objects.filter(id=self.speaker.id).update(quantity = models.F('quantity')-1)
    Motherboard.objects.filter(id=self.motherboard.id).update(quantity = models.F('quantity')-1)
    Processor.objects.filter(id=self.processor.id).update(quantity = models.F('quantity')-1)
    super(Computer,self).save(*args,**kwargs)

  # Con el metodo 3 aqui se modifica lo que se va a mostrar en el formulario desde serializers.py
  def __str__(self):
    return f'{self.name} - {self.monitor.name} - {self.mouse.name} - {self.keyboard.name} - {self.motherboard.name} - {self.processor.name}'
"""