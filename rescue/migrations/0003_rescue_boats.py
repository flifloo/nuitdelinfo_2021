# Generated by Django 3.2.9 on 2021-12-03 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0001_initial'),
        ('rescue', '0002_auto_20211202_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='rescue',
            name='boats',
            field=models.ManyToManyField(to='boat.Boat'),
        ),
    ]
