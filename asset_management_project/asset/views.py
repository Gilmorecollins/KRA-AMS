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
def assetApi(request):
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


@api_view(['GET', 'PUT', 'DELETE'])
def assetApiView(request, pk):
    try:
        asset = Asset.objects.get(pk=pk)

    except Asset.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        asset_serializer = AssetSerializer(asset)
        return Response(asset_serializer.data)

    elif request.method == 'PUT':
        asset_serializer = AssetSerializer(asset, data=request.data)

        if asset_serializer.is_valid():
            asset_serializer.save()
            return Response(asset_serializer.data)
        return Response(asset_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

