from django.contrib import admin
from .models import Contact,Vaccine,FAQ,Profile,Appointment

# Custom admin class for Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bdate', 'phone', 'role')
    search_fields = ('user__username', 'user__email')
    list_filter = ('role', 'bdate')

# Register your models here.
admin.site.register(Contact)
admin.site.register(Vaccine)
admin.site.register(FAQ)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Appointment)



