from rest_framework import viewsets

from ..models.component import Component, InternalDevice, DispEntry, DispOutput, Monitor, Motherboard, Mouse, Speaker, Keyboard, Processor
from ..serializers.component import DispEntrySerializer, DispOutputSerializer, InternalDeviceSerializer, MouseSerializer, KeyboardSerializer, MonitorSerializer, SpeakerSerializer, MotherboardSerializer, ProcessorSerializer



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