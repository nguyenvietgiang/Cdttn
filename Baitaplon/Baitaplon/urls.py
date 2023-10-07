"""
URL configuration for Baitaplon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home import views as home
from mytest import views as mytest
from conversation import views as conversation
from splash import views as splash
from contact import views as contact

urlpatterns = [
     path('admin/', admin.site.urls),
     path('home/',home.get_home),
     path('contact/', contact.get_contact),
     path('search_suggestions/',home.search_suggestions),
     path('search/', home.search),
     path('test/', mytest.test_view),
     path('convesation/', conversation.get_conversation),
     path('', splash.get_splash)
]
