# Generated by Django 4.2.7 on 2024-08-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kicksapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShirtCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
