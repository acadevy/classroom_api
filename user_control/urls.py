from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import UserViewSet

myrouter = DefaultRouter(trailing_slash=False)

myrouter.register('users', UserViewSet,'user_control')



urlpatterns = [
    path('', include(myrouter.urls)),
]