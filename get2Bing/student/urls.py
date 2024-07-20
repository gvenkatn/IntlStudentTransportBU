from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('login_success/', views.login_success, name='login_success'),
    path('new_trip/', views.new_trip, name='new_trip'),
    path('trips/', views.trips, name='trips'),
    path('logout/', views.LogoutView, name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.
MEDIA_ROOT)