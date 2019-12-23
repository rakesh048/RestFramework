from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from .views import *

urlpatterns = [
    # Your URLs...
    path('login/', LoginView.as_view(), name='login_user'),
    path('refresh_token/', refresh_jwt_token, name='token_refresh'),
    path('verify_token/', verify_jwt_token, name='verify_refresh'),
]