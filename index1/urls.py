from django.urls import path
from .views import *

urlpatterns = [
    path('', index1.as_view(), name='index1'),


]
