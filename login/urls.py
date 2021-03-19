from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', include('dashboard.urls')),
]
