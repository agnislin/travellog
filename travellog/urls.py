from django.urls import path
from . import views

urlpatterns = [
    path('', views.visit, name="login"),
    path('visit/', views.visit, name="visit"),
    path('uploadAlbum/', views.uploadAlbum, name="uploadAlbum"),


    path('clear/', views.clear_database, name='clear_database'),
    path('progress-bar-upload/', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
]
