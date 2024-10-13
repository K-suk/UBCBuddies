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
    
class MaleGymQueue(models.Model):
    users = models.ManyToManyField(User, related_name='male_gym_queues', blank=True)

    def __str__(self):
        return f"Male Queue: {self.users.count()} users"

class FemaleGymQueue(models.Model):
    users = models.ManyToManyField(User, related_name='female_gym_queues', blank=True)

    def __str__(self):
        return f"Female Queue: {self.users.count()} users"

class MaleDrinkQueue(models.Model):
    users = models.ManyToManyField(User, related_name='male_drink_queues', blank=True)

    def __str__(self):
        return f"Male Queue: {self.users.count()} users"

class FemaleDrinkQueue(models.Model):
    users = models.ManyToManyField(User, related_name='female_drink_queues', blank=True)

    def __str__(self):
        return f"Female Queue: {self.users.count()} users"
    
class MalePartyQueue(models.Model):
    users = models.ManyToManyField(User, related_name='male_party_queues', blank=True)

    def __str__(self):
        return f"Male Queue: {self.users.count()} users"

class FemalePartyQueue(models.Model):
    users = models.ManyToManyField(User, related_name='female_party_queues', blank=True)

    def __str__(self):
        return f"Female Queue: {self.users.count()} users"
    
class MaleDatingQueue(models.Model):
    users = models.ManyToManyField(User, related_name='male_dating_queues', blank=True)

    def __str__(self):
        return f"Male Queue: {self.users.count()} users"

class FemaleDatingQueue(models.Model):
    users = models.ManyToManyField(User, related_name='female_dating_queues', blank=True)

    def __str__(self):
        return f"Female Queue: {self.users.count()} users"