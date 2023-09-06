from django import forms

class EnglishInputForm(forms.Form):
    english_input = forms.CharField(max_length=100, label='Enter the English word')
