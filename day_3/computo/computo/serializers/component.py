from rest_framework import serializers

from ..models.component import Component,InternalDevice, DispOutput, DispEntry, Keyboard, Monitor, Mouse, Speaker, Motherboard, Processor

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