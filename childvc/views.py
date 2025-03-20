from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from PIL import Image
import datetime
import io
import os
import qrcode

from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact,FAQ,Vaccine,Profile,Appointment
from django.contrib.auth.models import User,auth
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from io import BytesIO
from .models import VaccinationRecord
from .decorators import patient_required, hospital_required
from django.db.models import Q

# *Email....................................................................
# *4 Emaill
# import requests
# import smtplib
# from email.mime.text import MIMEText

# # Function to generate a temporary email using Guerrilla Mail
# def generate_temp_email():
#     url = "https://api.guerrillamail.com/ajax.php?f=get_email_address"
#     response = requests.get(url)

#     if response.status_code == 200:
#         return response.json().get("email_addr")
#     else:
#         return f"Error: {response.status_code}, {response.text}"

# # Function to check received emails
# def get_received_emails(temp_email):
#     url = f"https://api.guerrillamail.com/ajax.php?f=check_email&email={temp_email}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         return f"Error: {response.status_code}, {response.text}"

# # Function to send an email
# def send_email(recipient_email):
#     sender_email = "your_email@gmail.com"  # Replace with your Gmail
#     sender_password = "your_app_password"  # Use an app password (not your actual Gmail password)

#     subject = "Test Message"
#     body = "Hello! This is a test message."

#     msg = MIMEText(body)
#     msg["Subject"] = subject
#     msg["From"] = sender_email
#     msg["To"] = recipient_email

#     try:
#         with smtplib.SMTP("smtp.gmail.com", 587) as server:
#             server.starttls()
#             server.login(sender_email, sender_password)
#             server.sendmail(sender_email, recipient_email, msg.as_string())
#         print(f"✅ Email sent successfully to {recipient_email}")
#     except Exception as e:
#         print("❌ Error sending email:", str(e))

# # Example usage
# temp_email = "un8gpx+7rrk1dm6z2arg@grr.la"
# print("📝 Temporary Email:", temp_email)

# send_email(temp_email)  # Send "Hello" message

# received_emails = "rafekob887@envoes.com"  # Changed variable name from messages to received_emails
# print("📩 Received Emails:", received_emails)
# -----------------------------------------------
# *3 email
# from faker import Faker
# import requests
# import smtplib
# from email.mime.text import MIMEText

# fake = Faker()

# # Generate a fake temp email
# def generate_temp_email():
#     return fake.user_name() + "@mailinator.com"  # Replace with a valid temp mail domain

# # Fetch messages for the generated temp email
# def get_received_emails(temp_email):
#     url = f"https://api.mailinator.com/api/v2/inbox?to={temp_email.split('@')[0]}"
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer YOUR_API_KEY"  # Replace with your API key if needed
#     }
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         return f"Error: {response.status_code}, {response.text}"

# # Send an email using SMTP
# def send_email(recipient_email):
#     sender_email = "your_email@gmail.com"  # Replace with your email
#     sender_password = "your_app_password"  # Use an app password (not your actual Gmail password)
    
#     subject = "Test Message"
#     body = "Hello! This is a test message."

#     msg = MIMEText(body)
#     msg["Subject"] = subject
#     msg["From"] = sender_email
#     msg["To"] = recipient_email

#     try:
#         with smtplib.SMTP("smtp.gmail.com", 587) as server:
#             server.starttls()
#             server.login(sender_email, sender_password)
#             server.sendmail(sender_email, recipient_email, msg.as_string())
#         print(f"Email sent successfully to {recipient_email}")
#     except Exception as e:
#         print("Error sending email:", str(e))

# # Example usage
# temp_email = generate_temp_email()
# print("Temporary Email:", temp_email)

# send_email(temp_email)  # Send "Hello" message
# messages = get_received_emails(temp_email)
# print("Received Emails:", messages)

#  *2 email
# from faker import Faker

# fake = Faker()

# def generate_temp_email():
#     return fake.email()

# # Example usage
# print(generate_temp_email())  # Output: random.email@example.com    

# import requests

# def get_temp_email():
#     url = "https://www.tempmail.us.com/"
#     response = requests.post(url)
#     if response.status_code == 201:
#         return response.json().get("email")
#     return None

# # Example usage
# print(get_temp_email())
# def get_received_emails(temp_email):
#     url = f"https://api.temp-mail.io/v1/email/{temp_email}/messages"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     return None

# # Example usage
# temp_email = "v9tzxhd89zdaqgc@tempmail.us.com"
# print(get_received_emails(temp_email))



