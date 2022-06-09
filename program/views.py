from django.shortcuts import redirect, render
from profiles import models as profiles_models
from . import models

# Create your views here.
def all_programs(request):
    user = request.user
    context = {"title": "All Programs"}
    if user.id and user.username != "admin":
        volunteer = profiles_models.Profile.objects.get(user_id=user.id).is_volunteer
        context["volunteer"] = volunteer
    programs = models.Program.objects.all()
    context["programs"] = programs

    return render(request, "programs.html", context)


def program_details(request, program, lecture=None):
    user = request.user
    program = models.Program.objects.get(id=program)
    lectures = models.Lecture.objects.filter(program=program)
    if lectures.count() > 0 and lecture is None:
        lecture = lectures[0].id
    if lecture:
        lecture = models.Lecture.objects.get(id=lecture)
    context = {
        "title": program.name,
        "program": program,
        "lectures": lectures,
        "lecture": lecture,
    }
    if user.id and user.username != "admin":
        volunteer = profiles_models.Profile.objects.get(user_id=user.id).is_volunteer
        context["volunteer"] = volunteer
    return render(request, "after_enrolmeant.html", context)


def add_program(request):
    user = request.user
    context = {
        "title": "add program",
    }
    if user.id and user.username != "admin":
        volunteer = profiles_models.Profile.objects.get(user_id=user.id).is_volunteer
    if (not user) or (volunteer == False):
        return redirect("/")
    else:
        if request.method == "POST":
            image = request.FILES["image"]
            models.Program.objects.create(
                creator=user, name=request.POST.get("name"), picture=image
            )
            return redirect("/profiles/control-panel")
        context["volunteer"] = volunteer
        return render(request, "add_program.html", context)


def delete_program(request, id):
    user = request.user
    if user.id and user.username != "admin":
        volunteer = profiles_models.Profile.objects.get(user_id=user.id).is_volunteer
    if (not user) or (volunteer == False):
        return redirect("/")
    else:
        program = models.Program.objects.get(id=id)
        if program.creator == user:
            program.delete()
        return redirect("/profiles/control-panel")


def add_lecture(request):
    program_id = request.GET.get("program_id")
    user = request.user
    context = {
        "title": "add lecture",
    }
    if user.id and user.username != "admin":
        volunteer = profiles_models.Profile.objects.get(user_id=user.id).is_volunteer
        context["volunteer"] = volunteer
    if request.method == "POST":
        models.Lecture.objects.create(
            program_id=program_id,
            name=request.POST.get("name"),
            text=request.POST.get("text"),
            video=request.POST.get("video_url"),
        )
        return redirect(f"/programs/{program_id}")

    return render(request, "add_lecture.html", context)


def delete_lecture(request, id):
    user = request.user
    if user.id and user.username != "admin":
        volunteer = profiles_models.Profile.objects.get(user_id=user.id).is_volunteer
    if (not user) or (volunteer == False):
        return redirect("/")
    else:
        lecture = models.Lecture.objects.get(id=id)
        if lecture.program.creator == user:
            lecture.delete()
        return redirect(f"/programs/{lecture.program.id}")
