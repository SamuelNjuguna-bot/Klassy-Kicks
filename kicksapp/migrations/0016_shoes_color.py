# Generated by Django 4.2.7 on 2024-09-12 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kicksapp', '0015_jacket_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='color',
            field=models.CharField(default='', max_length=20),
        ),
    ]
