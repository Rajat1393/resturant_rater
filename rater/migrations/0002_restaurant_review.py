# Generated by Django 2.1.5 on 2022-03-14 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('phoneno', models.CharField(max_length=20)),
                ('googleplaceid', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
