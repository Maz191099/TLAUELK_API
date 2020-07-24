from rest_framework import viewsets
from .models import Gallery
from .serializer import GallerySerializer

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer 