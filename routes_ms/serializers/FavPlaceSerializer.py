from rest_framework import serializers
from routes_ms.models import FavPlace

class FavPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavPlace
        fields = '__all__'
    
    def create(self, validated_data):
        favPlace = FavPlace(name = validated_data['name'],
                            latitude = validated_data['latitude'],
                            longitude = validated_data['longitude'],
                            userId = validated_data['userId'])
        favPlace.save()
        return favPlace