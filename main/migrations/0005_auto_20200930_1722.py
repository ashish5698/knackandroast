# Generated by Django 3.0.6 on 2020-09-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200930_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cake',
            name='cake_id',
            field=models.IntegerField(unique=True),
        ),
    ]
