from rest_framework import serializers
from .models import Programer


class ProgramerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programer
        fields = "__all__"
