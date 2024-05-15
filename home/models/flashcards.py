from django.db import models
from home.models.user import User


class FlashcardSet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_public = models.BooleanField(default=False)


class Flashcard(models.Model):
    set = models.ForeignKey(FlashcardSet, on_delete=models.CASCADE)
    front = models.TextField()
    back = models.TextField()