# Generated by Django 3.2.5 on 2021-07-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrmaker', '0003_auto_20210727_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='maker',
            name='username',
            field=models.CharField(default='', max_length=200),
        ),
    ]
