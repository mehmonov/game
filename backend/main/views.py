from rest_framework import viewsets
from rest_framework.response import Response
from .models import Room, Option, Question
from .serializers import RoomSerializer, OptionSerializer, QuestionSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        options_data = request.data.pop('options')
        question = Question.objects.create(**request.data)
        for option_data in options_data:
            Option.objects.create(question=question, **option_data)
        return Response(self.get_serializer(question).data)
