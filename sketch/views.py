import datetime

from django.http import HttpResponse
from django.shortcuts import render,redirect, render_to_response

# Create your views here.
from django.template import loader

from sketch.models import Note
from django.contrib import auth



def dateNav(request):

    return render(request,"sketch/dateNav.html")

def note(request):
    arrayWeekday = []
    today = datetime.date.today()
    sunday = today - datetime.timedelta(today.weekday())
    for i in range(7):
        tmp_date = sunday + datetime.timedelta(i)
        arrayWeekday.append(tmp_date.strftime('%A %x'))


    usernames = auth.get_user(request).username
    notes = Note.objects.filter(note_user_id= request.user, notes_date=datetime.date.today())
    context = {
        "notes": notes,
        "username": usernames,
        "date":arrayWeekday
    }
    return render(request, "sketch/notes.html", context)


def add_note(request):
    return render(request,"sketch/add.html")

def add(request):
    print(request.POST)
    note = Note(notes_title = request.POST['notes_title'],notes_description = request.POST['notes_description'],notes_time = request.POST['notes_time'], notes_date = request.POST['notes_date'],notes_priority = request.POST['notes_priority'])
    note.save()
    return redirect("/user/note")


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

