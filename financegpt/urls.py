from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from core.views import dashboard_view  # adjust if your dashboard is in a different app

urlpatterns = [
    path('', lambda request: redirect('login')),  # Redirect root to login
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
