from django.db import models

from .component import Monitor, Keyboard, Mouse, Speaker, Motherboard, Processor


class Computer(models.Model):    
  description = models.CharField(max_length=50) 
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
    return f'{self.description} - stock:{self.quantity}' # Para poder recuperar datos
