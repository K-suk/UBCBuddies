from datetime import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from match.models import DailyUserCount
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def add_user_to_daily_count(sender, instance, created, **kwargs):
    if created:
        DailyUserCount.add_new_user(instance)
