from django.shortcuts import render,redirect
from django.contrib import messages
from childvc.models import Contact,Profile,Appointment 
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.template import RequestContext
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from childvc.decorators import hospital_required
import xlsxwriter
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph
import io
from datetime import datetime


@hospital_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/hospital/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'hospital/change_password.html', {
        'form': form
    })

def handler404(request, *args, **argv):
    response = render('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'hospital/password_reset.html'
    email_template_name = 'hospital/password_reset_email.html'
    subject_template_name = 'hospital/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('index')


def index(request):
	return render(request,'hospital/index.html')

@hospital_required
@login_required(login_url='/hospital/login/')
def myappointment(request):
    appointments = Appointment.objects.filter(hospital=request.user)
    return render(request,'hospital/my_appointments.html',{'appointments':appointments})

def about(request):
	return render(request,'hospital/about.html')

@hospital_required
def userprofile(request,id):
	user = User.objects.get(id=id)
	user_obj = Profile.objects.get(user=user)
	return render(request,'hospital/userprofile.html',{'user':user,'user_obj':user_obj})

@hospital_required
def editprofile(request,id):
	for_edit=User.objects.get(id=id)
	for_profile=Profile.objects.get(user=for_edit)
	return render(request,'hospital/EditProfile.html',{'for_profile':for_profile})

def handle_edit(request,id):
	user=User.objects.get(id=id)
	pro=Profile.objects.get(user=request.user)
	
	if request.method == 'POST':
		try:
			img=request.FILES['p_image']
			firstname=request.POST.get('edit_firstname','')
			lastname=request.POST.get('edit_lastname','')
			username=request.POST.get('edit_username','')
			phone_no=request.POST.get('edit_phoneno','')
			email=request.POST.get('edit_email','')
			address=request.POST.get('edit_address','')

			pro.profile_image=img
			user.first_name=firstname
			user.last_name=lastname
			user.username=username
			pro.phone=phone_no
			user.email=email
			pro.address=address

			user.save()
			pro.save()
			
			messages.success(request, 'Profile updated successfully!')
			return redirect('userprofile', id=id)  # Redirect to user profile with success message
		except Exception as e:
			messages.error(request, f'Error updating profile: {str(e)}')
			return redirect('editprofile', id=id)
	else:
		messages.error(request,'Something went wrong.')
		return redirect('userprofile', id=id)

def contact_us(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		msg = request.POST['msg']

		s = Contact(name=name,email=email,phone=phone,msg=msg)
		s.save()
		print("DATA ADDED..")
		messages.success(request,"DATA ADDED..")
		return redirect('/hospital/')


	return render(request,'hospital/contact.html')

def register(request):
	if request.method == 'POST':
		hospitalname = request.POST['fname']
		uname = request.POST['uname']
		email = request.POST['email']
		password = request.POST['pass1']
		confirmPassword = request.POST['pass2']

		if password == confirmPassword:
			if User.objects.filter(username=uname).exists():
				messages.error(request,"Hospital name alrady exits...")
				return redirect('/hospital/register/')
			elif User.objects.filter(email=email).exists():
				messages.error(request,"email alrady exits..")
				return redirect ('/hospital/register/')
			else:
				u = User.objects.create_user(first_name=hospitalname,username=uname,email=email,password=password)
				u.save()
				last_u = User.objects.last()
				p = Profile.objects.get(user=last_u)
				p.role = '2'
				p.save()
				messages.success(request,'user created ...')
				return redirect('/hospital/login/')


		else:
			print("password does not match..")
		
	return render(request,'hospital/register.html')

def login(request):
	if request .method == 'POST':
		username = request.POST['username']
		password= request.POST['pass']
		
		User = auth.authenticate(username=username,password=password)

		if User is not None:
			auth.login(request,User)
			messages.success(request,'logged in..')
			return redirect('/hospital/')
		else:
			print("invalid credentials...")
			return redirect('/hospital/login/')
	return render (request,'hospital/login.html')

def logout(request):
	auth.logout(request)
	messages.error(request,"your account is logged out..")
	return redirect('/hospital/')

@login_required(login_url='/hospital/login/')
@csrf_exempt
def update_appointment_status(request, appointment_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            status = data.get('status')
            
            # Get the appointment
            appointment = Appointment.objects.get(aid=appointment_id)
            
            # Update status
            appointment.status = status
            appointment.save()
            
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@hospital_required
@login_required(login_url='/hospital/login/')
def search_data(request):
    from datetime import datetime, timedelta
    from django.db.models import Q, Sum
    from django.utils import timezone

    # Get all appointments for this hospital
    appointments = Appointment.objects.filter(hospital=request.user)
    
    # Get all vaccines for the dropdown
    from childvc.models import Vaccine
    vaccines = Vaccine.objects.all()

    # Apply filters
    if request.GET:
        # Patient name search
        search_query = request.GET.get('search', '')
        if search_query:
            appointments = appointments.filter(
                Q(user__first_name__icontains=search_query) |
                Q(user__last_name__icontains=search_query)
            )

        # Vaccine type filter
        vaccine_type = request.GET.get('vaccine_type', '')
        if vaccine_type:
            appointments = appointments.filter(vac__vid=vaccine_type)

        # Status filter
        status = request.GET.get('status', '')
        if status:
            appointments = appointments.filter(status=status)

        # Date range filters
        date_range = request.GET.get('date_range', '')
        custom_date_range = request.GET.get('custom_date_range', '')

        if custom_date_range:
            try:
                start_date, end_date = custom_date_range.split(' - ')
                start_date = datetime.strptime(start_date, '%m/%d/%Y')
                end_date = datetime.strptime(end_date, '%m/%d/%Y')
                end_date = end_date.replace(hour=23, minute=59, second=59)
                appointments = appointments.filter(datetime__range=[start_date, end_date])
            except:
                pass
        elif date_range:
            today = timezone.now()
            if date_range == 'today':
                appointments = appointments.filter(datetime__date=today.date())
            elif date_range == 'week':
                week_start = today - timedelta(days=today.weekday())
                appointments = appointments.filter(datetime__gte=week_start)
            elif date_range == 'month':
                appointments = appointments.filter(datetime__year=today.year, datetime__month=today.month)
            elif date_range == 'year':
                appointments = appointments.filter(datetime__year=today.year)

        # Age range filter
        min_age = request.GET.get('min_age', '')
        max_age = request.GET.get('max_age', '')
        if min_age or max_age:
            today = timezone.now().date()
            if min_age:
                max_birth_date = today - timedelta(days=int(min_age)*365)
                appointments = appointments.filter(user__profile__bdate__lte=max_birth_date)
            if max_age:
                min_birth_date = today - timedelta(days=int(max_age)*365)
                appointments = appointments.filter(user__profile__bdate__gte=min_birth_date)

        # Price range filter
        min_price = request.GET.get('min_price', '')
        max_price = request.GET.get('max_price', '')
        if min_price:
            appointments = appointments.filter(vac__vprice__gte=min_price)
        if max_price:
            appointments = appointments.filter(vac__vprice__lte=max_price)

        # Sorting
        sort_by = request.GET.get('sort_by', 'date_desc')
        if sort_by == 'date_asc':
            appointments = appointments.order_by('datetime')
        elif sort_by == 'date_desc':
            appointments = appointments.order_by('-datetime')
        elif sort_by == 'price_asc':
            appointments = appointments.order_by('vac__vprice')
        elif sort_by == 'price_desc':
            appointments = appointments.order_by('-vac__vprice')
        elif sort_by == 'name_asc':
            appointments = appointments.order_by('user__first_name', 'user__last_name')

        # Handle export requests
        export_type = request.GET.get('export_type')
        if export_type in ['excel', 'pdf']:
            return export_data(appointments, export_type)

    # Calculate statistics
    total_appointments = appointments.count()
    completed_appointments = appointments.filter(status='Completed').count()
    pending_appointments = appointments.filter(status='Pending').count()
    total_revenue = appointments.filter(status='Completed').aggregate(total=Sum('vac__vprice'))['total'] or 0

    context = {
        'appointments': appointments,
        'vaccines': vaccines,
        'total_appointments': total_appointments,
        'completed_appointments': completed_appointments,
        'pending_appointments': pending_appointments,
        'total_revenue': total_revenue,
    }

    return render(request, 'hospital/search_data.html', context)

def export_data(appointments, export_type):
    if export_type == 'excel':
        return export_to_excel(appointments)
    elif export_type == 'pdf':
        return export_to_pdf(appointments)

def export_to_excel(appointments):
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet('Vaccination Data')

    # Define formats
    header_format = workbook.add_format({
        'bold': True,
        'bg_color': '#3498db',
        'font_color': 'white',
        'border': 1
    })
    cell_format = workbook.add_format({
        'border': 1,
        'text_wrap': True
    })

    # Write headers
    headers = ['Patient Name', 'Vaccine Type', 'Appointment Date', 'Duration', 'Status', 'Hospital', 'Price']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header, header_format)
        worksheet.set_column(col, col, 15)

    # Write data
    for row, appointment in enumerate(appointments, start=1):
        worksheet.write(row, 0, f"{appointment.user.first_name} {appointment.user.last_name}", cell_format)
        worksheet.write(row, 1, appointment.vac.vname, cell_format)
        worksheet.write(row, 2, appointment.datetime.strftime('%d %b %Y'), cell_format)
        worksheet.write(row, 3, appointment.vac.vdiscription, cell_format)
        worksheet.write(row, 4, appointment.status, cell_format)
        worksheet.write(row, 5, appointment.hospital.first_name, cell_format)
        worksheet.write(row, 6, f"₹{appointment.vac.vprice}", cell_format)

    workbook.close()
    output.seek(0)

    response = HttpResponse(
        output.read(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename="vaccination_data_{datetime.now().strftime("%Y%m%d")}.xlsx"'
    return response

def export_to_pdf(appointments):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Add title
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=30
    )
    elements.append(Paragraph('Vaccination Data Report', title_style))

    # Add date
    date_style = ParagraphStyle(
        'CustomDate',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=30
    )
    elements.append(Paragraph(f'Generated on: {datetime.now().strftime("%d %b %Y")}', date_style))

    # Prepare table data
    data = [['Patient Name', 'Vaccine Type', 'Appointment Date', 'Duration', 'Status', 'Hospital', 'Price']]
    for appointment in appointments:
        data.append([
            f"{appointment.user.first_name} {appointment.user.last_name}",
            appointment.vac.vname,
            appointment.datetime.strftime('%d %b %Y'),
            appointment.vac.vdiscription,
            appointment.status,
            appointment.hospital.first_name,
            f"₹{appointment.vac.vprice}"
        ])

    # Create table
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    elements.append(table)
    doc.build(elements)

    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="vaccination_data_{datetime.now().strftime("%Y%m%d")}.pdf"'
    return response












