from rest_framework import viewsets
from .models import Establishment
from .serializer import EstablishmentSerializer

class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer 