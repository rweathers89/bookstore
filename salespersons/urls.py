# src/salespersons/urls.py
from django.urls import path
from .views import salespersons

# specify the app_name
app_name = "salespersons"

# specify the path under urlpatterns, which is the default URL configuration
# specify the name of your FBV and pass it as the second argument to the path function
urlpatterns = [
    path("salespersons/", salespersons),
]