from django.shortcuts import render

# Create your views here.
# events/views.py
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter(date_time__gte=timezone.now())
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

from rest_framework import viewsets
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework import serializers
from .models import Category
from .serializers import CategorySerializer
from django.core.mail import send_mail

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter(date_time__gte=timezone.now())
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        event = serializer.validated_data['event']
        if event.capacity > 0:
            event.capacity -= 1
            event.save()
            serializer.save(user=self.request.user)
        else:
            raise serializers.ValidationError("Event is fully booked")

class CategoryViewSet(viewsets.ModelViewSet): 
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer

class EventViewSet(viewsets.ModelViewSet): 
    ... 
    def perform_create(self, serializer): 
        serializer.save(organizer=self.request.user) 
        send_mail( 'Event Created', 
                  'Your event has been created successfully.',
                    'from@example.com', 
                    [self.request.user.email], 
                    fail_silently=False,
                      )