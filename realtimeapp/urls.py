from django.urls import path
from realtimeapp import views

urlpatterns = [
    path('realtimeapp/', views.alert)
]