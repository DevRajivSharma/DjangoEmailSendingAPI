from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
# Create your views here.
@api_view(['POST'])
def send_email(request):
        subject = request.data.get('subject', 'No Subject')  
        message = request.data.get('message', '')  
        recipient_list = request.data.get('tosend', [])  
        print(recipient_list)
        if  recipient_list == ['']:
            messages.warning(request, 'Please enter a valid email address.')
            # raise ValueError("Recipient list cannot be empty.")
        try:
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
            messages.success(request, 'Email sent successfully!')
        except:
            messages.warning(request, 'Please enter a valid email address.')
        return Response('Email sent successfully!')


def home(request):
    context = {}
    return render(request,'main.html',context=context)