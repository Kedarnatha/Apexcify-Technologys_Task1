from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer
from django.http import HttpResponse

# API ViewSet
class EventViewSet(viewsets.ViewSet):
    def list(self, request):
        events = Event.objects.all().order_by('date')
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Home view
def home(request):
    return HttpResponse("Welcome to the Event Scheduler!")
