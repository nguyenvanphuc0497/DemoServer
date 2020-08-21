from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.view_list, name="view_list"),
    path('detail/<int:question_id>', views.detail_view, name="detail"),
    path('<int:question_id>', views.vote, name="vote"),
]
