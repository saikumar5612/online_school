# Generated by Django 4.2.16 on 2024-11-27 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
    ]
