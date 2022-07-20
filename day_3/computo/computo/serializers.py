from dataclasses import fields
from pyexpat import model
from unicodedata import category, name
from rest_framework import serializers

from .models import DispEntry, Mouse, Keyboard, Monitor, Computer, Order


#Esto viene de rest_framework y ayuda a la conversion de diccionarios a JSON usa tambien los modelos que teniamos
class DispEntrySerializer(serializers.ModelSerializer):
  class Meta:
    model = DispEntry
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
  class Meta:
    model = Computer
    fields = '__all__' 
    #exclude = ('id','author','category') #Que muestre todo menos los datos especificados
    #fields = ['title', 'author', 'category'] #Solo muestra los datos especificados
  
  def to_representation(self, instance):  #Con esto mostramos lo que necesitemos
    return {
      'id': instance.id,
      'name': instance.name,
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