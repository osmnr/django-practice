# Generated by Django 5.0.7 on 2024-08-01 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0003_userstodolist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstodolist',
            name='sessionKey',
            field=models.TextField(null=True),
        ),
    ]
