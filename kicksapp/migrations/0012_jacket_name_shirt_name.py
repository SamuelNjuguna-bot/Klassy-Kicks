# Generated by Django 4.2.7 on 2024-09-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kicksapp', '0011_cart_items_delete_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='jacket',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='shirt',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
