from django.urls import path
from . import views

urlpatterns = [
    # ... your existing URLs ...
    path('update-appointment-status/', views.update_appointment_status, name='update_appointment_status'),
] 