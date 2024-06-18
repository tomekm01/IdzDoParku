# Generated by Django 5.0.6 on 2024-06-18 07:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_comment_comment_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPOI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completion_date', models.DateTimeField(auto_now_add=True)),
                ('poi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.poi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
