from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    isComplete = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
