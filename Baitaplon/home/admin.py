from django.contrib import admin
from .models import DictionaryEntry, Conversation

@admin.register(DictionaryEntry)
class DictionaryEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'english', 'vietnam', 'category', 'pronounce','image')
    search_fields = ('english', 'vietnam', 'category', 'pronounce')
 # Thêm chức năng sửa và xóa
    list_display_links = ('id', 'english')
    list_editable = ('vietnam', 'image', 'pronounce')
    list_per_page = 25  # Số lượng bản ghi hiển thị trên mỗi trang

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'vnconversation', 'enconversation')
    search_fields = ('vnconversation', 'enconversation')
   