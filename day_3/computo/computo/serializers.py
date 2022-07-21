
from rest_framework import serializers

from .models import DispEntry, DispOutput, InternalDevice, Motherboard, Mouse, Keyboard, Monitor, Computer, Order, Processor, Speaker, Component


#Esto viene de rest_framework y ayuda a la conversion de diccionarios a JSON usa tambien los modelos que teniamos
class ComponentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Component
    fields = '__all__'

class DispEntrySerializer(serializers.ModelSerializer):
  class Meta:
    model = DispEntry
    fields = '__all__'

class DispOutputSerializer(serializers.ModelSerializer):
  class Meta:
    model = DispOutput
    fields = '__all__'

class InternalDeviceSerializer(serializers.ModelSerializer):
  class Meta:
    model = InternalDevice
    fields = '__all__'

class SpeakerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Speaker
    fields = '__all__'

class MotherboardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Motherboard
    fields = '__all__'

class ProcessorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Processor
    fields = '__all__'

class MouseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mouse
    fields = '__all__' 

class MonitorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Monitor
    fields = '__all__' 

class KeyboardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Keyboard
    fields = '__all__' 
    
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
      'name': instance.name,
      'total_cost': instance.total_cost,
      'monitor': {
        'name': instance.monitor.name,
        'trademark': instance.monitor.trademark,
        'status': instance.monitor.status
      },
      'keyboard': {
        'name': instance.keyboard.name,
        'trademark': instance.keyboard.trademark,
        'status': instance.keyboard.status
      },
      'mouse': {
        'name': instance.mouse.name,
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

class OrderSerializer(serializers.ModelSerializer):
  
  computer = serializers.PrimaryKeyRelatedField(queryset=Computer.objects.all())
  class Meta:
    model = Order
    fields = '__all__' 
    #exclude = ('id','author','category') #Que muestre todo menos los datos especificados
    #fields = ['title', 'author', 'category'] #Solo muestra los datos especificados
  
  def to_representation(self, instance):  #Con esto mostramos lo que necesitemos
    return {
      'id': instance.id,
      'name':instance.name,
      'computer': {
        'name': instance.computer.name
      }
    }