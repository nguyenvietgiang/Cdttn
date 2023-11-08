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
from category import views as cate
from search import views as searchview
urlpatterns = [
     path('admin/', admin.site.urls),
     path('search/',home.get_home),
     path('contact/', contact.get_contact, name='save_contact'),
     path('search_suggestions/',home.search_suggestions),
     path('homesearch/', home.search, name="search"),
     path('translate/', home.translate, name='translate'),
     path('home/',searchview.get_product, name='product'),
     path('test/', mytest.get_random, name='test_view'),
     path('importexcel/', home.get_import),
     path('import/', home.import_data_from_excel, name='import_data_from_excel'),
     path('change',mytest.change_word, name='change_word'),
     path('convesation/', conversation.get_conversation),
     path('category/<str:category>/', cate.dictionary_by_category, name='dictionary_by_category'),
     path('category/',cate.get_category),
     path('', splash.get_splash)
]
