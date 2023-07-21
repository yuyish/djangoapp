
from django.urls import path
from .views import homepage,create

urlpatterns = [
    path("", homepage,name="Home"),
    path("create/",create)
]