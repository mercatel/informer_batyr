# Generated by Django 3.0 on 2019-12-15 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabinv',
            name='time_end',
            field=models.CharField(blank=True, default=0, max_length=50, verbose_name='Время окончания инвент'),
        ),
    ]
