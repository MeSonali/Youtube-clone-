from django.urls import path
from .views import home



urlpatterns = [
    path('youtube/',home,name = "home")
]
