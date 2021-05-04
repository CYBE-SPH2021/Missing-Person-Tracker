from . import views
from django.urls import path, include

urlpatterns = [
    path('case/', views.case, name='case'),
    path('vehicle_case/', views.vehicle_case, name='vehicle_case'),
    path('track_vehicles/', views.track_vehicles, name='track_vehicles'),
    path('vehicle/', views.vehicle, name='vehicle'),
    path('case/map/', views.maps, name='map'),
    path('',views.dashboard, name='dashboard' ),
    path('webcamon/',views.realrec, name='realrec'),
    path('addcase/',views.addcase,name='addcase'),
    path('detectedmissing/',views.detectedmissing,name='detectedmissing'),
    path('case/info/',views.information,name='information')
]
