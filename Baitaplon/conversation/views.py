from django.shortcuts import render
from googletrans import Translator

def get_conversation(request):
    if request.method == 'POST':
        english_text = request.POST.get('english_text', '') 
        translator = Translator()
        vietnamese_text = translator.translate(english_text, src='en', dest='vi').text
        return render(request, 'conversation.html', {'vietnamese_text': vietnamese_text, 'english_text': english_text})
    return render(request, 'conversation.html')
