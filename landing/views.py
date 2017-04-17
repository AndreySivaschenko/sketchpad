from django.shortcuts import render, redirect
from landing.models import comment

# Create your views here.

def main(request):
    recall = comment.objects.order_by("-id")[0:3]
    return render(request, "main.html",{"recall":recall})


def add_comments(request):
    print(request.POST)
    comments = comment(comment_name=request.POST['comments_name'], comment_email=request.POST['comments_email'],
                       comment_recall=request.POST['comments_recall'])
    comments.save()
    return redirect("/")
