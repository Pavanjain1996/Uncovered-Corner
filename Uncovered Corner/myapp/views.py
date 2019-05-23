from django.shortcuts import render, redirect
from myapp.models import Country, Feedback, Season, Wonder
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage

user = None

def index(request):
    country = Country.objects.all().filter(Q(name='USA') | Q(name='India') | Q(name='Japan')) 
    season = Season.objects.all()
    wonder = Wonder.objects.all()
    return render(request,'Index.html',{'country':country,'season':season,'wonder':wonder})

def country(request):
    country = Country.objects.all()
    return render(request,'Country.html',{'country':country})

def explore(request,pk):
    country = Country.objects.get(pk=pk)
    return render(request,'Explore.html',{'country':country})

def search(request):
    searchtext = request.POST['searchtext']
    country = Country.objects.all().filter(name__contains=searchtext)
    if len(country)>0:
        return render(request,'Country.html',{'country':country})
    else:
        return render(request,'Error.html',{'searchtext':searchtext})

def feedback(request):
    name = request.POST['name']
    email = request.POST['email']
    content = request.POST['content']
    data = Feedback(name=name,email=email,feedback=content)
    data.save()
    return redirect('/Thanks')

def about(request):
    return render(request,'About.html')

def thanks(request):
    return render(request,'Thanks.html')

def administrator(request):
    return render(request,'AdminLogin.html')

def adminlogin(request):
    global user
    if user is None:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        data = Feedback.objects.all().filter(status='Not Resolved')
        return render(request,'AdminHome.html',{'data':data})
    else:
        return redirect('/Administrator')

def adminlogout(request):
    logout(request)
    global user
    user = None
    return redirect('/Administrator')

def sendreply(request,pk):
    data = Feedback.objects.get(pk=pk)
    email = data.email
    reply = request.POST['reply']
    data.reply = reply
    data.status = 'Resolved'
    data.save()
    try:
        mail = EmailMessage('Reply from Uncovered Notes',reply,to = [email])
        mail.send()
    except:
        pass
    return redirect('/AdminLogin')

def solved(request):
    if user is None:
        return redirect('/Administrator')
    else:
        data = Feedback.objects.all().filter(status='Resolved')
        return render(request,'SolvedComplaints.html',{'data':data})
