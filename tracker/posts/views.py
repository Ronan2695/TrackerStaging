from django.shortcuts import render, redirect, get_object_or_404, reverse, render_to_response
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import forms
from .models import Post
from .forms import CreateArticle
from django.http import HttpResponse
from django.contrib.auth.forms import UserChangeForm

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

def tracker_view(request, track_id):
    #post = Post.objects.get(pk=post_id)
    track = get_object_or_404(Post, pk=track_id)
    return render(request, 'posts/tracker_view.html', {'track':track})

'''
def tracker_edit(request, id):
    session = Post.objects.get(pk=id)
    if request.method == 'POST':
        tracker = forms.CreateArticle(request.POST or None, instance=session)
        if tracker.is_valid():
            #save article to db
            tracker.save(commit=False)
            return redirect('posts:tracker_list')
    else:
        tracker = forms.CreateArticle()
    return render(request, 'posts/tracker_edit.html',{'tracker':tracker})
'''




















'''
def modify(request, track_id):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('posts:tracker_list')
    else:
        form = UserChangeForm(instance=request.user)
        args = {'form':form}
        return render(request, 'posts/modify.html', args)
'''

#def tracker_edit(request, task_id=None):
#    if task_id is not None:
#        track  = Post.objects.get(pk=task_id)
#    else:
#        track = Post()
#
#    if request.method == 'POST': # If the form has been submitted...
#        tracker = forms.CreateArticle(request.POST, instance=track)
#        if tracker.is_valid():
#            tracker.save()
#    else:
#        tracker  = forms.CreateArticle(instance=track)
#
#    return render(request,'posts/tracker_edit.html',{'tracker': tracker, 'task_id':task_id})



#def tracker_edit(request, id=None, template_name='posts/tracker_edit.html'):
#    if id:
#        track = get_object_or_404(Post, pk=id)
#    else:
#        track = Post()
#    tracker = CreateArticle(request.POST or None, instance=track)
#    if request.POST and tracker.is_valid():
#        tracker.save()
#
        # Save was successful, so redirect to another page
#        redirect_url = reverse('posts:tracker_list')
#        return redirect(redirect_url)
#    else:
#        tracker = CreateArticle(instance=track)
#
#    return render(request, template_name, {
#        'tracker': tracker, 'id':id
#    })


#def modify(request):
#    if request.method == 'POST':
#        form = UserChangeForm(request.POST, instance=request.user)
#
#        if form.is_valid():
#            form.save()
#            return redirect('posts:tracker_list')
#    else:
#        form = UserChangeForm(instance=request.user)
#        args = {'form':form}
#        return render(request, 'posts/modify.html', args)
