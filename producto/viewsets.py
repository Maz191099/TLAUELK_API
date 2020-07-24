from .models import Product
from .serializer import ProductSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class  ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Product.objects.filter(id_establishment=pk)
        serializer = ProductSerializer(queryset,many= True)
        return Response(serializer.data)