# Generated by Django 3.0.3 on 2020-04-13 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200412_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='calories',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='activity_level',
            field=models.CharField(choices=[('not_active', 'Not active'), ('light', 'Lightly Active'), ('active', 'Active'), ('very', 'Very Active')], default='active', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='goal',
            field=models.CharField(choices=[('Gain', 'Gain Weight'), ('maintain', 'Maintain Weight'), ('fat_Loss', 'Fat loss')], default='maintain', max_length=20),
        ),
    ]
