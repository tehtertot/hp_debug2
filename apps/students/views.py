from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Wand

def index(request):
    """
    show form to add new students
    """
    context = {
        "all_student": Student.objects.all(),
    }
    return render(request, "wizard/index.html", context)

def register(request):
    """
    create a new student IF BOTH FIELDS have been validated
    or show errors
    """
    if request.method == "POST":
        errors = Student.objects.my_validator(request.POST)
        if len(errors) > 0:
            Student.objects.create(first_name=request.POST["first_name"], last_name=request.POST["lastname"])
        else:
            for error in errors:
                messages.error(request, error)
                return redirect("/students")
    return redirect("/students")

def add_wand(request):
    """
    add the selected wand to the student
    """
    if request.method == "POST":
        student = Student.objects.get(id=request.POST["student"])
        student.wand = request.POST["wand"]
        student.save()
    return redirect("/")

def show_wizard(request):
    """
    show the selected wizard
    """
    return render(request, "wizards/show.html")