# Generated by Django 4.2.7 on 2024-02-12 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starmen', '0011_uploadfiles_alter_starmen_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='starmen',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
