from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
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

def flight_details(request):
    if(request.method == 'POST'):
        flight = request.POST.get('flight').upper()
        flight_num = request.POST.get('flight_num').upper()
        seat = request.POST.get('seat').upper()
        
        airport = request.POST.get('airport')
        arrival_date = request.POST.get('arrival_date')
        est_arrival = request.POST.get('est_arrival')

        dest = request.POST.get('dest')
        num_of_bags = request.POST.get('num_of_bags')
        new_trip = Flight(  user=request.user,
                            flight = flight,
                            flight_num = flight_num,
                            seat = seat,
                            airport = airport,
                            arrival_date = arrival_date,
                            est_arrival = est_arrival,
                            dest = dest,
                            num_of_bags = num_of_bags)

        new_trip.save()

        if request.POST.get("bus"):
            new_trip.is_cab = False
            new_trip.save()
            return redirect('bus')
        elif request.POST.get("cab"):
            new_trip.is_cab = True
            new_trip.save()  
            return redirect('cab')

        return redirect('search_trips')

    return render(request, 'student/flight_details.html', {})



def bus(request):
    if(request.method == 'POST'):    
        nypa_travel = request.POST.get('nypa_travel')
        bus_company = request.POST.get('bus_company').upper()
        bus_timing = request.POST.get('bus_timing')
        meeting_point = request.POST.get('meeting_point')
        start_time = request.POST.get('start_time')
        travel_plan = request.POST.get('travel_plan')

        new_trip = Bus( user=request.user,
                        bus_company = bus_company,
                        bus_timing = bus_timing,
                        meeting_point = meeting_point,
                        start_time = start_time,
                        travel_plan = travel_plan,
                        nypa_travel = nypa_travel)
        
        new_trip.save()
        return redirect('search_trips')

    return render(request, 'student/bus.html', {})


def cab(request):
    if(request.method == 'POST'):
        cab = request.POST.get('cab')
        cab_num = request.POST.get('cab_num')
        seats = request.POST.get('seats')
        
        meeting_area = request.POST.get('meeting_area')
        meeting_time = request.POST.get('meeting_time')

        pickup = request.POST.get('pickup')
        drop = request.POST.get('drop')

        travel_plan = request.POST.get('travel_plan')

        new_trip = Cab( user=request.user,
                        cab = cab,
                        cab_num = cab_num,
                        seats = seats,
                        meeting_area = meeting_area,
                        meeting_time = meeting_time,
                        pickup = pickup,
                        drop = drop,
                        travel_plan = travel_plan)

        new_trip.save()
        return redirect('search_trips')

    return render(request, 'student/cab.html', {})



def search_trips(request):
    # if request.method == 'POST':
    #     task = request.POST.get('task')
    #     new_todo = todo(user=request.user, todo_name=task)
    #     new_todo.save()
    
    flights = Flight.objects.all()
    bus = Bus.objects.all()
    cab = Cab.objects.all()
    context = {
        'flights' : flights,
        'bus' : bus,
        'cab' : cab
    }

    return render(request, 'student/search_trips.html', context)


def LogoutView(request):
    logout(request)
    return redirect('login')