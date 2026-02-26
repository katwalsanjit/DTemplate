from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Note

# Create your views here.
def indexView(request):
  notes = Note.objects.all()
  return render(request, 'index.html', context={
    'notes':notes
  })

def aboutView(request):
  return render(request, 'about.html')

def saveData(req):
  title = req.POST.get("title","")
  description = req.POST.get("description","")

  if not title or not description:
    messages.error(req, "Fill All Details in the form.")
    return redirect('/')
  
  note = Note(title=title,description=description)
  note.save()
  messages.success(req, "Detail saved")
  return redirect("/")


def deleteNote(req,id):
  note = Note.objects.get(id=id)
  note.delete()
  messages.success(req, 'Note Deleted')
 
  return redirect("/")