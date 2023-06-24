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
from cryptocons import  views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    ## when enter home defaults to home page

    path('', views.home, name='homepage_url'),
    path('register/', views.register, name='register_url'),
    path('login/', auth_views.LoginView.as_view(template_name='cryptocons/login.html'), name='login_url'),
    path('Logout/', auth_views.LogoutView.as_view(template_name='cryptocons/logout.html'), name='logout_url'),
    path('craiclounge/', views.craicLounge,name='craic_lounge'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('craiclounge/profile/', views.profile, name='profile'),
    path('qr_generator/', views.qr_generator, name='qr_generator'),
    re_path('qr_scan', views.qr_scan, name='qr_scan'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
