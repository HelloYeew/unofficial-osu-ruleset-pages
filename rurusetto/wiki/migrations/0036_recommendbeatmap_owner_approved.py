# Generated by Django 3.2.6 on 2021-09-03 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0035_ruleset_recommend_beatmap_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendbeatmap',
            name='owner_approved',
            field=models.BooleanField(default=False),
        ),
    ]