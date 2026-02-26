from .views import indexView, aboutView, saveData, deleteNote
from django.urls import path


urlpatterns = [
  path("", indexView, name="home"),
  path("about", aboutView, name="about"),
  path("save-data", saveData, name='save_data'),
  path("delete-note/<int:id>", deleteNote, name='delete_note'),
]