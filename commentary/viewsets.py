from .models import Commentary
from .serializer import CommentarySerializer
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class CommentaryViewSet(viewsets.ModelViewSet):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer 
    
    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Commentary.objects.filter(id_establecimiento=pk).order_by('-score')
        serializer = CommentarySerializer(queryset,many= True)
        return Response(serializer.data)