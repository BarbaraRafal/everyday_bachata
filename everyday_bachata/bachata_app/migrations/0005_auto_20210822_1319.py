# Generated by Django 3.2.6 on 2021-08-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bachata_app', '0004_auto_20210822_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
