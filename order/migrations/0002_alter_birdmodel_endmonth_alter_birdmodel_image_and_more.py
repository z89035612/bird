# Generated by Django 4.1.2 on 2023-07-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birdmodel',
            name='endMonth',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='birdmodel',
            name='image',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='birdmodel',
            name='level',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='birdmodel',
            name='season',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='birdmodel',
            name='startMonth',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
