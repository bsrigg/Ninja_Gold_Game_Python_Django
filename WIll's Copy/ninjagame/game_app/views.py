from django.shortcuts import render, redirect
from random import randint
from datetime import datetime


def index(request):
    if 'golds' not in request.session:
        request.session["golds"] = 0
    if 'activities' not in request.session:
        request.session["activities"] = []
    return render(request, "index.html")

def rpg(request):
    golds = 0
    if request.POST["location"] == "farm":
        golds = randint(10, 20)
    elif request.POST["location"] == "cave":
        golds = randint(5, 10)
    elif request.POST["location"] == "house":
        golds = randint(2, 5)
    elif request.POST["location"] == "casino":
        golds = randint(-50, 50)
    request.session["golds"] += golds
    ts = datetime.now().strftime("(%Y/%m/%d %I:%M %p)")
    if golds > 0:
        request.session["activities"].append(f"<p class='green'>Went to the {request.POST['location']} and earned {golds} gold {ts}</p>")
    else:
        request.session["activities"].append(f"<p class='red'>Went to the {request.POST['location']} and lost {-golds} gold {ts}</p>")
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")