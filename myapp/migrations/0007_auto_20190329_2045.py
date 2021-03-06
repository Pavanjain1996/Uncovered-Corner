# Generated by Django 2.1.5 on 2019-03-29 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='h1address',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='country',
            name='h1image',
            field=models.CharField(default='h1.jpg', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='h1name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='h1rating',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='h2address',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='country',
            name='h2image',
            field=models.CharField(default='h2.jpg', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='h2name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='h2rating',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='h3address',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='country',
            name='h3image',
            field=models.CharField(default='h3.jpg', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='h3name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='h3rating',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='h4address',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='country',
            name='h4image',
            field=models.CharField(default='h4.jpg', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='h4name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='h4rating',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='h5address',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='country',
            name='h5image',
            field=models.CharField(default='h5.jpg', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='h5name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='h5rating',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='r1image',
            field=models.CharField(default='r1.jpg', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='r2image',
            field=models.CharField(default='r2.jpg', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='r3image',
            field=models.CharField(default='r3.jpg', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='r4image',
            field=models.CharField(default='r4.jpg', max_length=30),
        ),
        migrations.AddField(
            model_name='country',
            name='r5image',
            field=models.CharField(default='r5.jpg', max_length=30),
        ),
    ]
