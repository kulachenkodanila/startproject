# Generated by Django 4.0.5 on 2022-07-04 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('category', models.CharField(choices=[('other', 'Разное'), ('Milk', 'Молоко'), ('Juce', 'Сок'), ('Bread', 'Хлеб')], default='other', max_length=30, verbose_name='Категория')),
                ('remains', models.IntegerField(verbose_name='Остаток')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'products',
            },
        ),
    ]