#  *1 email
# from django.core.mail import send_mail

# def send_vaccine_reminder(user_email):
#     subject = "Vaccination Reminder"
#     message = "Dear Parent, your child's vaccination is due soon. Please visit our center."
#     from_email = "your_email@gmail.com"
#     recipient_list = [user_email]

#     send_mail(subject, message, from_email, recipient_list)

# *Email....................................................................
#2 .................................................................
from PIL import Image, ImageDraw, ImageFont
import os
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User )
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User )
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
#2 .................................................................

#1 .................................................................
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Appointment

@patient_required
@login_required(login_url='/login/')
def view_certificate_details(request, appointment_id):
    appointment = get_object_or_404(Appointment, aid=appointment_id)
    context = {
        'appointment': appointment,
        'certificate_id': appointment.aid,
        'child_name': f"{appointment.user.first_name} {appointment.user.last_name}",
        'birth_date': appointment.user.profile.bdate.strftime('%d %B %Y') if appointment.user.profile.bdate else "Not provided",
        'vaccine_name': appointment.vac.vname,
        'price': f"₹{appointment.vac.vprice:,.2f}",
        'status': appointment.status,
        'appointment_date': appointment.datetime.strftime('%d %B %Y'),
        'hospital_name': appointment.hospital.first_name,
        'hospital_address': appointment.hospital.profile.address if appointment.hospital.profile and appointment.hospital.profile.address else "Not provided",
        'issue_date': datetime.datetime.now().strftime('%d %B %Y')
    }
    return render(request, 'certificate_details.html', context)

@patient_required
@login_required(login_url='/login/')
def appointment_slip(request, appointment_id):
    try:
        appointment = Appointment.objects.get(aid=appointment_id)
        
        # Check if the user is authorized to view this appointment
        if request.user != appointment.user and not request.user.is_superuser:
            messages.error(request, "You are not authorized to view this appointment slip.")
            return redirect('my_appointments')
            
        context = {
            'appointment': appointment,
            'child_name': appointment.user.first_name + ' ' + appointment.user.last_name,
            'hospital_name': appointment.hospital.first_name,
            'vaccine_name': appointment.vac.vname,
            'appointment_date': appointment.datetime.strftime("%d %B %Y, %I:%M %p"),
            'price': appointment.vac.vprice,
            'status': appointment.status
        }
        
        return render(request, 'appointment_slip.html', context)
    except Appointment.DoesNotExist:
        messages.error(request, "Appointment not found.")
        return redirect('my_appointments')

