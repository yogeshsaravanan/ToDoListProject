# Generated by Django 5.0.2 on 2024-02-17 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoListApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['id']},
        ),
    ]
