from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('turnTo', turnTo.as_view(), name='turnTo')

]