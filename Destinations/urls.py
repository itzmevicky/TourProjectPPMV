from django.urls import path
from Destinations import views
urlpatterns = [
    path("",views.index,name = "Home")
]