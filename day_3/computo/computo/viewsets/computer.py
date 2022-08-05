from rest_framework import viewsets
from rest_framework.views import Response

from ..models.computer import Computer
from ..serializers.computer import ComputerSerializer

class ComputerViewSets(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

    def create(self, request, *args, **kwargs):
        pc = super().create(request, *args, **kwargs)
        if pc.data['id'] is not None:
            return pc   
        else:
            return Response({'message': 'Falta stock'})