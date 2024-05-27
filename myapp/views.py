from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_function_view(request):
    return Response({"message": "This is a protected view"})

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected view"})

class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

class AllRoomsListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

class RoomUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]
    partial = True

class RoomDeleteView(generics.DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Room deleted successfully"})
