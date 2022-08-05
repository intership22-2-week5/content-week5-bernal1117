
from django.db import models

from .computer import Computer

class Order(models.Model):    
  description = models.CharField(max_length=50) 
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=20, blank=True, null=True, default='active')

  def __str__(self):
    return f'{self.description}'


class Detailsorder(models.Model):  
  computer = models.ForeignKey(Computer, on_delete=models.CASCADE)   
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)
  total_cost_order = models.FloatField(null=True, blank=True)

  def decrementar_cant(self):
    computer = Computer.objects.filter(id=self.computer.id)

    if computer[0].quantity >= self.quantity:
      """Decremento de existencia en computadoras"""
      computer.update(quantity = models.F('quantity')-self.quantity)

      total = computer[0].total_cost * self.quantity

      return total
    else:
      return 0

  def save(self,*args,**kwargs):
    result = self.decrementar_cant()
    if result > 0:
      self.total_cost_order = result
      super(Detailsorder,self).save(*args,**kwargs)
    else:
      return False

  def __str__(self):
    return f'{self.order.description}'