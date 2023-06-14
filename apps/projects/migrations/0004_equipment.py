# Generated by Django 4.1.5 on 2023-06-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_uss'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование')),
                ('characteristic', models.TextField(verbose_name='Характеристика')),
                ('owner', models.CharField(max_length=256, verbose_name='Владелец')),
                ('contact', models.CharField(max_length=256, verbose_name='Контакт')),
                ('image', models.ImageField(blank=True, null=True, upload_to='equipment_photos/', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
