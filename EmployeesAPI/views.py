from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializers import EmployeesAPISerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
import json
from rest_framework.decorators import api_view
class EmployeesList(APIView):
    def get(self,request):
        emp=Employees.objects.all()
        serializer=EmployeesAPISerializer(emp,many=True)
        return Response(serializer.data)

   
        


@api_view(['GET', 'POST', 'DELETE'])
def insertRecord(request):

 
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =EmployeesAPISerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def updateRecord(request, pk):
    emp=Employees.objects.get(pk=pk)
    if request.method == 'PUT': 
        data = JSONParser().parse(request) 
        serializer = EmployeesAPISerializer(emp, data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors)


@api_view(['GET', 'POST', 'DELETE'])
def deleteRecord(request,pk):
    
    
    if request.method == 'DELETE':
        count = Employees.objects.get(pk=pk).delete()
        return Response({'Message': 'Record is deleted successfully!'})