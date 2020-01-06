from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from .views import *

urlpatterns = [
    # Your URLs...
    path('register/', RegisterView.as_view(), name='register_user'),
    path('login/', LoginView.as_view(), name='login_user'),
    path('refresh_token/', RefreshToken.as_view(), name='token_refresh'),
    path('verify_token/', VerifyToken.as_view(), name='verify_refresh'),
]