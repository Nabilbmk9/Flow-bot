from django.urls import path
from . import views

urlpatterns = [
    path('authentication/api/', views.LeadListCreate.as_view()),
]