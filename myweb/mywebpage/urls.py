from django.urls import path
from mywebpage import views

urlpatterns = [
    path("", views.myHomepage, name="myHomepage"),
]
