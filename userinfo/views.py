from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework import status
# Create your views here.

# @csrf_exempt 
# class storeInfo(APIView):
#     # print(request.data)
#     serializer=infoSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(status.HTTP_201_CREATED)
#     return Response(status.HTTP_400_BAD_REQUEST)


class infoList(APIView):
    def get(self,request,format=None):
        products=info.objects.all()
        serializer=infoSerializer(products,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
            # print(request.data)
            serializer=infoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status.HTTP_201_CREATED)
            return Response(status.HTTP_400_BAD_REQUEST)