from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_of_speaker, name='list_of_speaker'),
    path('create/', views.create_speaker, name='create_speaker'),
    path('<int:speaker_id>/', views.detail_of_speaker, name='detail_of_speaker'),
    path('<int:speaker_id>/update/', views.update_speaker, name='speaker)
]
    