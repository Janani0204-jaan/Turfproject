"""
URL configuration for turfproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from turfapp import views
# from .views import quick_message_view


# from turfproject.turfapp.views import bookingviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', views.home, name='home'),
    path('allturfs/',views.allturfs),
    path('contacts/',views.contacts),
    path('events/',views.events),
    path('book/', views.bookingview, name='book_turf'),
path('booking/', views.bookingview, name='book_turf'),

    path('payment/', views.payment, name='payment'),
path('bookingconfirmation/', views.bookingconfirmation, name='bookingconfirmation'),
    path('draft/', views.draft, name='draft'),
    path('quick-message/', views.quick_message_view, name='quick_message'),
    path('print-teams/', views.team_list_view, name='print_teams'),

]




