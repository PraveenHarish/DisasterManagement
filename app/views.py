from django.shortcuts import render, redirect
from .models import Report

def home(request):
    return render(request, "home.html")

def disasters(request):
    return render(request, "disasters.html")

def preparedness(request):
    return render(request, "preparedness.html")

def shelters(request):
    return render(request, "shelters.html")

def contacts(request):
    return render(request, "contacts.html")

def report(request):

    if request.method == "POST":
        Report.objects.create(
            name=request.POST["name"],
            disaster=request.POST["disaster"],
            location=request.POST["location"],
            description=request.POST["description"]
        )

        return redirect("/report/")

    reports = Report.objects.all().order_by("-id")

    return render(request, "report.html", {"reports": reports})