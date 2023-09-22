from django.shortcuts import render

def get_splash(request):
    return render(request,'splash.html') 