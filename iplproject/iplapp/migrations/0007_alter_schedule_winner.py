# Generated by Django 4.2.7 on 2023-12-14 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplapp', '0006_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='winner',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
