# src/books/urls.py
from django.urls import path
from .views import BookListView, BookDetailView


# specify the app_name
app_name = "books"

# specify the path under urlpatterns, which is the default URL configuration
# specify the name of your FBV and pass it as the second argument to the path function
urlpatterns = [
   path('list/', BookListView.as_view(), name='list'),
   path('list/<pk>', BookDetailView.as_view(), name='detail'),
]