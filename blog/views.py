from django.contrib.messages.api import MessageFailure
from django.http.response import HttpResponse, JsonResponse, ResponseHeaders
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login

from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Image
from .forms import CommentForm, UserForm, ImageForm

import json

# Create your views here.



def image_list(request):
    images = Image.objects.filter(approved=True).order_by('-published_date')
    form = CommentForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post_image = Image.objects.get(id=form.data['image'])
                comment.author = request.user
                print(request.body)
                comment.save()
                return redirect('image_list')
        else:
            return redirect('login')
    return render(request, 'blog/image_list.html', {'images': images, 'form': form})



@staff_member_required()
def info_image_list_approved(request):
    images = Image.objects.filter(approved=False)
    images_count = images.count()

    data= {
        'count': images_count,
    }

    return JsonResponse(data)

def image_detail(request, id):
    image = get_object_or_404(Image, id=id)
    form = CommentForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                print(form.data)
                comment.post_image = Image.objects.get(id=form.data['image'])
                comment.author = request.user

                comment.save()
                return redirect('image_detail', id=image.id)
        else:
            return redirect('login')

    return render(request, 'blog/image_detail.html', {'image': image, 'form': form})


@login_required
def liked(request):
    if request.method == 'POST':
        post_data = json.loads(request.body.decode("utf-8"))
        image = get_object_or_404(Image, id=post_data.get('image_id'))
        if image.likes.filter(id=request.user.id):
            image.likes.remove(request.user)
            action = False
        else:
            image.likes.add(request.user)
            action = True

    data= {
        'count_like': image.likes.count(),
        'action': action,
    }

    return JsonResponse(data)

def userliked(request):
    if request.method == 'GET':
        post_data = json.loads(request.body.decode("utf-8"))

    data = {
        'test': 1
    }
    print(data)
    return JsonResponse(data)


@login_required
def image_post(request):
    form = ImageForm()

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = request.user
            image.filename = image.image_file.name
            image.save()

            return redirect('image_list')
    return render(request, 'blog/image_post.html', {'form': form})


@staff_member_required()
def image_list_admin(request):
    images = Image.objects.filter(approved=False).order_by('-published_date')
    return render(request, 'blog/image_list.html', {'images': images})

@staff_member_required()
def approve_image(request, id):
    image = get_object_or_404(Image, id=id)
    image.approve()

    return redirect('image_list_admin')

@staff_member_required()
def remove_image(request, id):
    image = get_object_or_404(Image, id=id)
    image.delete()

    return redirect('image_list_admin')

def register_request(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('image_list')
    
    return render(request, 'registration/register.html', {'form':form})