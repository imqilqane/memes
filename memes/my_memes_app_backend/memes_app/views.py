from rest_framework import generics, serializers,  status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Meme
from .serializers import MyMemeSerializer, CreatMemeSerializer
from .permissions import IsOwner
# Create your views here.


class ListMyMemesAPIView(generics.ListAPIView):
    serializer_class = MyMemeSerializer

    def get_queryset(self):
        return Meme.objects.filter(user=self.request.user)


class CreateMemeAPIView(APIView):
    serializer_class = CreatMemeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            obj.user = request.user
            obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateMemeAPIView(generics.UpdateAPIView):
    queryset = Meme.objects.all()
    serializer_class = MyMemeSerializer
    permission_classes = [IsOwner, ]
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Your Meme updated successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "failed", "details": serializer.errors}, status=status.HTTP_404_NOT_FOUND)


class DeleteMemeAPIView(generics.DestroyAPIView):
    permission_classes = [IsOwner, ]
    serializer_class = MyMemeSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Meme.objects.filter(
            id=self.kwargs['pk'])
        return queryset
