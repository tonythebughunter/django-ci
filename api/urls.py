from django.urls import path
from . import views
urlpatterns = [
    path('students/', views.studentApiView),
    path('posts/', views.postApiView)
]