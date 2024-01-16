from django.urls import path
from .views import message_board

urlpatterns = [
    path('message-board/', message_board, name='message_board'),
]
