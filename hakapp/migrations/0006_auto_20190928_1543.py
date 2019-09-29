# Generated by Django 2.2.5 on 2019-09-28 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hakapp', '0005_auto_20190928_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='Avatar',
            field=models.ImageField(default='None', upload_to='', verbose_name='Фотография работника'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='Position',
            field=models.CharField(default=None, max_length=255, verbose_name='Должность'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='Status',
            field=models.IntegerField(default=0, verbose_name='Статус работника'),
            preserve_default=False,
        ),
    ]