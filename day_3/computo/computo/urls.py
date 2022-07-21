
from django.db import router   #ENRUTADOR

#Django rest framework
from rest_framework.routers import DefaultRouter
#views
from .views import DispEntryViewSets, DispOutputViewSets, SpeakerViewSets, ProcessorViewSets, MotherboardViewSets, MouseViewSets, KeyboardViewSets, MonitorViewSets, ComputerViewSets, OrderViewSets #llamada a las viewsets de views.py

router = DefaultRouter()
router.register(r'entries', DispEntryViewSets)
router.register(r'outputs', DispOutputViewSets)
router.register(r'mouses', MouseViewSets)
router.register(r'keyboards', KeyboardViewSets)
router.register(r'monitors', MonitorViewSets)
router.register(r'speakers', SpeakerViewSets)
router.register(r'motherboards', MotherboardViewSets)
router.register(r'processors', ProcessorViewSets)
router.register(r'computers', ComputerViewSets)
router.register(r'orders', OrderViewSets)

urlpatterns = router.urls

urlpatterns += [
  
]