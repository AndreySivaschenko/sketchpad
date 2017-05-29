import datetime
import time
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse

from django.shortcuts import render,redirect, render_to_response
from django.template import RequestContext

from sketch.forms import EditProfileForm, EditProfileMoreForm
from sketch.models import Note
from django.contrib import auth
from Holidays.models import holidays
from django.conf import settings

@login_required
def note(request):

    arrayWeekday = []
    dayWeekday = []
    today = datetime.date.today()
    sunday = today - datetime.timedelta(today.weekday())
    today = datetime.date.today().strftime('%Y-%m-%d')
    times = time.strftime("%H:%M", time.localtime())
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


    try:
        user = User.objects.get(username=request.user)
        date = Note.objects.get(note_user_id=request.user, notes_time=times, notes_date=today)
        if(date):
            send_mail("SketchPad - Напоминание",
                      "Вам пришло это письмо потому,что вы запланировали на " + today + "в " + times + "дело.",
                      settings.EMAIL_HOST_USER, [user.email])
    except Note.DoesNotExist:
        date = 'Событий нет'

    try:
        holiday = holidays.objects.get(holidays_days=datetime.date.today())
    except holidays.DoesNotExist:
        holiday = "Праздников нет! Иди работай."

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
        'holiday':holiday,
        'today':today,
        "dayCheck":date,
        "todayDay": today,
        "todayTime": times,
    }
    return render(request, "sketch/notes.html", context)

def check_event(request):
    today = datetime.date.today()
    times = time.strftime("%H:%M", time.localtime())
    date = Note.objects.filter(note_user_id=request.user, notes_date=datetime.date.today(),
                               notes_time=time.strftime("%H:%M", time.localtime()))
    timelocal = time.strftime("%Y-%m-%d %H.%M", time.localtime())
    user = User.objects.get(username=request.user)

    if request.method == 'GET':
        notes_time = request.GET["notes_time"]
        notes_date = request.GET["notes_date"]
        note = Note.objects.filter(note_user_id=request.user, notes_time=notes_time, notes_date=notes_date)
        if (note):
            send_mail("SketchPad - Напоминание", "Вам пришло это письмо потому,что вы запланировали на " + notes_date + "в " + notes_time + "дело." , settings.EMAIL_HOST_USER, [user.email])
            return HttpResponse("yes",content_type="text/html")
        else:
            return HttpResponse("no", content_type="text/html")
    else:
        return HttpResponse("no", content_type="text/html")

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
    note.notes_time = request.POST['notes_time']
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