# Generated by Django 3.2.5 on 2021-07-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrmaker', '0006_auto_20210727_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='title',
            field=models.CharField(default='N/A', max_length=200),
        ),
    ]