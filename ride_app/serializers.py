from rest_framework import serializers
from .models import Ride

class RideSerializer(serializers.ModelSerializer):
    rider = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ride
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('rider', 'pickup_location','dropoff_location'),
                message="You already have a ride with this pickup and dropoff location"
            )
        ]

    def create(self, validated_data):
        validated_data['rider'] = self.context['request'].user
        return super().create(validated_data)