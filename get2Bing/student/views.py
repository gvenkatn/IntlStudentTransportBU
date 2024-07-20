from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student
from django.contrib import messages



# Create your views here.
def register(request):
    if(request.method == 'POST'):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        bNumber = request.POST.get('bNumber')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')

        if(len(password) < 8):
            messages.error(request, 'Password must be at least 3 characters')
            return redirect('register')

        get_email = User.objects.filter(email=email)
        if get_email:
            messages.error(request, 'Email already exists, Login')
            return redirect('register')
        
        get_bNumber = User.objects.filter(email=email)
        if get_bNumber:
            messages.error(request, 'B-Number already exists, Login')
            return redirect('register')

        new_user = User.objects.create_user(username = bNumber,
                                            email = email,
                                            password = password,
                                            first_name = first_name,
                                            last_name = last_name)

        new_student = Student(user = new_user,
                             gender = gender,
                             phone = phone)
                    
        new_user.save()
        new_student.save()
        

    return render(request, 'student/register.html',{})


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('login_success')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('trips')
        else:
            messages.error(request, 'Error, wrong user details or user does not exist')
            return redirect('login')


    return render(request, 'student/loginpage.html', {})


def login_success(request):

    return render(request, 'student/login_success.html', {})

def new_trip(request):

    return render(request, 'student/new_trip.html', {})


def trips(request):

    return render(request, 'student/trips.html', {})


def LogoutView(request):
    logout(request)
    return redirect('login')