@patient_required
@login_required(login_url='/login/')
def download_appointment_slip(request, appointment_id):
    try:
        appointment = Appointment.objects.get(aid=appointment_id)
        
        # Check if the user is authorized to download this appointment slip
        if request.user != appointment.user and not request.user.is_superuser:
            messages.error(request, "You are not authorized to download this appointment slip.")
            return redirect('my_appointments')
            
        # Create the PDF
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        
        # Add modern gradient background
        p.setFillColorRGB(0.95, 0.98, 1)  # Very light blue
        p.rect(0, 0, width, height, fill=1)
        
        # Add white content area with shadow effect
        p.setFillColor(colors.white)
        p.setStrokeColorRGB(0.8, 0.8, 0.8)  # Light gray for shadow
        p.setLineWidth(1)
        # Draw shadow
        p.rect(45, 45, width-90, height-90, fill=1, stroke=1)
        # Draw main white background
        p.setFillColor(colors.white)
        p.rect(40, 40, width-80, height-80, fill=1)
        
        # Add modern border with rounded corners
        p.setStrokeColorRGB(0.2, 0.6, 1)  # Modern blue
        p.setLineWidth(2)
        p.roundRect(50, 50, width-100, height-100, 10, stroke=1)
        
        # Add header with modern styling
        p.setFillColorRGB(0.2, 0.6, 1)  # Modern blue
        p.setFont("Helvetica-Bold", 24)  # Reduced from 32
        title = "Appointment Slip"
        title_width = p.stringWidth(title, "Helvetica-Bold", 24)
        p.drawString((width - title_width) / 2, height - 100, title)
        
        # Add decorative elements
        p.setLineWidth(3)
        p.line(70, height - 120, width-70, height - 120)
        p.setLineWidth(1)
        p.line(100, height - 125, width-100, height - 125)
        
        # Patient Information Section with modern styling
        current_y = height - 180
        p.setFillColorRGB(0.2, 0.6, 1)
        p.setFont("Helvetica-Bold", 16)  # Reduced from 20
        p.drawString(70, current_y, "PATIENT INFORMATION")
        
        # Add modern box for patient info
        p.setFillColorRGB(0.95, 0.98, 1)  # Very light blue
        p.setStrokeColorRGB(0.8, 0.9, 1)  # Light blue border
        box_height = 60  # Reduced from 70
        p.roundRect(60, current_y - box_height, width-120, box_height, 8, fill=1, stroke=1)
        
        # Add patient details with improved typography
        p.setFillColorRGB(0.2, 0.3, 0.4)  # Dark blue-gray text
        p.setFont("Helvetica", 10)  # Reduced from 14
        p.drawString(80, current_y - 25, f"Patient Name: {appointment.user.first_name} {appointment.user.last_name}")
        p.drawString(80, current_y - 40, f"Appointment ID: {appointment.aid}")
        
        # Appointment Details Section
        current_y -= 90  # Reduced spacing
        p.setFillColorRGB(0.2, 0.6, 1)
        p.setFont("Helvetica-Bold", 16)  # Reduced from 20
        p.drawString(70, current_y, "APPOINTMENT DETAILS")
        
        # Add modern box for appointment details
        p.setFillColorRGB(0.95, 0.98, 1)
        box_height = 80  # Reduced from 90
        p.roundRect(60, current_y - box_height, width-120, box_height, 8, fill=1, stroke=1)
        
        # Add appointment details
        p.setFillColorRGB(0.2, 0.3, 0.4)
        p.setFont("Helvetica", 10)  # Reduced from 14
        p.drawString(80, current_y - 25, f"Vaccine Name: {appointment.vac.vname}")
        p.drawString(80, current_y - 40, f"Price: Rs.{appointment.vac.vprice}")
        p.drawString(400, current_y - 25, f"Status: {appointment.status}")
        p.drawString(80, current_y - 55, f"Date: {appointment.datetime.strftime('%d %B %Y, %I:%M %p')}")
        
        # Hospital Information Section
        current_y -= 100  # Reduced spacing
        p.setFillColorRGB(0.2, 0.6, 1)
        p.setFont("Helvetica-Bold", 16)  # Reduced from 20
        p.drawString(70, current_y, "HOSPITAL INFORMATION")
        
        # Add modern box for hospital info
        p.setFillColorRGB(0.95, 0.98, 1)
        box_height = 80  # Reduced from 90
        p.roundRect(60, current_y - box_height, width-120, box_height, 8, fill=1, stroke=1)
        
        # Add hospital details
        p.setFillColorRGB(0.2, 0.3, 0.4)
        p.setFont("Helvetica", 10)  # Reduced from 14
        p.drawString(80, current_y - 25, f"Hospital Name: {appointment.hospital.first_name}")
        
        # Add hospital address with text wrapping
        if appointment.hospital.profile and appointment.hospital.profile.address:
            address = f"Address: {appointment.hospital.profile.address}"
            address_lines = wrap_text(p, address, width-200, "Helvetica", 10)  # Reduced from 14
            y = current_y - 40
            for line in address_lines:
                p.drawString(80, y, line)
                y -= 15  # Reduced from 20
        
        # Important Notes Section
        current_y -= 100  # Reduced spacing
        p.setFillColorRGB(0.2, 0.6, 1)
        p.setFont("Helvetica-Bold", 16)  # Reduced from 20
        p.drawString(70, current_y, "IMPORTANT NOTES")
        
        # Add modern box for notes
        p.setFillColorRGB(0.95, 0.98, 1)
        box_height = 90  # Reduced from 100
        p.roundRect(60, current_y - box_height, width-120, box_height, 8, fill=1, stroke=1)
        
        # Add notes with bullet points
        p.setFillColorRGB(0.2, 0.3, 0.4)
        p.setFont("Helvetica", 9)  # Reduced from 12
        notes = [
            "• Please arrive 15 minutes before your scheduled appointment time",
            "• Bring your child's previous vaccination records if any",
            "• Make sure your child is healthy on the day of vaccination",
            "• Keep this appointment slip with you for reference"
        ]
        y = current_y - 25
        for note in notes:
            p.drawString(80, y, note)
            y -= 15  # Reduced from 20
        
        # Generate QR Code
        qr_data = f"Appointment ID: {appointment.aid}\n"
        qr_data += f"Patient: {appointment.user.first_name} {appointment.user.last_name}\n"
        qr_data += f"Vaccine: {appointment.vac.vname}\n"
        qr_data += f"Date: {appointment.datetime.strftime('%d %B %Y, %I:%M %p')}\n"
        qr_data += f"Hospital: {appointment.hospital.first_name}\n"
        qr_data += f"Status: {appointment.status}"
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        
        # Save QR to buffer
        qr_buffer = io.BytesIO()
        qr_img.save(qr_buffer, format='PNG')
        qr_buffer.seek(0)
        
        # Draw QR code in bottom right with modern styling
        qr_size = 90  # Reduced from 100
        qr_x = width - qr_size - 80
        qr_y = 80
        
        # Add QR code background
        p.setFillColorRGB(0.95, 0.98, 1)
        p.roundRect(qr_x - 10, qr_y - 10, qr_size + 20, qr_size + 20, 8, fill=1, stroke=1)
        
        # Draw QR code
        p.drawImage(ImageReader(qr_buffer), qr_x, qr_y, width=qr_size, height=qr_size)
        
        # Add QR code label with modern styling
        p.setFillColorRGB(0.2, 0.3, 0.4)
        p.setFont("Helvetica-Bold", 10)  # Reduced from 12
        qr_label = "Scan QR Code"
        label_width = p.stringWidth(qr_label, "Helvetica-Bold", 10)
        p.drawString(qr_x + (qr_size - label_width)/2, qr_y - 20, qr_label)
        
        # Add modern footer with gradient
        p.setFillColorRGB(0.2, 0.6, 1)
        p.setFont("Helvetica-Bold", 10)  # Reduced from 14
        footer_text = "Thank you for choosing our vaccination service!"
        footer_width = p.stringWidth(footer_text, "Helvetica-Bold", 10)
        p.drawString((width - footer_width) / 2, 70, footer_text)
        
        # Add date with modern styling
        p.setFillColorRGB(0.5, 0.5, 0.5)
        p.setFont("Helvetica", 9)  # Reduced from 12
        date_text = f"Generated on: {datetime.datetime.now().strftime('%d %B %Y, %I:%M %p')}"
        date_width = p.stringWidth(date_text, "Helvetica", 9)
        p.drawString((width - date_width) / 2, 55, date_text)
        
        p.showPage()
        p.save()
        
        # Get the value of the BytesIO buffer and write it to the response
        pdf = buffer.getvalue()
        buffer.close()
        
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="appointment_slip_{appointment.aid}.pdf"'
        return response
        
    except Appointment.DoesNotExist:
        messages.error(request, "Appointment not found.")
        return redirect('my_appointments')

