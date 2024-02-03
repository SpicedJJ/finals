
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def home_page(request):
    return render(request,'pages/home.html')

def about_page(request):
    return render(request,'pages/about.html')

def login_page(request):
    return render(request,'pages/login.html')


def contact_page(request):
    return render(request,'pages/contact.html')

def service_page(request):
    return render(request,'pages/service.html')

def register_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect('/home')

    else:
        form = UserCreationForm()

    return render(request, 'pages/register.html',{'form':form,})


def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            messages.success(request,("There was an error logging in, try again"))
            return redirect('login')
    else:
        return render(request, 'pages/login.html')
        return render(request, 'pages/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,("Successfully logged Out!"))
    return redirect('homePage')

    
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import Appointment

@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'pages/appointment_list.html', {'appointments': appointments})


def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aboutPage')
    else:
        form = AppointmentForm()

    return render(request, 'pages/create_appointment.html', {'form': form})

@login_required
def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'pages/edit_appointment.html', {'form': form, 'appointment': appointment})

@login_required
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.delete()
    return redirect('appointment_list')
