# Generated by Django 2.1.5 on 2020-10-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music_core", "0003_user_is_admin"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]
