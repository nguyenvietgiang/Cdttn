from django.shortcuts import render
from home.models import DictionaryEntry
from random import choice
from .forms import EnglishInputForm  

from home.models import DictionaryEntry  


dictionary_entries = {entry.id: entry for entry in DictionaryEntry.objects.all()}
def test_view(request):
    #random_entry = choice(DictionaryEntry.objects.all())
  
   # Chọn một ID ngẫu nhiên từ hash table
    random_entry_id = choice(list(dictionary_entries.keys()))

    random_entry = dictionary_entries[random_entry_id]
   
    if request.method == 'POST':
        form = EnglishInputForm(request.POST)
        if form.is_valid():
         
            english_input = form.cleaned_data['english_input']
            
           
            if english_input == random_entry.english:
                feedback = 'Correct!'
            else:
                feedback = 'Incorrect! Please try again.'
            
           
            random_entry = choice(DictionaryEntry.objects.all())
    else:

        form = EnglishInputForm()
        feedback = None
    
    context = {
        'random_entry': random_entry,
        'form': form,
        'feedback': feedback,
    }
    return render(request, 'test.html', context)

