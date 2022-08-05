from rest_framework import serializers

from ..models.computer import Computer
from ..models.component import Mouse, Keyboard, Monitor, Speaker, Motherboard, Processor

class ComputerSerializer(serializers.ModelSerializer):
  """
  Metodo 3 para mostrar datos de la relacion entre las tablas
  """
  mouse = serializers.PrimaryKeyRelatedField(queryset=Mouse.objects.all())
  keyboard = serializers.PrimaryKeyRelatedField(queryset=Keyboard.objects.all())
  monitor = serializers.PrimaryKeyRelatedField(queryset=Monitor.objects.all())
  speaker = serializers.PrimaryKeyRelatedField(queryset=Speaker.objects.all())
  motherboard = serializers.PrimaryKeyRelatedField(queryset=Motherboard.objects.all())
  processor = serializers.PrimaryKeyRelatedField(queryset=Processor.objects.all())
  class Meta:
    model = Computer
    fields = '__all__' 
    #exclude = ('id','author','category') #Que muestre todo menos los datos especificados
    #fields = ['title', 'author', 'category'] #Solo muestra los datos especificados
  
  def to_representation(self, instance):  #Con esto mostramos lo que necesitemos
    return {
      'id': instance.id,
      'description': instance.description,
      'total_cost': instance.total_cost,
      'quantity': instance.quantity,
      'monitor': {
        'description': instance.monitor.description,
        'trademark': instance.monitor.trademark,
        'status': instance.monitor.status
      },
      'keyboard': {
        'description': instance.keyboard.description,
        'trademark': instance.keyboard.trademark,
        'status': instance.keyboard.status
      },
      'mouse': {
        'description': instance.mouse.description,
        'trademark': instance.mouse.trademark,
        'status': instance.mouse.status
      },
      'motherboard': {
        'description': instance.motherboard.description
      },
      'processor': {
        'description': instance.processor.description
      }
    }