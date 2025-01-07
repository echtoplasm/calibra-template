from django.contrib import admin
from .models import Conversation, Message
from .forms import ConversationAddForm, ConversationChangeForm, MessageAddForm, MessageChangeForm

# Register your models here.

class ConversationAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_name']
    add_form = ConversationAddForm
    form = ConversationChangeForm
    model = Conversation

class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'conversation', 'author', 'content']
    add_form = MessageAddForm
    form = MessageChangeForm
    model = Message

admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Message, MessageAdmin)


