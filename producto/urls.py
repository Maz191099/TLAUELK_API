from django.urls import path
# Jess

# Larios

# Miguel

# Sandy
from rest_framework import routers
from .viewsets import ProductViewSet

route = routers.SimpleRouter()
route.register('producto', ProductViewSet)


urlpatterns = route.urls
    
    # Jess

    # Larios

    # Miguel

    # Sandy


