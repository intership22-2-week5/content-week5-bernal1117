#Django rest framework 
from rest_framework.views import Response
from rest_framework import viewsets

from .serializers import DispEntrySerializer, MouseSerializer, KeyboardSerializer, MonitorSerializer, ComputerSerializer, OrderSerializer

#models
from .models import DispEntry, Mouse, Keyboard, Monitor, Computer, Order

class DispEntryViewSets(viewsets.ModelViewSet):
    queryset = DispEntry.objects.all()
    serializer_class = DispEntrySerializer

class MouseViewSets(viewsets.ModelViewSet):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer

class KeyboardViewSets(viewsets.ModelViewSet):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer

class MonitorViewSets(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer

class ComputerViewSets(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
