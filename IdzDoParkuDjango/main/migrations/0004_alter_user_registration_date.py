# Generated by Django 5.0.6 on 2024-06-04 19:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_user_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateField(default=datetime.date(2024, 6, 4)),
        ),
    ]
