from django.urls import path
from .views import base 
from . import views

urlpatterns = [
    path('', base, name="base"),
    path('doctor_details/<int:pk>/', views.doctor_details, name="doctor_details" ),
    path('book_appointment/<int:pk>/', views.book_appointment, name='book_appointment'),
]
