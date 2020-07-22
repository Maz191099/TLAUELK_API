from .views import Register, Login
from django.urls import path
from knox import views as knox_views
urlpatterns = [
    path('register/', Register.as_view(), name="regster"),
    path('login/', Login.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
]
