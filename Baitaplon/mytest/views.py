from django.shortcuts import render
from home.models import DictionaryEntry
from random import choice
from .forms import EnglishInputForm  

from home.models import DictionaryEntry  

def test_view(request):
  
    random_entry = choice(DictionaryEntry.objects.all())
    
   
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

