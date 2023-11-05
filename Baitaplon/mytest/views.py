import random
from django import forms
from django.shortcuts import render

class TranslationForm(forms.Form):
    english_word = forms.CharField(label='Từ tiếng Anh', max_length=100)

class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

def get_random(request):
    hash_table = HashTable()
    hash_table.insert("hello", "xin chào")
    hash_table.insert("thank you", "cảm ơn")
    hash_table.insert("goodbye", "tạm biệt")
    

    english_word, correct_translation = next(iter(hash_table.table.items()))

    feedback = None

    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            user_translation = form.cleaned_data['english_word']
            if user_translation.lower() == correct_translation.lower():
                feedback = "Đúng!"
                try:
                    english_word, correct_translation = next(iter(hash_table.table.items()))
                except StopIteration:
                    pass
            else:
                feedback = "Sai!"
    else:
        form = TranslationForm()

    return render(request, 'test.html', {'form': form, 'random_entry': {'vietnam': correct_translation}, 'english_word': english_word, 'feedback': feedback})

def change_word(request):
    hash_table = HashTable()
    hash_table.insert("hello", "xin chào")
    hash_table.insert("thank you", "cảm ơn")
    hash_table.insert("goodbye", "tạm biệt")
    
    english_word, correct_translation = random.choice(list(hash_table.table.items()))
    
    form = TranslationForm()
    feedback = None

    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            user_translation = form.cleaned_data['english_word']
            if user_translation.lower() == correct_translation.lower():
                feedback = "Đúng!"
                try:
                    english_word, correct_translation = next(iter(hash_table.table.items()))
                except StopIteration:
                    pass
            else:
                feedback = "Sai!"
    else:
        form = TranslationForm()

    return render(request, 'test.html', {'form': form, 'random_entry': {'vietnam': correct_translation}, 'english_word': english_word, 'feedback': feedback})





