from rest_framework import serializers
from .models import *
from product.serializer import *



class OrdrItemSerializer(serializers.ModelSerializer):
    items = createPRODUCTSerializer(read_only=True, many=True)
    product = ProductName(read_only=True, many=True)
    class Meta:
        model = OrderItem
        fields = ['product', 'price', 'size', 'quantity', 'items']

class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    refrence = OrdrItemSerializer(read_only=True, many=True)
    class Meta:
        model = Order
        fields = ['ref_code', 'owner', 'is_ordered', 'date_ordered', 'refrence']