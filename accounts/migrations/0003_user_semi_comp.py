# Generated by Django 4.2.15 on 2024-09-07 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_user_review_count_user_review_sum"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="semi_comp",
            field=models.BooleanField(default=False),
        ),
    ]