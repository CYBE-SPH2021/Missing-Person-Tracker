from . import views
from django.urls import path, include

urlpatterns = [
    path('case/', views.case, name='case'),
    path('map/', views.maps, name='map'),
    path('webcamon/case/', views.case, name='case'),
    path('webcamon/map/', views.maps, name='map'),
    path('',views.dashboard, name='dashboard' ),
    path('webcamon/',views.realrec, name='realrec')
]
