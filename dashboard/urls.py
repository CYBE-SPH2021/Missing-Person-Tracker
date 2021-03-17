from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.case, name='case'),
]
