# Generated by Django 4.1.1 on 2022-10-14 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='today_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Take_name', models.CharField(max_length=250)),
                ('priority', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
