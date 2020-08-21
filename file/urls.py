from django.urls import path

from . import views

app_name = "file"

urlpatterns = [
    path('download/<str:file_name>', views.download_file, name="download"),
    path('upload', views.model_form_upload, name="upload"),
]
