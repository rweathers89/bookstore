# src/sales/urls.py
from django.urls import path
from .views import home, records

# specify the app_name
app_name = "sales"

# specify the path under urlpatterns, which is the default URL configuration
# specify the name of your FBV and pass it as the second argument to the path function
urlpatterns = [
    path("", home),
    path('sales/', records)
]