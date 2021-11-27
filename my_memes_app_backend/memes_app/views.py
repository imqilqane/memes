from rest_framework import generics,  status
from rest_framework.response import Response
from .models import Meme
from .serializers import MyMemeSerializer

# Create your views here.


class ListMyMemesAPIView(generics.ListAPIView):
    serializer_class = MyMemeSerializer

    def get_queryset(self):
        return Meme.objects.all()


class CreateMemeAPIView(generics.CreateAPIView):
    serializer_class = MyMemeSerializer
    queryset = Meme.objects.all()


class UpdateMemeAPIView(generics.UpdateAPIView):
    queryset = Meme.objects.all()
    serializer_class = MyMemeSerializer
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
    serializer_class = MyMemeSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Meme.objects.filter(
            id=self.kwargs['pk'])
        return queryset
