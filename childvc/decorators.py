from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from childvc.models import Profile

def patient_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            if profile.role == '1':  # 1 for patient
                return function(request, *args, **kwargs)
            else:
                messages.error(request, 'Access Denied. Patient access required.')
                return redirect('/')
        else:
            messages.error(request, 'Please login first.')
            return redirect('/login/')
    return wrap

def hospital_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            if profile.role == '2':  # 2 for hospital
                return function(request, *args, **kwargs)
            else:
                messages.error(request, 'Access Denied. Hospital access required.')
                return redirect('/')
        else:
            messages.error(request, 'Please login first.')
            return redirect('/login/')
    return wrap 