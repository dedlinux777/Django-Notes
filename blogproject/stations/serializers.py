from rest_framework import serializers
from .models import Station

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

    # C. Validation Logic: Ensure temperature is within a realistic range
    def validate_temperature(self, value):
        if value < -50 or value > 60:
            raise serializers.ValidationError("Temperature out of valid sensor range.")
        return value