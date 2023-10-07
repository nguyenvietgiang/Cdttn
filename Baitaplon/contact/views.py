from django.shortcuts import render

def get_contact(request):
    return render(request,'contact.html') 
