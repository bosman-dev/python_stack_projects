from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls'), name ='login'), 
    path("signup/", views.SignUp.as_view(), name='signup'),
    path('logout/', views.logout_view, name='logout'),
]