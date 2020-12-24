from django.urls import path
from . import views
 
urlpatterns = [
  path('', views.PostAPI.as_view())
]