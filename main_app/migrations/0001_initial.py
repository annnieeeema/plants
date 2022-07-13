# Generated by Django 4.0.6 on 2022-07-13 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=50)),
                ('difficultyLevel', models.IntegerField()),
                ('waterFrequency', models.CharField(max_length=100)),
            ],
        ),
    ]
