# messages/views.py
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

def message_board(request):
    messages = Message.objects.all()
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_board')

    return render(request, 'messages1/message_board.html', {'messages': messages, 'form': form})