def wrap_text(canvas, text, max_width, font_name, font_size):
    canvas.setFont(font_name, font_size)
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        current_line.append(word)
        line_width = canvas.stringWidth(' '.join(current_line), font_name, font_size)
        if line_width > max_width:
            if len(current_line) > 1:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]
            else:
                lines.append(word)
                current_line = []
    
    if current_line:
        lines.append(' '.join(current_line))
    return lines

@hospital_required
@login_required(login_url='/login/')
def approve_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, aid=appointment_id, hospital=request.user)
    
    if appointment.status == 'Pending':
        appointment.status = 'Approved'
        appointment.save()
        messages.success(request, 'Appointment approved successfully!')
    else:
        messages.error(request, 'Only pending appointments can be approved.')
    
    return redirect('myappointment')

@hospital_required
@login_required(login_url='/login/')
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, aid=appointment_id, hospital=request.user)
    
    if appointment.status in ['Pending', 'Approved']:
        appointment.status = 'Cancelled'
        appointment.save()
        messages.success(request, 'Appointment cancelled successfully!')
    else:
        messages.error(request, 'Only pending or approved appointments can be cancelled.')
    
    return redirect('myappointment')

@hospital_required
@login_required(login_url='/login/')
def complete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, aid=appointment_id, hospital=request.user)
    
    if appointment.status == 'Approved':
        appointment.status = 'Completed'
        appointment.save()
        messages.success(request, 'Appointment marked as completed successfully!')
    else:
        messages.error(request, 'Only approved appointments can be marked as completed.')
    
    return redirect('myappointment')

