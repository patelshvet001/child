from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns= [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact_us,name='contact'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('profile/<int:id>/',views.userprofile,name='userprofile'),
    path('edit_profile/<int:id>/',views.editprofile,name='editprofile'),
    path('handle_edit/<int:id>',views.handle_edit,name='handle_edit'),
    path('my_appointments/',views.myappointment,name='myappointment'),
    path('search_data/',views.search_data,name='search_data'),
    path('update_status/<int:appointment_id>/', views.update_appointment_status, name='update_appointment_status'),
    
    path('password-reset/',views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='hospital/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='hospital/password_reset_complete.html'),
         name='password_reset_complete'),

     path('change-password/', views.change_password, name='change_password'),



]