# Generated by Django 4.2.7 on 2024-09-12 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kicksapp', '0016_shoes_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='color',
            field=models.CharField(default='', max_length=20),
        ),
    ]
