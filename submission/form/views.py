from django.shortcuts import render
from .serializers import SendMessageSerializer
from .models import SendMessage
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class MessagesView(APIView):
    def get(self, request):
        messages = SendMessage.objects.all()
        serialized_items = SendMessageSerializer(messages,many=True)
        return Response(serialized_items.data,status.HTTP_200_OK)
    def post(self,request):
        serializer = SendMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status.HTTP_201_CREATED)