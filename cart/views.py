from typing import OrderedDict
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from account.models import *
from cart.serializer import OrderSerializer, OrdrItemSerializer
from product.serializer import *
from rest_framework.response import Response
from .models import *
from product.serializer import createPRODUCTSerializer
# Create your views here.

@api_view(['GET'])
def get_cart_usr(request,pk):
    if request.method == 'GET':
        # user_profile = get_object_or_404(Profile, user=request.user)
        # print(user_profile)
        # order = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
        # print(order)
        # usr = get_object_or_404(Profile, user=request.user)
        # item = Product.objects
        # print(item)
        #order_item = OrderItem.objects.get(items=item)
        #usr_order = Order.objects.get_or_create(owner=usr, is_ordered=False)
        #item.items().add(order_item)
        #order.refrence.add(order_item)

        # order = Order.objects.get(
        #     owner=request.user.profile, is_ordered=False)
        # item = Product.objects.filter(pk=pk).first()
        # order_item= OrderItem.objects.filter(
        # product=item
        # )
        # order.refrence.add(order_item)
        # if order.refrence.filter(id=pk).exists():
        #     order_item.quantity += 1
        #     order_item.save()
        # context = {'object': order}
        user_profile = get_object_or_404(Profile, user=pk)
        print(user_profile)
        order = Order.objects.filter(owner=user_profile, is_ordered=False).first()
        order_item =OrderItem.objects.filter(refrence_id=order.id)
        print(order_item)
        # order.refrence.add(order_item)
        print(order)
        serializer = OrdrItemSerializer(data=order_item, many=True)
        serializer.is_valid(raise_exception=False)
        return Response(serializer.data)