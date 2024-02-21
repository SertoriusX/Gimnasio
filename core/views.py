from django.shortcuts import render, get_object_or_404

from .forms import CommentForm
from .models import Gym, Gym_d, Gym_r, Gym_S, Trainer, Classes,Classes_tabs


# Create your views here.
def frontpage(request):
    classes_tabs=Classes_tabs.objects.all()
    gyms=Gym.objects.all()
    gimnasios=Gym_d.objects.all()
    gym_r=Gym_r.objects.all()
    gym_S=Gym_S.objects.all()
    trainers=Trainer.objects.all()
    classes = Classes.objects.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.gyms = gyms
            comment.save()

    else:
        form = CommentForm()
    return render(request,'core/frontpage.html',{'gyms':gyms,'gimnasios':gimnasios,'gym_r':gym_r,'gym_S':gym_S,'trainers':trainers,'form':form,'classes':classes,'classesTabs':classes_tabs})

def gym_d(request,slug):
    gym_d=get_object_or_404(Gym_d,slug=slug)
    return render(request,'core/gym_d.html',{'gym_d':gym_d})

def gym_r(request,slug):
    gym_r=get_object_or_404(Gym_r,slug=slug)
    return render(request,'core/gym_r.html',{'gym_r':gym_r})