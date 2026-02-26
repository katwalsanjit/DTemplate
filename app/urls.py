from .views import indexView, aboutView, saveData, deleteNote, updateNote
from django.urls import path


urlpatterns = [
  path("", indexView, name="home"),
  path("about", aboutView, name="about"),
  path("save-data", saveData, name='save_data'),
  path("delete-note/<int:id>", deleteNote, name='delete_note'),
  path("update-note/<int:id>", updateNote, name='update_note'),
]