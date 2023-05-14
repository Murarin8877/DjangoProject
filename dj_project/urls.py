"""dj_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
""" from django.conf.urls import url """
from mysite import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Hellow/',views.Hellow),
    
    path('index/',views.index),
    path('login/',views.login),
    path('grade/',views.grade),
    path('grade/type/',views.type),
    path('grade/type/bihua', views.bihua, name='bihua'),
    path('grade/type/keyboard',views.keyboard),
    
]
