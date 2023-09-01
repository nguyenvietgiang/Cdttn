from django.shortcuts import render
from .models import DictionaryEntry

def search(request):
    search_query = request.GET.get('search_query')

    if search_query:
        results = DictionaryEntry.objects.filter(english__icontains=search_query)
        return render(request, 'search_results.html', {'results': results, 'search_query': search_query})
    else:
        return render(request, 'home.html')
    
def get_home(request):
    return render(request,'home.html') 
