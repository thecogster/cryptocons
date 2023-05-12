"""crm1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as user_views

from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    ## when enter home defaults to home page
    path('home', include('businesses.urls'), name='homepage'),
    path('craiclounge/', include('accounts.urls'), name='craic_lounge'),
    path('Login/', auth_views.LoginView.as_view(template_name= 'accounts/login.html'), name='login_url'),
    path('Logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout_url'),
    path('register/', include('accounts.urls'), name='register_url'),
    path('profile/', include('accounts.urls'), name='profile'),


    # path('profile/', include('accounts.urls'), name='profile'),

    # path('businesses/', include('businesses.urls'))

]
