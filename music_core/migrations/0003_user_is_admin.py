# Generated by Django 2.1.5 on 2020-10-07 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music_core", "0002_auto_20201007_1028"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
    ]
