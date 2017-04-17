import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


from django.shortcuts import render,redirect, render_to_response
from django.template import RequestContext

from sketch.forms import EditProfileForm, EditProfileMoreForm
from sketch.models import Note
from django.contrib import auth

@login_required
def note(request):
    arrayWeekday = []
    dayWeekday = []
    today = datetime.date.today()
    sunday = today - datetime.timedelta(today.weekday())

    for i in range(7):
        tmp_date = sunday + datetime.timedelta(i)
        arrayWeekday.append(tmp_date.strftime('%A %d.%m.%Y'))
        dayWeekday.append(tmp_date.strftime( '%Y-%m-%d'))

    usernames = auth.get_user(request).username
    notes_1 = Note.objects.filter(note_user_id = request.user, notes_date__exact= dayWeekday[0])
    notes_2 = Note.objects.filter(note_user_id=request.user, notes_date__exact=dayWeekday[1])
    notes_3 = Note.objects.filter(note_user_id=request.user, notes_date__exact=dayWeekday[2])
    notes_4 = Note.objects.filter(note_user_id=request.user, notes_date__exact=dayWeekday[3])
    notes_5 = Note.objects.filter(note_user_id=request.user, notes_date__exact=dayWeekday[4])
    notes_6 = Note.objects.filter(note_user_id=request.user, notes_date__exact=dayWeekday[5])
    notes_7 = Note.objects.filter(note_user_id=request.user, notes_date__exact=dayWeekday[6])

    context = {
        "notes_1": notes_1,
        "notes_2": notes_2,
        "notes_3": notes_3,
        "notes_4": notes_4,
        "notes_5": notes_5,
        "notes_6": notes_6,
        "notes_7": notes_7,
        "username": usernames,
        "date":arrayWeekday,
        'testday':dayWeekday[0],
    }
    return render(request, "sketch/notes.html", context)


def add_note(request):
    return render(request,"sketch/add.html")

def add(request):
    print(request.POST)
    note = Note(notes_title=request.POST['notes_title'], notes_description=request.POST['notes_description'],
                notes_time=request.POST['notes_time'], notes_date=request.POST['notes_date'],
                notes_priority=request.POST['notes_priority'])
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
    return redirect('/user/note')

def destroy(request, id):
    note = Note.objects.get(id = id)
    note.delete()
    return redirect('/user/note')

@login_required
def view_profile(request):
    return render(request,'profile/base.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profileUserEdit = EditProfileForm(request.POST, instance = request.user)
        profileMoreEdit = EditProfileMoreForm(request.POST,request.FILES, instance=request.user.profile)
        if profileUserEdit.is_valid() and profileMoreEdit.is_valid():
            profileUserEdit.save()
            profileMoreEdit.save()
            return redirect('/user/profile')
    else:
        profileUserEdit = EditProfileForm(instance=request.user)
        profileMoreEdit = EditProfileMoreForm(instance=request.user.profile)
        context = {'profileEdit':profileUserEdit,'profileMore':profileMoreEdit}
        return render(request, 'profile/profile_edit.html', context)