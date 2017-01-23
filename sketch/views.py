from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .forms import AddForm
# Create your views here.
from sketch.models import Note
from sketch.forms import AddForm



def note(request):
    notes = Note.objects.all()
    context = {
        "notes": notes
    }
    return render(request, "sketch/notes.html", context)



def add_note(request):
    return render(request,"sketch/add.html")

def add(request):
    print(request.POST)
    note = Note(notes_title = request.POST['notes_title'],notes_description = request.POST['notes_description'],notes_date = request.POST['notes_date'],notes_priority = request.POST['notes_priority'])
    note.save()
    return redirect("/")


def edit(request, id):
    note = Note.objects.get(id = id)
    context = {"note":note}
    return render(request, "sketch/edit.html", context)

def update(request, id):
    note = Note.objects.get(id = id)
    note.notes_title = request.POST['notes_title']
    note.notes_description = request.POST['notes_description']
    note.notes_date = request.POST['notes_date']
    note.notes_priority = request.POST['notes_priority']
    note.save()
    return redirect('/')

def destroy(request, id):
    note = Note.objects.get(id = id)
    note.delete()
    return redirect('/')