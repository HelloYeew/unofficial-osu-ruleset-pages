# Generated by Django 4.1.1 on 2022-09-05 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0058_recommendbeatmap_approved_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruleset',
            name='github_localisation_filename',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='ruleset',
            name='localisation_support',
            field=models.BooleanField(default=False),
        ),
    ]