# Generated by Django 3.2.7 on 2021-09-08 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_auto_20210909_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='support_message',
            field=models.TextField(blank=True, default=''),
        ),
    ]