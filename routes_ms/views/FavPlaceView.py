from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from routes_ms.models import FavPlace
from routes_ms.serializers import FavPlaceSerializer

class FavPlaceView(APIView):
    def get_list(self):
        favPlaces = FavPlace.objects.all()
        serializer = FavPlaceSerializer(favPlaces, many=True)
        return Response(serializer.data)
    
    def get(self, request, *args, **kwargs):
        id = request.query_params['id']
        if (id != None):
            place = FavPlace.objects.get(id=id)
            serializer = FavPlaceSerializer(place)
            return Response(serializer.data)
        else:
            return self.get_list(request, *args, **kwargs)

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

