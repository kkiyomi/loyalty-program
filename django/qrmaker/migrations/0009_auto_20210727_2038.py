# Generated by Django 3.2.5 on 2021-07-27 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qrmaker', '0008_auto_20210727_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='uid',
        ),
        migrations.AlterField(
            model_name='promo',
            name='maker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='promos', to='qrmaker.maker'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='state',
            field=models.CharField(choices=[('Published', 'Published'), ('Pending', 'Pending'), ('Archived', 'Archived'), ('Completed', 'Completed'), ('Deleted', 'Deleted')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='promo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='qrmaker.promo'),
        ),
    ]
