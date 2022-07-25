from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('postapp.urls')),
    path('api/user/', include('accounts.urls')),
    path('api/user/', include('allauth.urls')),   
]