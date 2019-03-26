from django.shortcuts import render, redirect, get_object_or_404, reverse, render_to_response
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import forms
from .models import Update
from .forms import UpdateArticle
from django.http import HttpResponse
from django.contrib.auth.forms import UserChangeForm


def process_updates(request):
    if request.method == 'POST':
        updates = forms.UpdateArticle(request.POST)
        if updates.is_valid():
            #save article to db
            updates.save()
            return redirect('updates:updates_list')
    else:
        updates = forms.UpdateArticle()
    return render(request, 'updates/process_updates.html',{'updates':updates})

def updates_list(request):
    updates = Update.objects.all()
    return render(request,'updates/updates_list.html',{'updates':updates})
