# Generated by Django 2.1.7 on 2019-04-06 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0002_connect_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connect',
            name='summary',
            field=models.TextField(),
        ),
    ]