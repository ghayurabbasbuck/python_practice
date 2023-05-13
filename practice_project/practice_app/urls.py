from django.urls import path
from . import views

urlpatterns = [
    path("ghayur/",views.index,name = "index"),
]
