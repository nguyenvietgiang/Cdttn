from django.shortcuts import render
# sử dụng để thực hiện các truy vấn and, or
from django.db.models import Q
from .models import DictionaryEntry, Conversation
from django.http import JsonResponse
# Khởi tạo một dict để lưu trữ kết quả cache
search_cache = {}

def search(request):
    search_query = request.GET.get('search_query')

    if search_query:
        # Kiểm tra xem có kết quả tìm kiếm trong cache hay không
        results = search_cache.get(search_query)

        if results is None:
            dictionary_results = DictionaryEntry.objects.filter(english__icontains=search_query)
            conversation_results = Conversation.objects.filter(enconversation__icontains=search_query)

            # Tạo danh sách kết quả
            results = []
            for dictionary_entry in dictionary_results:
                results.append(('dictionary', dictionary_entry))
            for conversation_entry in conversation_results:
                results.append(('conversation', conversation_entry))
            # Lưu kết quả vào cache
            search_cache[search_query] = results
            # Ghi thông tin vào log trong terminal
        print("Results:", results)

        return render(request, 'search_results.html', {'results': results, 'search_query': search_query})
    else:
        return render(request, 'home.html')

def search_suggestions(request):
    search_query = request.GET.get('search_query', '')
    suggestions = DictionaryEntry.objects.filter(english__icontains=search_query)[:5]
    suggestion_list = [entry.english for entry in suggestions]
    return JsonResponse(suggestion_list, safe=False)
    
def get_home(request):
    return render(request,'home.html') 
