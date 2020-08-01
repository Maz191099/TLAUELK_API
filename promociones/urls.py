from django.urls import path
from rest_framework import routers

from .viewsets import PromotionsViewSet

# Jess

# Larios

route = routers.SimpleRouter()
route.register('promotions', PromotionsViewSet)

# Miguel

# Sandy


urlpatterns = route.urls
    #path('admin/', admin.site.urls),
    # Jess

    # Larios

    # Miguel

    # Sandy


