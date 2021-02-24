# Generated by Django 2.1.5 on 2019-05-06 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20190329_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('about', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Wonder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('about', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=40)),
            ],
        ),
    ]