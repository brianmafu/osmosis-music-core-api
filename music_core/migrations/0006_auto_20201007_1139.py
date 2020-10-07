# Generated by Django 2.1.5 on 2020-10-07 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_core', '0005_auto_20201007_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='status',
            field=models.IntegerField(choices=[(0, 'ENABLE'), (1, 'DISABLE')], default=0),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_status',
            field=models.IntegerField(choices=[(0, 'ENABLE'), (1, 'DISABLE')], default=0),
        ),
        migrations.AlterField(
            model_name='bannerslider',
            name='banner_slider_status',
            field=models.IntegerField(choices=[(0, 'ENABLE'), (1, 'DISABLE')], default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_status',
            field=models.IntegerField(choices=[(0, 'ENABLE'), (1, 'DISABLE')], default=0),
        ),
        migrations.AlterField(
            model_name='homecomponents',
            name='home_components_status',
            field=models.IntegerField(choices=[(0, 'ENABLE'), (1, 'DISABLE')], default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_status',
            field=models.IntegerField(choices=[(0, 'ENABLE'), (1, 'DISABLE')], default=0),
        ),
        migrations.AlterField(
            model_name='music',
            name='music_status',
            field=models.IntegerField(choices=[(0, 'ENABLE'), (1, 'DISABLE')], default=0),
        ),
        migrations.AlterField(
            model_name='packagesettings',
            name='package_status',
            field=models.IntegerField(choices=[(0, 'ENABLE'), (1, 'DISABLE')], default=0),
        ),
    ]