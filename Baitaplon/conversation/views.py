from django.shortcuts import render

def get_conversation(request):
    return render(request,'conversation.html') 