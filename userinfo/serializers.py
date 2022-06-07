from rest_framework import serializers
from .models import *

class infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = info
        fields = (
            "first_name",
            "last_name",
            "Phone_number",
            "email",
            "message",
        )