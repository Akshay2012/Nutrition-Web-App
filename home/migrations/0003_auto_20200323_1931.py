# Generated by Django 3.0.3 on 2020-03-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_nutrition_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='calories',
            field=models.IntegerField(default=222),
        ),
        migrations.AddField(
            model_name='food',
            name='carbs',
            field=models.IntegerField(default=222),
        ),
        migrations.AddField(
            model_name='food',
            name='fat',
            field=models.IntegerField(default=222),
        ),
        migrations.AddField(
            model_name='food',
            name='protein',
            field=models.IntegerField(default=222),
        ),
        migrations.DeleteModel(
            name='nutrition_values',
        ),
    ]
