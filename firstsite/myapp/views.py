from django.shortcuts import render

def index(request):
    context = {"contents": "Welcome, my app!!"}
    return render(request, "index.html", context)