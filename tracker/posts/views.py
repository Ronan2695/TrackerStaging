from django.shortcuts import render, redirect
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
    return render(request, 'posts/tracker_list.html')

def tracker_edit(request):
    if request.method == 'POST':
        tracker = forms.CreateArticle(request.POST)
        if tracker.is_valid():
            #save article to db
            tracker.save()
            return redirect('posts:home')
    else:
        tracker = forms.CreateArticle()
    return render(request, 'posts/tracker_edit.html',{'tracker':tracker})
