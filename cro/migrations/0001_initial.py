# Generated by Django 3.0 on 2019-12-09 00:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TabInv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default=uuid.uuid4, max_length=120, unique=True)),
                ('shop', models.CharField(max_length=120, verbose_name='Магазин')),
                ('sv_shop', models.CharField(max_length=100, verbose_name='СВ')),
                ('dm_shop', models.CharField(max_length=100, verbose_name='ДМ')),
                ('date_inv', models.CharField(max_length=120, verbose_name='Дата')),
                ('dm_shop_new', models.CharField(blank=True, default=None, max_length=120, verbose_name='ДМ принимающий')),
                ('res_main', models.DecimalField(decimal_places=2, default=None, max_digits=9, verbose_name='Осн.мето.хр')),
                ('res_defect', models.DecimalField(decimal_places=2, default=None, max_digits=9, verbose_name='Зона Брака')),
                ('res_6_line', models.DecimalField(decimal_places=2, default=None, max_digits=9, verbose_name='Бал. Лок.')),
                ('res_4_line', models.DecimalField(decimal_places=2, default=None, max_digits=9, verbose_name='4 Линия')),
                ('res_total', models.DecimalField(decimal_places=2, default=None, max_digits=9, verbose_name='Итого')),
                ('type_inv', models.CharField(default=None, max_length=120, verbose_name='тип инв')),
                ('format_shop', models.IntegerField(blank=True, default=None, verbose_name='Формат')),
                ('fact_format', models.IntegerField(default=None, verbose_name='Формат Факт')),
                ('coment', models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='Коментарии')),
                ('qky_mop', models.IntegerField(default=None, verbose_name='Кол.Моп')),
                ('fact_qky_mop', models.IntegerField(default=None, verbose_name='Факт.Кол.Моп')),
                ('qky_scro', models.IntegerField(default=None, verbose_name='Кол.СКРО')),
                ('diver_qky_mop', models.IntegerField(default=None, verbose_name='Отклонение')),
                ('vscro', models.CharField(max_length=100, verbose_name='ВСКРО')),
                ('t_o', models.DecimalField(decimal_places=2, default=None, max_digits=15, verbose_name='ТО')),
                ('percent_of_to', models.DecimalField(decimal_places=2, default=None, max_digits=9, verbose_name='% от ТО')),
                ('resort_001', models.DecimalField(decimal_places=2, default=None, max_digits=9, verbose_name='001 счет')),
                ('previous_date', models.CharField(default=None, max_length=40, verbose_name='Дата пред. инвент')),
                ('time_end', models.TimeField(auto_now_add=True, verbose_name='Время завершение инвент')),
            ],
            options={
                'verbose_name': 'Таблица инв. СКРО',
                'verbose_name_plural': 'Таблица инв. СКРО',
            },
        ),
        migrations.CreateModel(
            name='WorkerStatusCis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_status', models.CharField(max_length=48)),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='WorkerCis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='ФИО')),
                ('work_status', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='cro.WorkerStatusCis')),
            ],
            options={
                'verbose_name': 'Специалист КРО',
                'verbose_name_plural': 'Специалисты КРО',
            },
        ),
    ]
