# Generated by Django 2.1.5 on 2019-03-17 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_country_cardimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='p10image',
            field=models.CharField(default='p10.jpg', max_length=15),
        ),
        migrations.AlterField(
            model_name='country',
            name='p1image',
            field=models.CharField(default='p1.jpg', max_length=15),
        ),
        migrations.AlterField(
            model_name='country',
            name='p2image',
            field=models.CharField(default='p2.jpg', max_length=15),
        ),
        migrations.AlterField(
            model_name='country',
            name='p3image',
            field=models.CharField(default='p3.jpg', max_length=15),
        ),
        migrations.AlterField(
            model_name='country',
            name='p4image',
            field=models.CharField(default='p4.jpg', max_length=15),
        ),
        migrations.AlterField(
            model_name='country',
            name='p5image',
            field=models.CharField(default='p5.jpg', max_length=15),
        ),
        migrations.AlterField(
            model_name='country',
            name='p6image',
            field=models.CharField(default='p6.jpg', max_length=15),
        ),
        migrations.AlterField(
            model_name='country',
            name='p7image',
            field=models.CharField(default='p7.jpg', max_length=15),
        ),
        migrations.AlterField(
            model_name='country',
            name='p8image',
            field=models.CharField(default='p8.jpg', max_length=15),
        ),
        migrations.AlterField(
            model_name='country',
            name='p9image',
            field=models.CharField(default='p9.jpg', max_length=15),
        ),
    ]