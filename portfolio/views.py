from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.
def home(request):
   return render(request, "portfolio/home.html")

def contact(request):
    return render(request, "portfolio/contact.html")

def portfolio(request):
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects': projects})
  

