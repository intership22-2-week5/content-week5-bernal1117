from rest_framework import serializers

from ..models.computer import Computer
from ..models.order import Order, Detailsorder


class OrderSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Order
    fields = '__all__' 
    #exclude = ('id','author','category') #Que muestre todo menos los datos especificados
    #fields = ['title', 'author', 'category'] #Solo muestra los datos especificados
  
  def to_representation(self, instance):  #Con esto mostramos lo que necesitemos
    return {
      'id': instance.id,
      'description':instance.description,
      'created_at': instance.created_at,
      'status': instance.status
      
    }

class DetailsOrderSerializer(serializers.ModelSerializer):

  order = serializers.PrimaryKeyRelatedField(queryset = Order.objects.all())
  computer = serializers.PrimaryKeyRelatedField(queryset = Computer.objects.all())
  class Meta:
    model = Detailsorder
    fields = '__all__'
  

  def to_representation(self, instance):
    return {
      'id_details_order': instance.id,
      'quantity_computers_order': instance.quantity,
      'total_cost_order': instance.total_cost_order,
      'order': {
        'description': instance.order.description,
        'created_at': instance.order.created_at
      },
      'computer': {
        'description': instance.computer.description,
        'cost_per_computer': instance.computer.total_cost
      }
    }
