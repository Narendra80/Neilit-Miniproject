from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    # Dashboard & Home
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Authentication System
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    
    # CRUD Operations & Directory
    path('list/', views.employee_list, name='list'),
    path('create/', views.employee_create, name='create'),
    path('update/<int:pk>/', views.employee_update, name='update'),
    path('delete/<int:pk>/', views.employee_delete, name='delete'),
    
    # Demo & Legacy Views
    path('simple/', views.simple_http_demo, name='simple_http'),
    path('cbv/', views.HomeView.as_view(), name='home_cbv'),
    path('session/', views.session_demo, name='session_demo'),
]
