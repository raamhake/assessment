from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('schedule/', views.movie_schedule, name='movie_schedule'),
]
