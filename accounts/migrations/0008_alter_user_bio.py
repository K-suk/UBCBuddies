# Generated by Django 4.2.15 on 2024-10-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_alter_user_matching_history"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="bio",
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
    ]
