# Generated by Django 3.1.5 on 2021-02-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210203_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
