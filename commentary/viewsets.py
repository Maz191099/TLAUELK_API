from rest_framework import viewsets
from .models import Commentary
from .serializer import CommentarySerializer

class CommentaryViewSet(viewsets.ModelViewSet):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer 