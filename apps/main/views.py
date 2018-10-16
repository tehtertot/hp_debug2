from django.shortcuts import render

def index(request):
    """show main page with routes to Ollivander's and Students apps"""
    return render(request, "main/index.html")