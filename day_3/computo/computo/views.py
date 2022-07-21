#Django rest framework 
from rest_framework.views import Response
from rest_framework import viewsets

from .serializers import DispEntrySerializer, DispOutputSerializer, InternalDeviceSerializer, MotherboardSerializer, MouseSerializer, KeyboardSerializer, MonitorSerializer, ComputerSerializer, OrderSerializer, ProcessorSerializer, SpeakerSerializer

#models
from .models import DispEntry, DispOutput, InternalDevice, Motherboard, Mouse, Keyboard, Monitor, Computer, Order, Processor, Speaker
"""
class ComponentViewSets(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
"""

class DispEntryViewSets(viewsets.ModelViewSet):
    queryset = DispEntry.objects.all()
    serializer_class = DispEntrySerializer

class DispOutputViewSets(viewsets.ModelViewSet):
    queryset = DispOutput.objects.all()
    serializer_class = DispOutputSerializer

class InternalDeviceViewSets(viewsets.ModelViewSet):
    queryset = InternalDevice.objects.all()
    serializer_class = InternalDeviceSerializer

class MouseViewSets(viewsets.ModelViewSet):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer

class KeyboardViewSets(viewsets.ModelViewSet):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer

class MonitorViewSets(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer

class SpeakerViewSets(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

class MotherboardViewSets(viewsets.ModelViewSet):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer

class ProcessorViewSets(viewsets.ModelViewSet):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer

class ComputerViewSets(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

    def create(self, request, *args, **kwargs):
        pc = super().create(request, *args, **kwargs)
        if pc.data['id'] is not None:
            return pc   
        else:
            return Response({'message': 'Falta stock'})

class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
