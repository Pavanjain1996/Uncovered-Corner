# Generated by Django 2.1.5 on 2019-03-16 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='p10name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='country',
            name='p1name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='country',
            name='p2name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='country',
            name='p3name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='country',
            name='p4name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='country',
            name='p5name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='country',
            name='p6name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='country',
            name='p7name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='country',
            name='p8name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='country',
            name='p9name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='country',
            name='capital',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]