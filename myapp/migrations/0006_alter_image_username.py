# Generated by Django 5.0.1 on 2024-04-21 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_image_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='username',
            field=models.CharField(default='guest', max_length=30),
        ),
    ]
