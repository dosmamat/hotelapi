# Generated by Django 4.0.4 on 2022-04-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
