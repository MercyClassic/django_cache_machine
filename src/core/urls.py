from django.urls import path

from core import views

urlpatterns = [
    path('cache_machine', views.CreateCheckAPIView.as_view()),
]
