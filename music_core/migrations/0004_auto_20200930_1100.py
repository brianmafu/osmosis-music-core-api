# Generated by Django 2.1.5 on 2020-09-30 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_core', '0003_auto_20200930_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_package_expiry_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_package_paid_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
