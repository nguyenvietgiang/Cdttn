from django.contrib import admin
from .models import Contact

# Đăng ký model Contact với admin site
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')  
    search_fields = ('name', 'email', 'subject')  

