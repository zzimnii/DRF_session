from django.urls import path, include
from rest_framework import urls
from rest_framework.routers import DefaultRouter
from . import views

user_router = DefaultRouter()
user_router.register('user',views.UserViewSet)

urlpatterns = [
    path('signup/',include(user_router.urls)),
    path('signup/<int:user_id>',include(user_router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]