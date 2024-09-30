from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
class SimpleApi(APIView):
    def get(self, request):
        data = {"message": "HEllo, this is a sample message", "status": "success"}
        return Response(data, status=status.HTTP_200_OK)
