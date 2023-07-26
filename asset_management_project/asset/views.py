from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


#importing the models created
from .models import Station, Department, Section, User, Asset, Ticket, DeployedAsset
from .serializers import StationSerializer, DepartmentSerializer, SectionSerializer, UserSerializer, AssetSerializer,\
    TicketSerializer, DeployedAssetSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def assetApi(request, id=0):
    if request.method == 'GET':
        asset = Asset.objects.all()
        asset_serializer = AssetSerializer(asset, many=True)
        return Response(asset_serializer.data)

    elif request.method == 'POST':
        # asset_data = JSONParser().parse(request)
        asset_serializer = AssetSerializer(data=request.data)

        if asset_serializer.is_valid():
            asset_serializer.save()
            return Response(asset_serializer.data, status=status.HTTP_201_CREATED)
        return Response(asset_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        asset_data = JSONParser().parse(request)
        asset = Asset.objects.get(serial_number=asset_data['serial_number'])
        asset_serializer = AssetSerializer(asset, data=asset_data)

        if asset_serializer.is_valid():
            asset_serializer.save()
            return JsonResponse('Asset Update Successfully', safe=False)
        return JsonResponse('Failed to Update Asset')

    elif request.method == 'DELETE':
        asset = Asset.objects.get(serial_number=id)
        asset.delete()
        return JsonResponse('Deleted Successfully', safe=False)

