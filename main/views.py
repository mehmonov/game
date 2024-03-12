# views.py

from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import Option, Room, Question
from .serializers import RoomSerializer, QuestionSerializer, OptionSerializer
from django.core.exceptions import PermissionDenied
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(creator=self.request.user)
        else:
            raise PermissionDenied('Only authenticated users can create rooms.')

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        room_pk = self.kwargs['room_pk']
        return Question.objects.filter(room_pk=room_pk)

    def perform_create(self, serializer):
        serializer.save(room_id=self.kwargs['room_pk'])

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        question_pk = self.kwargs['question_pk']
        return Option.objects.filter(question_pk=question_pk)