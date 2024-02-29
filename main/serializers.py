from rest_framework import serializers
from .models import Room, Question, Option
from users.serializers import UserProfileSerializer

class RoomSerializer(serializers.ModelSerializer):
    followers = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ('name', 'max_member', 'followers', 'creator')

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ( 'text', 'is_correct')

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ( 'room', 'image', 'text', 'options')
