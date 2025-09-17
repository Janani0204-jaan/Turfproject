from django.contrib import admin
from .models import Booking
from.models import Turf
from .models import QuickMessage
# Register your models here.
admin.site.register(Booking)
admin.site.register(Turf)
@admin.register(QuickMessage)
class QuickMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')

