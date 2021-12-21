from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from routes_ms.models import FavPlace
from routes_ms.serializers import FavPlaceSerializer

class FavPlaceView(APIView):
    def get_list(self):
        favPlaces = FavPlace.objects.all()
        return favPlaces
    
    def get(self, request, *args, **kwargs):
        
        idPlace = request.query_params.get('id', None)
        if (idPlace != None):
            place = FavPlace.objects.get(id=idPlace)
            serializer = FavPlaceSerializer(place)   
        else:
            place = self.get_list()
            serializer = FavPlaceSerializer(place, many=True)
        return Response(serializer.data)
            

    def post(self, request, *args, **kwargs):
        serializer = FavPlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        id = request.query_params['id']
        if (id != None):
            place = FavPlace.objects.get(id=id)
            place.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class FavPlaceUserView(APIView):
    def get(self, request, *args, **kwargs):
        userId = request.query_params.get('userId',None)
        if (userId != None):
            favPlaces = FavPlace.objects.filter(userId=userId)
            serializer = FavPlaceSerializer(favPlaces, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        userId = request.query_params['userId']
        if (userId != None and id != None):
            favPlaces = FavPlace.objects.filter(userId=userId)
            favPlaces.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

