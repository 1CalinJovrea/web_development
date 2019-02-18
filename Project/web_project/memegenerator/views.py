from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as l, logout

from memegenerator.forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'index.html', {'username': username})
    else:
        username = None
                
    return render(request, 'index.html')

def sign_up(request):

    if request.session.has_key('username'):
        username = request.session['username']
    else:
        username = None

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()

           
        login_form = LoginForm()

        return render(request, 'login.html', {'login_form': login_form, 'username': username})
    else:
        register_form = RegisterForm()

    if username:
        return render(request, 'sign_up.html', {'username': username, 'register_form': register_form})
    else:
        return render(request, 'sign_up.html', {'register_form': register_form})

        


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        username = login_form.data['username']
        password = login_form.data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                l(request,user)
                request.session['username'] = username
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:        
        if request.session.has_key('username'):
            username = request.session['username']

            return render(request, 'login.html', {'username':username})
        else:
            login_form = LoginForm()
            
            return render(request, 'login.html', {'login_form':login_form, 'username': None})


def logout(request):
    try:
        del request.session['username']
        return render(request, 'index.html')
    except:
        login_form = LoginForm()
        pass
   
    if login_form:
        return render(request, 'login.html', {'login_form':login_form})
    else:
        return render(request, 'index.html')

def profile(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'profile.html', {'username': username})
    else:
        username = None

    return render(request, 'index.html')


