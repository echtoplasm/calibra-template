from rest_framework import serializers
from messenger.models import Conversation, Message
from tasks.models import Task
from notifications.models import Notification
from conference.models import VideoConference
from fileshare.models import File, FileAccess


# ---- Messenger Serializers here ---- #
class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'



# ---- Task Serializers here ---- #
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


# ---- Notification Serializers here ---- #
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


# ---- Video Conference Serializer ----#
class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoConference
        fields = '__all__'



# ---- Fileshare Serializers ---- #
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class FileAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileAccess
        fields = '__all__'
