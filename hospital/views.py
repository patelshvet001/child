from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

@login_required
@require_POST
def update_appointment_status(request):
    try:
        appointment_id = request.POST.get('appointment_id')
        new_status = request.POST.get('status')
        
        # Get the appointment
        appointment = Appointment.objects.get(id=appointment_id)
        
        # Update the status
        appointment.status = new_status
        appointment.save()
        
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}) 