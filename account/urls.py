from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register('sign_up', views.UserRegistrationAPIView)

urlpatterns = [
    path('sign_up/', views.UserRegistrationAPIView.as_view(), name='user_registration'),
    path('login/', views.UserLoginAPIView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
]
