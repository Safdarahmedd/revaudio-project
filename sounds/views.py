from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SoundSerializer


@api_view(['POST',])
def SoundView (request):
    if  request.method == 'POST':
        serializer = SoundSerializer(data=request.data)
        data = request.data        
        if serializer.is_valid():
            sound = serializer.create(serializer.validated_data)
        else:
            data = serializer.errors
        return Response(sound)

    