from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required
def quicklinkview(request):
    return render(request, 'posts/quicklinks.html')

def scheduleview(request):
    return render(request, 'posts/engschedule.html')

def prupdatesview(request):
    return render(request, 'posts/processupdates.html')

def nonpdview(request):
    return render(request, 'posts/nonpd.html')
