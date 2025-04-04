# Generated by Django 4.2.7 on 2024-01-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starmen', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='starmen',
            options={'ordering': ['-time_create']},
        ),
        migrations.AddField(
            model_name='starmen',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AddIndex(
            model_name='starmen',
            index=models.Index(fields=['-time_create'], name='starmen_sta_time_cr_bd8efc_idx'),
        ),
    ]
