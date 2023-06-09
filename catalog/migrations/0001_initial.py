# Generated by Django 4.2.1 on 2023-05-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='preview')),
                ('category', models.CharField(max_length=100, verbose_name='Категория')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('data_creating', models.DateTimeField(verbose_name='Дата создания')),
                ('data_updating', models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего изменения')),
            ],
        ),
    ]
