from django.contrib import admin

# Register your models here.
from .models import DispEntry, Mouse, Keyboard, Monitor, Computer, Order, DispOutput, InternalDevice, Speaker, Motherboard, Processor

admin.site.register(InternalDevice)
admin.site.register(DispEntry)
admin.site.register(DispOutput)
admin.site.register(Mouse)
admin.site.register(Keyboard)
admin.site.register(Monitor)
admin.site.register(Speaker)
admin.site.register(Motherboard)
admin.site.register(Processor)
admin.site.register(Computer)
admin.site.register(Order)