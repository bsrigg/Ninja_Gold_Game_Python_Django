from django.shortcuts import render, redirect
from datetime import datetime
import random
def index(request):
    if "gold" not in request.session:
        request.session['activities']=["1"]
        request.session['gold']=0
        request.session['score']=0
        request.session['bankrupt']='hide'
        request.session['stopme']=False
    return render(request,'goldactivity/index.html')
def farm(request):
    if request.session['stopme'] == False:
        if "gold" not in request.session:
            request.session['gold']=0
        if "score" not in request.session:
            request.session['score']=0
        if request.method == "POST":
            request.session['gold'] = random.randrange (10,20,1)
            request.session['score'] += request.session['gold']
        if request.session['score'] <0:
            request.session['bankrupt']='unhide'
            request.session['stopme']=True
        myactivities = request.session['activities']
        myactivities.append(f"You got {request.session['gold']} gold pieces from the Farm at ({datetime.now().strftime('%B %d,%Y %H:%M:%S %p')})")
        request.session['activities']=myactivities
    return render(request,'goldactivity/index.html')
def house(request):
    if request.session['stopme'] == False:
        if "gold" not in request.session:
            request.session['gold']=0
        if "score" not in request.session:
            request.session['score']=0
        if request.method == "POST":
            if request.session['bankrupt'] == 'hide':
                request.session['gold'] = random.randrange (2,5,1)
                request.session['score'] += request.session['gold']
        if request.session['score'] <0:
            request.session['bankrupt']='unhide'
            request.session['stopme']=True
        myactivities = request.session['activities']
        myactivities.append(f"You got {request.session['gold']} gold pieces from the House at ({datetime.now().strftime('%B %d,%Y %H:%M:%S %p')})")
        request.session['activities']=myactivities
    return render(request,'goldactivity/index.html')
def cave(request):
    if request.session['stopme'] == False:
        if "gold" not in request.session:
            request.session['gold']=0
        if "score" not in request.session:
            request.session['score']=0
        if request.method == "POST":
            request.session['gold'] = random.randrange (5,10,1)
            request.session['score'] += request.session['gold']
        if request.session['score'] <0:
            request.session['bankrupt']='unhide'
            request.session['stopme']=True
        myactivities = request.session['activities']
        myactivities.append(f"You got {request.session['gold']} gold pieces from the Cave at ({datetime.now().strftime('%B %d,%Y %H:%M:%S %p')})")
        request.session['activities']=myactivities
    return render(request,'goldactivity/index.html')
def casino(request):
    if request.session['stopme'] == False:
        if "gold" not in request.session:
            request.session['gold']=0
        if "score" not in request.session:
            request.session['score']=0
        if request.method == "POST":
            request.session['gold'] = random.randrange (-100,100,1)
            request.session['score'] += request.session['gold']
        if request.session['score'] <0:
            request.session['bankrupt']='unhide'
            request.session['stopme']=True
        myactivities = request.session['activities']
        myactivities.append(f"You got {request.session['gold']} gold pieces from the Casino at ({datetime.now().strftime('%B %d,%Y %H:%M:%S %p')})")
        request.session['activities']=myactivities
    return render(request,'goldactivity/index.html')
def bankrupt(request):
    request.session['bankrupt']='unhide'
    request.session['stopme']=True
    return render(request,'goldactivity/index.html')
def resetme(request):
    request.session.clear
    request.session['activities']=[]
    request.session['gold'] = 0
    request.session['score'] = 0
    request.session['bankrupt']='hide'
    request.session['stopme']=False
    return render(request,'goldactivity/index.html')
