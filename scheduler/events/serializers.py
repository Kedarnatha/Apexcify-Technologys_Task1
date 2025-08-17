from rest_framework import serializers
from .models import Event
from datetime import date

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'date', 'description']

    def validate_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Event date cannot be in the past.")
        return value
