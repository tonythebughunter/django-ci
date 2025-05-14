from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('students/', views.student_view, name='students'),
]