@login_required(login_url='/login/')
def generate_certificate(request, appointment_id):
    # Fetch the appointment details
    appointment = get_object_or_404(Appointment, aid=appointment_id)
    
    # Check if user is either the patient or the hospital staff
    if request.user != appointment.user and request.user != appointment.hospital:
        messages.error(request, 'You do not have permission to generate this certificate.')
        return redirect('myappointment')
    
    # Allow certificate generation for both approved and completed appointments
    if appointment.status not in ['Approved', 'Completed']:
        messages.error(request, 'Only approved or completed appointments can generate certificates.')
        return redirect('myappointment')

    # Create certificate data for QR code
    certificate_data = {
        'certificate_id': appointment.aid,
        'name': f"{appointment.user.first_name} {appointment.user.last_name}",
        'vaccine': appointment.vac.vname,
        'date': appointment.datetime.strftime('%d %B %Y'),
        'hospital': appointment.hospital.first_name,
        'status': appointment.status,
        'price': f"Rs. {appointment.vac.vprice:,.2f}"
    }
    
    # Convert to string for QR code
    qr_data = f"Certificate ID: {certificate_data['certificate_id']}\n" \
              f"Name: {certificate_data['name']}\n" \
              f"Vaccine: {certificate_data['vaccine']}\n" \
              f"Date: {certificate_data['date']}\n" \
              f"Hospital: {certificate_data['hospital']}\n" \
              f"Status: {certificate_data['status']}\n" \
              f"Price: {certificate_data['price']}"

    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificate_{appointment.aid}.pdf"'

    # Create a PDF canvas
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Define margins and spacing
    left_margin = 70
    right_margin = width - 70
    top_margin = height - 50
    bottom_margin = 70
    content_width = right_margin - left_margin

    # Add decorative background
    p.setFillColor(colors.lightblue)
    p.rect(0, 0, width, height, fill=1)
    
    # Add white background for content
    p.setFillColor(colors.white)
    p.rect(left_margin - 20, bottom_margin - 20, content_width + 40, height-80, fill=1)

    # Add decorative border
    p.setStrokeColor(colors.blue)
    p.setLineWidth(3)
    p.rect(left_margin - 10, bottom_margin - 10, content_width + 20, height-100)

    # Add certificate title
    p.setFillColor(colors.black)
    p.setFont("Times-Bold", 30)
    title = "VACCINATION CERTIFICATE"
    title_width = p.stringWidth(title, "Times-Bold", 30)
    p.drawString((width - title_width) / 2, top_margin - 60, title)

    # Add decorative lines under title
    p.setStrokeColor(colors.blue)
    p.setLineWidth(2)
    line_width = 400
    line_start = (width - line_width) / 2
    p.line(line_start, top_margin - 70, line_start + line_width, top_margin - 70)

    # Calculate positions for image and QR code
    image_x = right_margin - 120  # Position for image on right
    image_y = top_margin - 210  # Higher position for image
    
    # QR code position in bottom left corner
    qr_x = left_margin  # Align with left margin
    qr_y = bottom_margin + 10  # Slightly above bottom margin
    qr_width = 120  # QR code size
    qr_height = 120

    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR to buffer
    qr_buffer = io.BytesIO()
    qr_img.save(qr_buffer, format='PNG')
    qr_buffer.seek(0)
    
    # Draw QR code in bottom left corner
    p.drawImage(ImageReader(qr_buffer), qr_x, qr_y, width=qr_width, height=qr_height)
    
    # Add QR code label
    p.setFont("Times-Bold", 10)
    qr_label = "Scan QR Code to View Details"
    label_width = p.stringWidth(qr_label, "Times-Bold", 10)
    p.drawString(qr_x + (qr_width - label_width)/2, qr_y - 15, qr_label)

    # Add profile image if available
    try:
        profile_image = appointment.user.profile.profile_image
        if profile_image and hasattr(profile_image, 'path') and os.path.exists(profile_image.path):
            img = Image.open(profile_image.path)
            
            # Handle image orientation
            if hasattr(img, '_getexif') and img._getexif() is not None:
                orientation = img._getexif().get(274)  # 274 is the orientation tag
                if orientation is not None:
                    if orientation == 3:
                        img = img.rotate(180, expand=True)
                    elif orientation == 6:
                        img = img.rotate(270, expand=True)
                    elif orientation == 8:
                        img = img.rotate(90, expand=True)
            
            # Calculate aspect ratio and new dimensions
            aspect_ratio = img.width / img.height
            max_width = 100
            max_height = 100
            
            if aspect_ratio > 1:
                new_width = min(max_width, img.width)
                new_height = int(new_width / aspect_ratio)
            else:
                new_height = min(max_height, img.height)
                new_width = int(new_height * aspect_ratio)
            
            # Resize image with high quality
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Save to buffer with high quality
            img_buffer = io.BytesIO()
            img.save(img_buffer, format='JPEG', quality=100, optimize=True)
            img_buffer.seek(0)
            
            # Draw image
            p.drawImage(ImageReader(img_buffer), image_x, image_y, 
                       width=new_width, height=new_height)
            
    except Exception as e:
        print(f"Error adding profile image: {str(e)}")

    # Content starting position
    content_x = left_margin + 20
    current_y = top_margin - 120

    # Add personal information section
    p.setFont("Times-Bold", 20)
    p.drawString(content_x, current_y, "PERSONAL INFORMATION")
    current_y -= 30

    # Add details
    p.setFont("Times-Roman", 14)
    name = f"Name: {appointment.user.first_name} {appointment.user.last_name}"
    p.drawString(content_x, current_y, name)
    current_y -= 25

    # Add birth date
    birth_date = appointment.user.profile.bdate
    formatted_birth_date = birth_date.strftime('%d %B %Y') if birth_date else "Not provided"
    birth_date_text = f"Date of Birth: {formatted_birth_date}"
    p.drawString(content_x, current_y, birth_date_text)
    current_y -= 40

    # Add vaccination information section
    p.setFont("Times-Bold", 20)
    p.drawString(content_x, current_y, "VACCINATION DETAILS")
    current_y -= 30

    # Add vaccination details
    p.setFont("Times-Roman", 14)
    details = [
        f"Vaccine Name: {appointment.vac.vname}",
        f"Price: Rs. {appointment.vac.vprice:,.2f}",
        f"Status: {appointment.status}",
        f"Appointment Date: {appointment.datetime.strftime('%d %B %Y')}"
    ]
    
    for detail in details:
        p.drawString(content_x, current_y, detail)
        current_y -= 25

    current_y -= 15

    # Add hospital information section
    p.setFont("Times-Bold", 20)
    p.drawString(content_x, current_y, "HOSPITAL INFORMATION")
    current_y -= 30
    
    # Add hospital details
    p.setFont("Times-Roman", 14)
    p.drawString(content_x, current_y, f"Hospital Name: {appointment.hospital.first_name}")
    current_y -= 25
    
    if appointment.hospital.profile and appointment.hospital.profile.address:
        # Use wrap_text function for address
        address = f"Address: {appointment.hospital.profile.address}"
        address_lines = wrap_text(p, address, content_width - 40, "Times-Roman", 14)
        for line in address_lines:
            p.drawString(content_x, current_y, line)
            current_y -= 25
    else:
        current_y -= 25

    # Add certificate issue date
    current_y -= 10
    p.setFont("Times-Roman", 14)
    issue_date = f"Issue Date: {datetime.datetime.now().strftime('%d %B %Y')}"
    p.drawString(content_x, current_y, issue_date)

    # Add certificate ID at bottom with proper margin
    p.setFont("Times-Bold", 12)
    cert_id = f"Certificate ID: {appointment.aid}"
    cert_id_width = p.stringWidth(cert_id, "Times-Bold", 12)
    p.drawString(right_margin - cert_id_width - 20, bottom_margin + 10, cert_id)

    # Add signature section with proper margins
    p.setStrokeColor(colors.blue)
    p.setLineWidth(2)
    signature_width = 200
    signature_x = right_margin - signature_width - 40  # Increased margin
    p.line(signature_x, bottom_margin + 60, signature_x + signature_width, bottom_margin + 60)
    
    p.setFont("Times-Bold", 14)
    signature_text = "Authorized Signature"
    signature_text_width = p.stringWidth(signature_text, "Times-Bold", 14)
    p.drawString(signature_x + (signature_width - signature_text_width) / 2, 
                bottom_margin + 40, signature_text)

    p.showPage()
    p.save()
    return response

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('index')


# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


@patient_required
@login_required(login_url='/login/')
def myappointment(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request,'my_appointments.html',{'appointments':appointments})


@patient_required
@login_required(login_url='/login/')
def bookappointment(request):
    if request.method == 'POST':
        hos = request.POST['hos']
        vac = request.POST['vac']
        date = request.POST['date']
        hospital = User.objects.get(id = hos)
        vac_data = Vaccine.objects.get(vid=vac)
        a = Appointment(user=request.user,hospital=hospital,vac=vac_data,datetime=date)
        a.save()
        messages.success(request,"your appointment is booked ..")
        return redirect('/')
    
    pro = Profile.objects.filter(role='2')
    hospitals = []
    for p in pro:    
        u = p.user.id
        hospitals.append(User.objects.get(id=u))
    vac = Vaccine.objects.all()
    
    # Get selected vaccine ID from URL if present
    selected_vaccine_id = request.GET.get('vac')
    selected_vaccine = None
    if selected_vaccine_id:
        try:
            selected_vaccine = Vaccine.objects.get(vid=selected_vaccine_id)
        except Vaccine.DoesNotExist:
            pass
    
    return render(request,'bookappointment.html',{
        'hospitals': hospitals,
        'vaccine': vac,
        'selected_vaccine': selected_vaccine
    })


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
        return redirect('/')


    return render(request,'contact.html')

