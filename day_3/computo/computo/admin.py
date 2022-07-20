from django.contrib import admin

# Register your models here.
from .models import DispEntry, Mouse, Keyboard, Monitor, Computer, Order

admin.site.register(DispEntry)
admin.site.register(Mouse)
admin.site.register(Keyboard)
admin.site.register(Monitor)
admin.site.register(Computer)
admin.site.register(Order)