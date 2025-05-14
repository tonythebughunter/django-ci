from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('assignments/', views.postView, name='assignment')
]