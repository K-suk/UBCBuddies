from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MaleQueue(models.Model):
    users = models.ManyToManyField(User, related_name='male_queues', blank=True)

    def __str__(self):
        return f"Male Queue: {self.users.count()} users"

class FemaleQueue(models.Model):
    users = models.ManyToManyField(User, related_name='female_queues', blank=True)

    def __str__(self):
        return f"Female Queue: {self.users.count()} users"