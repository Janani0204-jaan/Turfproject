from django.db import models
from django.utils import timezone

# Create your models here.



class Turf(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    team_name = models.CharField(max_length=100)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    slot = models.CharField(max_length=50)
    is_tournament = models.BooleanField()
    tournament_name = models.CharField(max_length=100, blank=True)
    payment_method = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    booking_date = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(default=False)
    is_booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



from django.db import models

class QuickMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
