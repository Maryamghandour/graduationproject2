from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from program import models as program_models
from . import models

# Create your views here.
def login(request):
    context = {"title": "Login"}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect("/")
        except:
            messages.info(request, "Wrong password")
            return render(request, "login.html")
    return render(request, "login.html", context)


def signup(request):
    context = {
        "title": "register",
    }
    if request.method == "POST":
        try:
            user = User.objects.create_user(
                email=request.POST.get("email"),
                username=request.POST.get("username"),
                password=request.POST.get("password"),
            )
            models.Profile.objects.create(
                user=user,
                name=request.POST.get("name"),
                is_volunteer=False,
                is_patient=True,
                phone_number=request.POST.get("phone_number"),
            )
            auth_login(request, user)
            return redirect("/")

        except:
            messages.info(request, "username is taken already")
            return render(request, "register.html", context=context)
    else:
        return render(request, "register.html", context=context)


def logout_request(request):
    logout(request)
    return redirect("/")


def become_a_volunteer(request):
    user = request.user.id
    profile = models.Profile.objects.get(user_id=user)
    profile.is_volunteer = True
    profile.save()
    return redirect("/")


def control_panel(request):
    user = request.user
    if user.id and user.username != "admin":
        volunteer = models.Profile.objects.get(user_id=user.id).is_volunteer
        if volunteer == True:
            programs = program_models.Program.objects.filter(creator=user)
            context = {
                "volunteer": volunteer,
                "title": "Control Panel",
                "programs": programs,
            }
            return render(request, "control_panel.html", context)
    return redirect("/")
