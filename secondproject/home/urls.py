from django.urls import path, include
from home.views import *

urlpatterns = [
    path('', home_view),
    path('contact/', contact_view),
]