from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.case, name='case'),
    path('map/', views.maps, name='map')
]
