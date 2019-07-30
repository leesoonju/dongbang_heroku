from django.shortcuts import render, redirect
from .models import Dong
from .models import Bang


def home(request):
    dongs = Dong.objects
    bangs = Bang.objects
    return render(request, 'home.html', {'dongs' : dongs, 'bangs': bangs})


def submit(request):
    d = Dong()
    d.message = request.GET['a']
    d.writer = request.GET['b']
    d.date = request.GET['c']
    d.save()
    return redirect('/')


def reple(request):
    e = Bang()
    e.message = request.POST['f']
    e.writer = request.POST['g']
    e.date = request.POST['h']
    e.save()
    return redirect('/')
