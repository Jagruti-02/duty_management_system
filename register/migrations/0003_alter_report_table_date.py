# Generated by Django 4.0.4 on 2022-07-06 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_report_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_table',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
