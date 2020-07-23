"""APIServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# Jess
from django.urls import include
# Larios

# Miguel
from django.urls import include
# Sandy


urlpatterns = [
    path('admin/', admin.site.urls),
    # Jess
    path('commentary/', include('commentary.urls')),
    # Larios
<<<<<<< HEAD
<<<<<<< HEAD
    path('', include('establecimientos.urls') ),
=======
     path('', include('establecimientos.urls') ),
>>>>>>> larios
=======
    path('establishment/', include('establecimientos.urls') ),
>>>>>>> a4ae167347b08be8654f44e3a45b3d519574d6b2
    # Miguel
    path('', include('api.urls')),
    # Sandy
    path('apiproducto/', include('producto.urls')),
]

# Larios
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
