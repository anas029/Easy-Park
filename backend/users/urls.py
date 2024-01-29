from django.urls import path

from .views import (CustomObtainAuthTokenView, LogoutView, UserCreateAPIView,
                    UserRetrieveUpdateAPIView)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('token/', CustomObtainAuthTokenView.as_view(), name='token'),
    path('profile/', UserRetrieveUpdateAPIView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
