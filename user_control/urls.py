from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import UserViewSet,UserProfileViewSet

myrouter = DefaultRouter(trailing_slash=False)

myrouter.register('users', UserViewSet,'user_control')
myrouter.register('user-profile', UserProfileViewSet,'user_profile_control')



urlpatterns = [
    path('', include(myrouter.urls)),
]