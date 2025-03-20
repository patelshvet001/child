from django.db import models
from django.contrib.auth.models import User

class VaccinationRecord(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=100)
    vaccine_name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved')],
        default='Pending'
    )

    def __str__(self):
        return f"{self.child_name} - {self.vaccine_name} ({self.status})"

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField()
    msg = models.TextField()

    def __str__(self):
        return self.name

class Vaccine(models.Model):
    vid = models.AutoField(primary_key=True)
    vname=models.CharField(max_length=100)
    vprice = models.IntegerField(default=150)
    vdiscription=models.CharField(max_length=100)

    def __str__(self):
        return self.vname
    
class FAQ(models.Model):
    fid=models.AutoField(primary_key=True)
    question=models.TextField()
    answer=models.TextField()
    u_id = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    datetime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question 
    

# class Hospital(models.Model):
#     hid = models.AutoField(primary_key=True)
#     hname= models.CharField(max_length=100)
#     haddress=models.TextField()
#     gmail = models.CharField(max_length=50)
#     phone = models.BigIntegerField()

#     def __str__(self):
#         return self.hname

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Cancelled', 'Cancelled'),
    )

    aid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Person')
    hospital = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Hospital')
    vac = models.ForeignKey(Vaccine,on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    ROLE_CHOICES = (
        ("1" , "P"),
        ("2" , "H"),   

    )
    
    profile_id=models.AutoField(primary_key=True)
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bdate = models.DateField(null=True, blank=True)  # Birth date field

    profile_image=models.ImageField(upload_to="",default="img3.png")
    address = models.TextField(blank=True)
    phone = models.BigIntegerField(blank=True,null=True)
    role = models.CharField(max_length = 20,choices = ROLE_CHOICES,default = '1')
    
    def __str__(self):
        return str(self.user)


