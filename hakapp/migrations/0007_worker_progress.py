# Generated by Django 2.2.5 on 2019-09-28 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hakapp', '0006_auto_20190928_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='Progress',
            field=models.SmallIntegerField(default=0, verbose_name='Прогресс обучения'),
        ),
    ]
