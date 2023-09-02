from django.shortcuts import render
# sử dụng để thực hiện các truy vấn and, or
from django.db.models import Q
from .models import DictionaryEntry, Conversation

def search(request):
    search_query = request.GET.get('search_query')

    if search_query:
        dictionary_results = DictionaryEntry.objects.filter(english__icontains=search_query)
        conversation_results = Conversation.objects.filter(enconversation__icontains=search_query)

        # Tạo danh sách kết quả kết hợp từ cả hai models
        results = []

        for dictionary_entry in dictionary_results:
            results.append(('dictionary', dictionary_entry))

        for conversation_entry in conversation_results:
            results.append(('conversation', conversation_entry))

        return render(request, 'search_results.html', {'results': results, 'search_query': search_query})
    else:
        return render(request, 'home.html')

    
def get_home(request):
    return render(request,'home.html') 
