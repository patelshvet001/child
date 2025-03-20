class Appointment(models.Model):
    # ... existing fields ...
    certificate_downloaded = models.BooleanField(default=False)
    
    class Meta:
        # ... existing meta ...
        
class Revenue(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    last_updated = models.DateTimeField(auto_now=True) 