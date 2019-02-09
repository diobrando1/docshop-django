"""docshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import include, path, re_path

# urlpatterns = [
#     path('pdfshop/', include('pdfshop.urls')),
#     path('admin/', admin.site.urls),
# ]

from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from pdfshop import views as custom_views


urlpatterns = [
    re_path(r'^$', custom_views.home, name='home'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='pdfshop/login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    re_path(r'^signup/$', custom_views.signup, name='signup'),
    re_path(r'^upload/$', custom_views.upload, name='upload'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),
]
