from rest_framework import serializers
from routes_ms.models import Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
    
    def create(self, validated_data):
        record = Record(date = validated_data['date'],
                        startLatitude = validated_data['startLatitude'],    
                        startLongitude = validated_data['startLongitude'],
                        endLatitude = validated_data['endLatitude'],
                        endLongitude = validated_data['endLongitude'],
                        startAddress = validated_data['startAddress'],
                        endAddress = validated_data['endAddress'],
                        userId = validated_data['userId'])
        record.save()
        return record
    