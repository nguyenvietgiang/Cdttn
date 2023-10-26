from django.shortcuts import render
from .models import Contact
from django.http import HttpResponseRedirect

def get_contact(request):
    success_message = None
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Lưu dữ liệu vào CSDL
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        success_message = 'Phản hồi của bạn đã được ghi nhận, cảm ơn bạn!'
        
    return render(request, 'contact.html', {'success_message': success_message})


