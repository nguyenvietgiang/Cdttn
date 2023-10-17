from django.contrib import admin
from .models import DictionaryEntry, Conversation , Synonym, Antonym

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

@admin.register(Synonym)
class SynonymAdmin(admin.ModelAdmin):
    list_display = ('id', 'entry', 'synonym')
    search_fields = ('entry__english', 'synonym')
    list_display_links = ('id', 'synonym')

@admin.register(Antonym)
class AntonymAdmin(admin.ModelAdmin):
    list_display = ('id', 'entry', 'antonym')
    search_fields = ('entry__english', 'antonym')
    list_display_links = ('id', 'antonym')