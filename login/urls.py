from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('clogin/', views.clogin, name='clogin'),
    path('plogin/', views.plogin, name='plogin'),
    path('register/', views.register, name='register'),
    path('dashboard/', include('dashboard.urls')),
    path('suspect/',views.suspect, name='suspect'),
]
