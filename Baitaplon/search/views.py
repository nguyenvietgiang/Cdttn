from django.shortcuts import render
from .data import hash_table

def get_product(request):
    english_word = None
    word_entry = None

    if request.method == 'POST':
        english_word = request.POST.get('english_word')
        if english_word:
            word_entry = hash_table.search(english_word)

    return render(request, 'search.html', {'english_word': english_word, 'word_entry': word_entry})



