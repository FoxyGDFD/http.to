from django.urls import path
from .views import *

urlpatterns = [
    path('', CaratView.as_view(), name='carat'),
    path('free-vygem/', FreeVygemView.as_view(), name='free-vygem'),
    path('cut/', CutView.as_view(), name='cut')
]