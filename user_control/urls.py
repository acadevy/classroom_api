from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import UserViewSet,UserProfileViewSet,StudentViewSet,TeacherViewSet,FileUploadViewSet


myrouter = DefaultRouter(trailing_slash=False)

myrouter.register('users', UserViewSet,'user_control')
myrouter.register('user-profile', UserProfileViewSet,'user_profile_control')
myrouter.register('student', StudentViewSet,'student_control')
myrouter.register('teacher', TeacherViewSet,'teacher_control')
myrouter.register('file-upload', FileUploadViewSet,'file_upload_control')




urlpatterns = [
    path('', include(myrouter.urls)),
    
]