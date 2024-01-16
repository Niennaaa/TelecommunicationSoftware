# messages/views.py
from django.shortcuts import render
from .models import Message

def message_board(request):
    messages = Message.objects.all()
    return render(request, 'messages1/message_board.html', {'messages': messages})
