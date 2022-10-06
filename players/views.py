import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from requests import request
from .models import Player,match,Team,Officials
from accounts.models import Account
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .form import playerForm


def index(request):
    player  =Player.objects.all()
    team = Team.objects.all()
    official = Officials.objects.all()
    a = datetime.datetime.now().year
    print(a)
    context = {
        'officials':official,
        'players':player,
        'team':team,
    }
    return render(request,'index.html', context)

def player_detail(request,id):
    player = Player.objects.get(pk=id)
    context={
        'player':player
    }
    return render(request,'player_detail.html',context)
    

def players(request):
    player  =Player.objects.all()
    c = player.count()
    context = {
        'player':player,
        'c':c
    }
    return render(request,'players.html', context)
 
def matches(request):
    a = datetime.date.today()
    Matchs  = match.objects.all()
    for matchs in Matchs:
        if matchs.date < a :
            matchs.played = True
            matchs.save()
        else:
            matchs.played = False
            matchs.save()
           
    print(a)
    matches = match.objects.filter(date__gte = a).order_by('date')
    result = match.objects.filter(played = True).order_by('-date')[:5]
    context = {
        'match':matches,
        'results':result,
    }
    return render(request,'matches.html',context)
        
    
def signup(request):
    form = playerForm()

    if request.method == "POST":
        form = playerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('login') 
            #  username = form.cleaned_data.get['username']
            #  email = form.cleaned_data.get['email']
            #  kit_number = form.cleaned_data.get['kit_number']
            #  position = form.cleaned_data.get['position']
            #  image = form.cleaned_data.get['image']
            #  first_name = form.cleaned_data.get['first_name']
            #  last_name= form.cleaned_data.get['last_name']
            #  password = form.cleaned_data.get['password1']
            #  password2 = form.cleaned_data.get['password2']
        
        
        # if request.POST['password'] == password2:
        #     if Account.objects.filter(email=email).exists():
        #         messages.info(request,'Email already exist')
        #         return HttpResponseRedirect('signup')
        #     elif Account.objects.filter(username=username).exists():
        #         messages.info(request,'User name already exist')
        #         return HttpResponseRedirect('signup')
        #     elif Account.objects.filter(kit_number=kit_number).exists():
        #         messages.info(request,'sorry this jersey number is takken')
        #         return HttpResponseRedirect('signup')
        #     else:
                
        #         return HttpResponseRedirect('login')
                
        # else:
        #     messages.info(request,'Password does not match')
        #     return HttpResponseRedirect('signup')
       
    else:

        return render(request,'signup.html',{'form':form})
    return render(request,'signup.html',{'form':form})
    
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user= auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/')
        else:
            messages.info(request,'credencials not valid')
            return HttpResponseRedirect('login')
        pass
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
def profile(request,username):
    username =request.user.username
    player = Account.objects.get(username=username)
    return render(request,'profile.html',{'player':player})


def officialsDetails(request,id):
    official = Officials.objects.get(pk = id)
    context = {
        'official':official,
    }
    return render(request,'officials-details.html',context)
    

def Results(request):
    a = datetime.date.today()
    Matchs  = match.objects.all()
    for matchs in Matchs:
        if matchs.date < a :
            matchs.played = True
            matchs.save()
        else:
            matchs.played = False
            matchs.save()
            
    result = match.objects.filter(played = True)
    context = {
        
        'results':result,
    }
    return render(request,'results.html',context)
# Create your views here.
