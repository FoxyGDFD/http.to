from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('carat/', CaratView.as_view(), name='carat'),
    path('color/', ColorView.as_view(), name='color'),
    path('transparency/', TransparencyView.as_view(), name='transparency'),
    path('cut/', CutView.as_view(), name='cut'),
    path('free-vygem/', FreeVygemView.as_view(), name='free-vygem'),
]