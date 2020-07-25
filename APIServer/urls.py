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
from django.urls import include
# Jess

# Larios
from core import views
# Miguel

# Sandy

urlpatterns = [
    path('admin/', admin.site.urls),
    # Jess
    path('', include('commentary.urls')),
    # Larios
    path('', include('establecimientos.urls') ),
    path('', views.home, name="home"),
    path('accounts/', include('django.contrib.auth.urls') ),
    # Miguel
    path('', include('api.urls')),
    # Sandy
    path('', include('producto.urls')),
]

# Larios
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Configuraciones para titulos en el admin
admin.site.site_header = "TLAKUALI UELIK"
admin.site.index_title = "Panel administrativo"
admin.site.site_title = "Tlakuali Uelik"