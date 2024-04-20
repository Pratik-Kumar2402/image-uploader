from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('set-session/', views.set_session, name='set_session'),
    path('get-session/', views.get_session, name='get_session'),
    path('delete-session/', views.delete_session, name='delete_session'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
]