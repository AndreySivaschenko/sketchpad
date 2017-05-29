from django.shortcuts import render, redirect
from landing.models import comment
from django.shortcuts import render_to_response
from django.template.context import RequestContext
# Create your views here.

def main(request):
    recall = comment.objects.order_by("-id")[0:3]

    context = RequestContext(request,
                             {'request': request,
                              'recall': recall,
                              'user': request.user}
                             )
    return render_to_response('main.html',context=context)



def add_comments(request):
    print(request.POST)
    comments = comment(comment_name=request.POST['comments_name'], comment_email=request.POST['comments_email'],
                       comment_recall=request.POST['comments_recall'])
    comments.save()
    return redirect("/")
