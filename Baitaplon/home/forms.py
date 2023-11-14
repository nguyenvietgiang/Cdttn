from django import forms

class EnglishToVietnameseForm(forms.Form):
    english_word = forms.CharField(label='English Word', max_length=100)
