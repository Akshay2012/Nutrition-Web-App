# Generated by Django 3.0.3 on 2020-05-14 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20200513_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='target_muscle_id',
            field=models.IntegerField(default=-1),
        ),
    ]
