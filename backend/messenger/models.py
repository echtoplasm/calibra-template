from django.db import models

# Create your models here.

class Conversation(models.Model):
    chat_name = models.CharField(max_length=255)
    participants = models.ManyToManyField('accounts.CustomUser')

    def __str__(self):
        return self.chat_name
    
class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content
