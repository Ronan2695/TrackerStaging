from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import forms
from .models import Post
from .forms import CreateArticle
from django.http import HttpResponse

@login_required
def quicklinkview(request):
    return render(request, 'posts/quicklinks.html')

def scheduleview(request):
    return render(request, 'posts/engschedule.html')

def prupdatesview(request):
    return render(request, 'posts/processupdates.html')

def tracker_list(request):
    tracks = Post.objects.all()
    return render(request,'posts/tracker_list.html',{'tracks':tracks})

def tracker_edit(request):
    if request.method == 'POST':
        tracker = forms.CreateArticle(request.POST)
        if tracker.is_valid():
            #save article to db
            tracker.save()
            return redirect('posts:tracker_list')
    else:
        tracker = forms.CreateArticle()
    return render(request, 'posts/tracker_edit.html',{'tracker':tracker})

def tracker_view(request, post_id):
    #post = Post.objects.get(pk=post_id)
    track = get_object_or_404(Post, pk=track_id)
    return render(request, 'posts/tracker_view.html', {'track':track})
