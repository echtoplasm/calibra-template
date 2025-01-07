from django import forms
from .models import Conversation, Message

class ConversationAddForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ['participants', 'chat_name']

class ConversationChangeForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ['participants', 'chat_name']

class MessageAddForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['conversation', 'author', 'content']
    
class MessageChangeForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['conversation', 'author', 'content']
