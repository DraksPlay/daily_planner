from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('auth/', include('django.contrib.auth.urls')),
    path("signup/", SignUp.as_view(), name="signup"),
]
