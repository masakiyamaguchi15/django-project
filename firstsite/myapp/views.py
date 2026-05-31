from django.shortcuts import render

def index(request):
    context = { "contents": "Welcome, my app!!" }
    return render(request, "index.html", context)

def question(request):
    return render(request, "questionnaire.html")

def confirm(request):
    if request.method != "POST":
        return render(request, "questionnaire.html")
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    lang_list = request.POST.getlist("lang")
    message = request.POST.get("message")
    context = {
        "name": name,
        "gender": gender,
        "lang_list": lang_list,
        "message": message
    }
    return render(request, "confirmation.html", context)