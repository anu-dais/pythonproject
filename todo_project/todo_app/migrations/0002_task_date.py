# Generated by Django 3.2.5 on 2021-07-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-08-22'),
            preserve_default=False,
        ),
    ]
