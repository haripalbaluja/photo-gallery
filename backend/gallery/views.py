from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AbstractSerializer, ScenicSerializer, StreetSerializer, MessageSerializer
from .models import Abstract, Scenic, Street, Message
# Create your views here.

class AbstractView(viewsets.ModelViewSet):
    serializer_class = AbstractSerializer
    queryset = Abstract.objects.all()

class ScenicView(viewsets.ModelViewSet):
    serializer_class = ScenicSerializer
    queryset = Scenic.objects.all()

class StreetView(viewsets.ModelViewSet):
    serializer_class = StreetSerializer
    queryset = Street.objects.all()    

class MessageView(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()    
