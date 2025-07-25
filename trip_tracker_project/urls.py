# trip_tracker/urls.py

from django.contrib import admin
from django.urls import path
from trips import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('search/', views.search, name='search'),
    path('hotel/', views.hotel, name='hotel'),
    path('', views.home, name='home'),
   # path('home/',views.display_sensor_data,name='display_sensor_data')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
