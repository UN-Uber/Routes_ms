from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from routes_ms.models import Record
from routes_ms.serializers import RecordSerializer

class RecordView(APIView):
    def get_list(self):
        records = Record.objects.all()
        return records
    
    def get(self, request, *args, **kwargs): 
        idRecord = request.query_params.get('id', None)
        if (idRecord != None):
            record = Record.objects.get(id=idRecord)
            serializer = RecordSerializer(record)   
        else:
            record = self.get_list()
            serializer = RecordSerializer(record, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        idRecord = request.query_params.get('id', None)
        if (idRecord != None):
            record = Record.objects.get(id=idRecord)
            record.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class RecordUserView(APIView):
    def get(self, request, *args, **kwargs):
        userId = request.query_params.get('userId',None)
        if (userId != None):
            records = Record.objects.filter(userId=userId)
            serializer = RecordSerializer(records, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        userId = request.query_params.get('userId',None)
        if (userId != None):
            records = Record.objects.filter(userId=userId)
            records.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
