from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import OrdersTB
from .Serializers import UserSerializers
@api_view(['GET'])
def all_orders(req):
    orders=OrdersTB.objects.all()
    try:
        if orders:
            ord=UserSerializers(orders,many=all)
            return Response({'all_orders':ord.data})
    except FileNotFoundError:
        return Response({'Empty':'no orders exist'})

@api_view(['GET'])
def get_order(req, id):
    try:
        order = OrdersTB.objects.get(id=id)
        serializer = UserSerializers(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except OrdersTB.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'PATCH'])
def update_order(req, id):
    try:
        order = OrdersTB.objects.get(id=id)
        partial_update = req.method == 'PATCH'
        serializer = UserSerializers(order, data=req.data, partial=partial_update)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': 'Successfully updated',
                    'updated_order': serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                'status': 'Invalid data',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    except OrdersTB.DoesNotExist:
        return Response({'status': 'Invalid ID'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_order(req,id):
    try:
        idd=OrdersTB.objects.get(id=id)
        ord=UserSerializers(idd)
        idd.delete()
        return Response({'status':'Oreder is deleted','DELETED-ORDER':ord.data},status=status.HTTP_200_OK)
    except OrdersTB.DoesNotExist:
        return Response({'Status':'invalid Id','msg':'enter valid id'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_order(req):
    se=UserSerializers(data=req.data)
    if se.is_valid():
        se.save()
        return Response({'status':'ORDER is created','Order':se.data},status=status.HTTP_201_CREATED)
    return Response({'error':'enter valid order details','errors':se.errors},status=status.HTTP_204_NO_CONTENT)