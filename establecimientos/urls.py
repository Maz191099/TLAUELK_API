from django.urls import path
from rest_framework import routers

from .viewsets import EstablishmentViewSet

# Jess

# Larios

route = routers.SimpleRouter()
route.register('establishment', EstablishmentViewSet)

# Miguel

# Sandy


urlpatterns = route.urls
    #path('admin/', admin.site.urls),
    # Jess

    # Larios

    # Miguel

    # Sandy


