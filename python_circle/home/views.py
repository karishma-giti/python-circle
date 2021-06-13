from django.shortcuts import redirect, render
from .models import UserSkills
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

#<------------------data insertion------------------------------>
def insertion(request):
    user = UserSkills(request.POST)
    if request.method =="POST":
        username=request.POST.get('username')
        if UserSkills.objects.filter(username=username).exists():
            messages.error(request,'username already exists!')
            return redirect("/home/")           
        name=request.POST.get('name')
        if name=="":
            return redirect("/home/")
        skill = request.POST.getlist(('skill[]'))
        skill=','.join(skill)
        if skill=="":
            return redirect("/home/")
        Insertion=UserSkills(name=name,skill=skill,username=username)
        Insertion.save()
        return redirect('/home/user_list')
    else:
        return render(request,"home/home.html")


#<-------------if user already exists on database----------------->
def validate_username(request):
    if request.is_ajax and request.method == "GET":
        username = request.GET.get('username', None)
        data = {
             'is_taken': UserSkills.objects.filter(username=username).exists()
             }
        return JsonResponse(data)        

#<-------------if data successfully inserted on data base-------->
def success_message(request):
    return render(request,"home/success.html")


def user_list(request):
    user_list = UserSkills.objects.all()
    print(user_list)
    return render(request,"home/success.html",{'context':user_list})



