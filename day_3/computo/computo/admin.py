from django.contrib import admin

# Register your models here.
from .models.component import DispEntry, Mouse, Keyboard, Monitor, DispOutput, InternalDevice, Speaker, Motherboard, Processor
from .models.computer import Computer
from .models.order import Order, Detailsorder

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
admin.site.register(Detailsorder)
