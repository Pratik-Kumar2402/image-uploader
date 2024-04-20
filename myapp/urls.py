from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-session/', views.get_session, name='get_session'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
]