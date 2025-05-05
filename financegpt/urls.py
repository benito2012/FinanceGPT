from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login')),  # 👈 redirect homepage to /login
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
