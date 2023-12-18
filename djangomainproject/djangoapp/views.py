from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

def registerPage(request):
    form = CreateUserForm()


    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form':form} 
    return render(request, 'djangoapp/register.html',context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password incorrect.')

    context = {}
    return render (request, 'djangoapp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    user = Usersinfo.objects.all()
    breeds = Breed.objects.all()

    total_alive = breeds.filter(status='Alive').count()
    total_breeds = breeds.count
    total_users = user.count
     

    context = {'user':user, 'breeds':breeds, 'total_alive':total_alive, 'total_breeds':total_breeds, 'total_users':total_users }

    return render(request, 'djangoapp/dashboard.html', context)

def userPage(request):
    context = {}
    return render(request, 'djangoapp/user.html', context)

def breeds(request):
    breeds = Breed.objects.all()

    return render(request, 'djangoapp/breeds.html', {'breeds':breeds})



def createDog(request):


    form = DogForm()
    if request.method == 'POST':
        # print('Printing Post:', request.POST)
        form = DogForm(request.POST)
        # if form info is valid, it will save. redirect will send back to main page once form submits
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}

    return render(request, 'djangoapp/adddog_form.html', context)



@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='user-page')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'djangoapp/user.html', {'user_form': user_form})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'djangoapp/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')