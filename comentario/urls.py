from django.urls import path
from rest_framework import routers
from .viewsets import CommentaryViewSet
# Jess
route = routers.SimpleRouter()
route.register('commentary', CommentaryViewSet)
# Larios

# Miguel

# Sandy



    #path('admin/', admin.site.urls),
    # Jess
urlpatterns = route.urls
    # Larios

    # Miguel

    # Sandy 