# Generated by Django 5.0.6 on 2024-06-18 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_user_completed_pois'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='completed_pois',
        ),
        migrations.DeleteModel(
            name='UserPOI',
        ),
    ]
