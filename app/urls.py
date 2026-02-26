from .views import indexView, aboutView
from django.urls import path


urlpatterns = [
  path("", indexView, name="home"),
  path("about", aboutView, name="about"),
]