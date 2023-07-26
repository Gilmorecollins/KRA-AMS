from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics



from .models import User, Department, Station, Section
from .serializer import UserSerializer, DepartmentSerializer, SectionSerializer, StationSerializer



class DepartmentList(APIView):
    def get(self, request, format=None):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentDetail(APIView):
    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        department= self.get_object(pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        department = self.get_object(pk)
        department.delete()
        return Response(satatus=status.HTTP_204_NO_CONTENT)
    

class StationListCreateAPIView(generics.ListCreateAPIView):
    stations = Station.objects.all()
    serializer_class = StationSerializer


class StationRetreiveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    station = Station.objects.all()
    serializer_class = StationSerializer


        
