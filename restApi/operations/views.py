from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Programer
from .serializers import ProgramerSerializer

from django.db.models import Q


# Create your views here.


@api_view(["GET"])
def endPoint(request):
    data = ["/programers", "programers/:username"]
    return Response(data)


@api_view(["GET","POST"])
def programer_list(request):
    if request.method == "GET":
        query = request.GET.get("query")
        if query == None:
            query = ""
            programers = Programer.objects.filter(
                Q(username__icontains=query) | Q(bio__icontains=query)
            )
            serializer = ProgramerSerializer(programers, many=True)
            return Response(serializer.data)
    if request.method == "POST":
        programers = Programer.objects.create(
            username=request.data["username"], bio=request.data["bio"]
        )
        serializer = ProgramerSerializer(programers, many=False)
        return Response(serializer.data)
