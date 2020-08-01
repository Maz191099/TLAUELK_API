from rest_framework import viewsets
from .models import Promotions
from .serializer import PromotionsSerializer

class PromotionsViewSet(viewsets.ModelViewSet):
    queryset = Promotions.objects.all()
    serializer_class = PromotionsSerializer 