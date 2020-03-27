# Generated by Django 3.0.3 on 2020-03-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mk_rc', '0004_auto_20200312_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vsd1c',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vsdmerc',
            name='name_1c',
            field=models.CharField(blank=True, max_length=128, verbose_name='Наименование 1С'),
        ),
        migrations.AlterField(
            model_name='vsdmerc',
            name='name_merc',
            field=models.CharField(blank=True, max_length=128, verbose_name='Наименование Меркурий'),
        ),
        migrations.AlterField(
            model_name='vsdmerc',
            name='w_in_pack',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, verbose_name='Вес упаковки'),
        ),
    ]
