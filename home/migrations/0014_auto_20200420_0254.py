# Generated by Django 3.0.3 on 2020-04-19 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200420_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_foodlist',
            name='user_carbs',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_foodlist',
            name='user_fat',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_foodlist',
            name='user_protein',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_foodlist',
            name='user_calories',
            field=models.BigIntegerField(default=0),
        ),
    ]
