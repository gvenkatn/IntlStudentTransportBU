from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('login_success/', views.login_success, name='login_success'),
    path('flight_details/', views.flight_details, name='flight_details'),
    path('bus/', views.bus, name='bus'),
    path('cab/', views.cab, name='cab'),
    path('search_trips/', views.search_trips, name='search_trips'),
    path('trip_details/', views.trip_details, name='trip_details'),
    path('logout/', views.LogoutView, name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.
MEDIA_ROOT)