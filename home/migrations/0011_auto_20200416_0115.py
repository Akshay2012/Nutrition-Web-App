# Generated by Django 3.0.3 on 2020-04-15 19:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_user_foodlist_userpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]