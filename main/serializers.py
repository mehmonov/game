from rest_framework import serializers
from .models import Room, Question, Option
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'max_member', 'followers')

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'text', 'is_correct')

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('id', 'room', 'text', 'image', 'options')