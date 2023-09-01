from django.contrib import admin
from .models import DictionaryEntry

@admin.register(DictionaryEntry)
class DictionaryEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'english', 'vietnam', 'category', 'pronounce')
    search_fields = ('english', 'vietnam', 'category', 'pronounce')

