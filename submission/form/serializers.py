from rest_framework import serializers
from .models import SendMessage
class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendMessage
        fields= ["id","name","email","message"]
        read_only_fields = ("id",)