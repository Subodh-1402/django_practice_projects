from django.urls import path
from home.views import *

urlpatterns = [
    path('', index_view),
    path('contact/', contact_view),
    path('dynamic_route/<number>/', dynamic_route),   # here if u take only <number>, it passes the value as String. for other data you have to typecast that data before passsing in the URL.
]
