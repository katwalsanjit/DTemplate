from .views import indexView, aboutView, saveData
from django.urls import path


urlpatterns = [
  path("", indexView, name="home"),
  path("about", aboutView, name="about"),
  path("save-data", saveData, name='save_data')

]