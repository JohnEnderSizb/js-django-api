from . import views
from django.urls import path

app_name = 'sentiment_analysis'
urlpatterns = [
    path('', views.sentimentResults, name='index'),
]
