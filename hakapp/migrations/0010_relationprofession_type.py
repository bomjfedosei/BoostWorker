# Generated by Django 2.2.5 on 2019-09-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hakapp', '0009_remove_worker_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationprofession',
            name='Type',
            field=models.IntegerField(default=0, verbose_name='Тип тега'),
            preserve_default=False,
        ),
    ]