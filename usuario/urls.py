from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView
from .views import index, admin, habitaciones, login, logout, registro, reservar
from usuario import views
#from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',views.index, name='index'),
    path('index.html/', views.index , name='index'),
    path('admin.html/', views.admin, name='admin'),
    path('login/',LoginView.as_view(template_name='usuario/index.html/login.html'), name="login"),
    path('logout/',LogoutView.as_view(template_name='usuario/index.html'),name="logout"), 
    path('registro.html/', views.registro, name='registro'),
    path('reservar.html/',views.reservar, name='reservar'),
    path('habitaciones.html/', views.habitaciones, name='habitaciones')
]

