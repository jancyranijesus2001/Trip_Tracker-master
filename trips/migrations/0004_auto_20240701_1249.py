# Generated by Django 3.2 on 2024-07-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20240701_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
