from django.db import models
from users.models import UserProfile

class Room(models.Model):
    name = models.CharField(max_length=100)
    max_member = models.IntegerField(default=20)
    followers = models.ManyToManyField(UserProfile, related_name='rooms', blank=True, null=True)
    creator = models.ForeignKey(UserProfile, related_name='room', on_delete=models.CASCADE)

class Question(models.Model):
    room = models.ForeignKey(Room, related_name='questions', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/question', default=None)
    text = models.TextField()
    
class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)