@login_required(login_url='/login/')
def Faq_data(request):
    if request.method == 'POST':
        questions = request.POST['que']
        s = FAQ(question=questions,u_id=request.user)
        s.save()
        messages.success(request,"Your question has been added..")
        return redirect("/faq/")
        
    data = FAQ.objects.all()
    return render(request,'faq.html',{'data':data})

def forgotpassword(reuqest):
    return render(reuqest,'forgotpassword.html')

def service(request):
    return render(request,'service.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        bdate_str = request.POST['bdate']  # Get birth date from form

        # Input validation
        if not all([fname, lname, uname, email, pass1, pass2, bdate_str]):
            messages.error(request, "All fields are required")
            return redirect('/register/')

        # Password validation
        if len(pass1) < 8:
            messages.error(request, "Password must be at least 8 characters long")
            return redirect('/register/')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('/register/')

        # Check for existing username
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists")
            return redirect('/register/')
        
        # Check for existing email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('/register/')
        
        try:
            # Convert birth date string to Date object
            try:
                bdate = datetime.datetime.strptime(bdate_str, '%Y-%m-%d').date()
            except ValueError:
                messages.error(request, "Invalid date format. Please use YYYY-MM-DD format.")
                return redirect('/register/')

            # Create user
            user = User.objects.create_user(
                first_name=fname,
                last_name=lname,
                username=uname,
                email=email,
                password=pass1
            )
            user.save()
            
            # Update profile with birth date
            profile = Profile.objects.get(user=user)
            profile.bdate = bdate
            profile.save()
            
            messages.success(request, "Account created successfully! Please login.")
            return redirect('/login/')
            
        except Exception as e:
            messages.error(request, f"An error occurred during registration: {str(e)}")
            return redirect('/register/')

    return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['pass']

        user = auth.authenticate(username=uname,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'Logged In...')
            return redirect('/')
        else:
            print('Invalid Credentials....')
            return redirect('/login/')
    return render(request,'login.html')

@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    messages.error(request,'your account is LOGGED OUT..')
    return redirect('/')

@patient_required
@login_required(login_url='/login/')
def userprofile(request,id):
    user = User.objects.get(id=id)
    user_obj = Profile.objects.get(user=user)
    return render(request,'userprofile.html',{'user':user,'user_obj':user_obj})

@patient_required
@login_required(login_url='/login/')
def editprofile(request,id):
    for_edit=User.objects.get(id=id)
    for_profile=Profile.objects.get(user=for_edit)
    return render(request,'EditProfile.html',{'for_profile':for_profile})

@login_required(login_url='/login/')
def handle_edit(request,id):
    # Get the user to edit (not the current user)
    user_to_edit = User.objects.get(id=id)
    profile_to_edit = Profile.objects.get(user=user_to_edit)
    
    # Check if the current user is editing their own profile
    if request.user != user_to_edit:
        messages.error(request, 'You can only edit your own profile.')
        return redirect('userprofile', id=id)
        
    if request.method == 'POST':
        try:
            # Handle profile image upload only if a new image is provided
            if 'p_image' in request.FILES:
                img = request.FILES['p_image']
                profile_to_edit.profile_image = img
            
            firstname = request.POST.get('edit_firstname','')
            lastname = request.POST.get('edit_lastname','')
            username = request.POST.get('edit_username','')
            phone_no = request.POST.get('edit_phoneno','')
            email = request.POST.get('edit_email','')
            address = request.POST.get('edit_address','')
            bdate_str = request.POST.get('edit_bdate','')  # Get birth date from form
            
            # Convert birth date string to Date object if it's not empty
            if bdate_str:
                try:
                    bdate = datetime.datetime.strptime(bdate_str, '%Y-%m-%d').date()
                except ValueError:
                    messages.error(request, 'Invalid date format. Please use YYYY-MM-DD format.')
                    return redirect('editprofile', id=id)
            else:
                bdate = None

            user_to_edit.first_name = firstname
            user_to_edit.last_name = lastname
            user_to_edit.username = username
            profile_to_edit.phone = phone_no
            user_to_edit.email = email
            profile_to_edit.address = address
            profile_to_edit.bdate = bdate  # Save the converted Date object

            user_to_edit.save()
            profile_to_edit.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('userprofile', id=id)  # Redirect to user profile page
            
        except Exception as e:
            messages.error(request, f'Error updating profile: {str(e)}')
            return redirect('editprofile', id=id)
    else:
        messages.error(request,'Something went wrong.')
        return redirect('userprofile', id=id)

@login_required(login_url='/login/')
def vaccine_search(request):
    vaccines = Vaccine.objects.all()
    search_query = request.GET.get('search', '')
    price_range = request.GET.get('price_range', '')

    if search_query:
        vaccines = vaccines.filter(vname__icontains=search_query)

    if price_range:
        if price_range == '0-200':
            vaccines = vaccines.filter(vprice__lte=200)
        elif price_range == '201-400':
            vaccines = vaccines.filter(vprice__gt=200, vprice__lte=400)
        elif price_range == '401-600':
            vaccines = vaccines.filter(vprice__gt=400, vprice__lte=600)
        elif price_range == '601+':
            vaccines = vaccines.filter(vprice__gt=600)

    context = {
        'vaccines': vaccines,
        'search_query': search_query,
        'price_range': price_range
    }
    return render(request, 'vaccine_search.html', context)

@hospital_required
@login_required(login_url='/login/')
def search_data(request):
    # Get all vaccines for the dropdown
    vaccines = Vaccine.objects.all()
    
    # Start with appointments for the logged-in hospital only
    appointments = Appointment.objects.filter(hospital=request.user)
    
    # Apply filters based on search parameters
    search_query = request.GET.get('search', '')
    vaccine_type = request.GET.get('vaccine_type', '')
    date_range = request.GET.get('date_range', '')
    
    if search_query:
        appointments = appointments.filter(
            Q(user__first_name__icontains=search_query) |
            Q(user__last_name__icontains=search_query)
        )
    
    if vaccine_type:
        appointments = appointments.filter(vac_id=vaccine_type)
    
    if date_range:
        today = datetime.datetime.now().date()
        if date_range == 'today':
            appointments = appointments.filter(datetime__date=today)
        elif date_range == 'week':
            week_ago = today - datetime.timedelta(days=7)
            appointments = appointments.filter(datetime__date__gte=week_ago)
        elif date_range == 'month':
            month_ago = today - datetime.timedelta(days=30)
            appointments = appointments.filter(datetime__date__gte=month_ago)
        elif date_range == 'year':
            year_ago = today - datetime.timedelta(days=365)
            appointments = appointments.filter(datetime__date__gte=year_ago)
    
    # Calculate statistics
    total_appointments = appointments.count()
    completed_appointments = appointments.filter(status='Completed').count()
    pending_appointments = appointments.filter(status='Pending').count()
    total_revenue = sum(appointment.vac.vprice for appointment in appointments if appointment.status == 'Completed')
    
    context = {
        'appointments': appointments,
        'vaccines': vaccines,
        'total_appointments': total_appointments,
        'completed_appointments': completed_appointments,
        'pending_appointments': pending_appointments,
        'total_revenue': total_revenue,
    }
    
    return render(request, 'search_data.html', context)

@login_required(login_url='/login/')
def change_status(request, appointment_id, new_status):
    if not request.user.is_superuser:
        messages.error(request, 'Only administrators can change appointment status.')
        return redirect('myappointment')
    
    appointment = get_object_or_404(Appointment, aid=appointment_id)
    
    # Validate the new status
    valid_statuses = ['Pending', 'Approved', 'Completed', 'Cancelled']
    if new_status not in valid_statuses:
        messages.error(request, 'Invalid status.')
        return redirect('myappointment')
    
    # Update the status
    appointment.status = new_status
    appointment.save()
    
    messages.success(request, f'Appointment status changed to {new_status} successfully!')
    return redirect('myappointment')









