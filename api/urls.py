from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    path('docs/', views.documents.index),
    path('docs/create', views.documents.create),
]
