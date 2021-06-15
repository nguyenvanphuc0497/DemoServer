from django.urls import path

from game import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play/<room_code>', views.game),
]
