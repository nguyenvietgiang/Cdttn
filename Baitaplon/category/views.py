from django.shortcuts import render
from home.models import DictionaryEntry 

def get_category(request):
    category_mapping = {
        "Tính từ": "http://127.0.0.1:8000/category/Tinhtu/",
        "Danh từ": "http://127.0.0.1:8000/category/Danhtu/",
        "Động từ": "http://127.0.0.1:8000/category/Dongtu/",
    }
    return render(request, 'category.html', {'category_mapping': category_mapping})

def dictionary_by_category(request, category):
    entries = DictionaryEntry.objects.filter(category=category)
    return render(request, 'dictionary_by_category.html', {'entries': entries, 'category': category})


