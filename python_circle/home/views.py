from django.shortcuts import redirect, render
from .models import UserSkills
from django.contrib import messages

# Create your views here.
def home_page(request):
    user = UserSkills(request.POST)
    if request.method =="POST":
        username=request.POST.get('username')
        print(username)
        if UserSkills.objects.filter(username=username).exists():
            return redirect('/home/already_exists')   
        name=request.POST.get('name')
        skill = request.POST.getlist(('skill[]'))
        skill=','.join(skill)
        Insertion=UserSkills(name=name,skill=skill,username=username)
        Insertion.save()
        return redirect('/home/success_message')
    else:
        return render(request,"home/home.html")

def success_message(request):
    return render(request,"home/message.html")

def already_exists(request):
    return render(request,"home/username_exists.html")

