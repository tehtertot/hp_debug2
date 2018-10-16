from django.shortcuts import render, redirect
from .models import Wand

def index(request):
    """show a page with all the wands"""
    context = {
        "all_wands": Wand.objects.all()
    }
    return render(request, "ollivanders/index.html", context)

def show_add(request):
    """ show a page with the form to add a wand"""
    return render(request, "ollivanders/add.html")

def add_to_db(request):
    """ process the submission of a new wand"""
    if request.method == "POST":
        Wand.objects.create(core=request.POST["core"], length=float(request.POST["length"]), wood=request.POST["wood"])
    return redirect("/wands")