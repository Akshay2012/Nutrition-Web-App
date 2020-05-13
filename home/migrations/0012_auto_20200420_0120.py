# Generated by Django 3.0.3 on 2020-04-19 19:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200416_0115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='Protein',
        ),
        migrations.AddField(
            model_name='food',
            name='cholestrol',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='dietlabel',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=[], size=None),
        ),
        migrations.AddField(
            model_name='food',
            name='fat',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='fiber',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='food_url',
            field=models.URLField(default='www.google.com', max_length=400),
        ),
        migrations.AddField(
            model_name='food',
            name='healthlabel',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=[], size=None),
        ),
        migrations.AddField(
            model_name='food',
            name='iron',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='magnesium',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='monounsaturated',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='protein',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='saturated',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='servings',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='steps',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=[], size=None),
        ),
        migrations.AddField(
            model_name='food',
            name='sugar',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='trans',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='vita',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='vitc',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='vite',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='vitk',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='zinc',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_foodlist',
            name='user_calories',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='carbs',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='food_name',
            field=models.TextField(max_length=200),
        ),
    ]
