
from django.db import router   #ENRUTADOR

#Django rest framework
from rest_framework.routers import DefaultRouter
#views
from .viewsets.component import DispEntryViewSets, DispOutputViewSets, InternalDeviceViewSets, SpeakerViewSets, ProcessorViewSets, MotherboardViewSets, MouseViewSets, KeyboardViewSets, MonitorViewSets #llamada a las viewsets de views.py
from .viewsets.computer import ComputerViewSets
from .viewsets.order import DetailsOrderViewSets, OrderViewSets

router = DefaultRouter()
router.register(r'entries', DispEntryViewSets)
router.register(r'outputs', DispOutputViewSets)
router.register(r'internals', InternalDeviceViewSets)
router.register(r'mouses', MouseViewSets)
router.register(r'keyboards', KeyboardViewSets)
router.register(r'monitors', MonitorViewSets)
router.register(r'speakers', SpeakerViewSets)
router.register(r'motherboards', MotherboardViewSets)
router.register(r'processors', ProcessorViewSets)
router.register(r'computers', ComputerViewSets)
router.register(r'orders', OrderViewSets)
router.register(r'detailsOrders', DetailsOrderViewSets)

urlpatterns = router.urls

urlpatterns += [
  
]