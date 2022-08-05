from rest_framework import viewsets
from rest_framework.views import Response

from ..models.order import Order, Detailsorder
from ..serializers.order import OrderSerializer, DetailsOrderSerializer

class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DetailsOrderViewSets(viewsets.ModelViewSet):
    queryset = Detailsorder.objects.all()
    serializer_class = DetailsOrderSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    """
    def create(self, request, *args, **kwargs):
        pc = super().create(request, *args, **kwargs)
        if pc.data['id'] is not None:
            return pc   
        else:
            return Response({'message': 'Falta stock en computers'})
    """