"""Dialektor_ URL Configuration

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
from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView

from dialektor.views import index_home, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'(^$|login$)', index_home),  # Regex: Either nothing (aka. index page) or /login
    url(r'signup$', signup),          # signup page
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/graphics/icon/favicon.ico')), # Google chrome favicon fix



]
