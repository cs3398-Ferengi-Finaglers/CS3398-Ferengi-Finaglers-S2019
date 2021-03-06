# Generated by Django 2.1.7 on 2019-03-04 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0010_auto_20190303_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responseinstances',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Answers', verbose_name='The answer given'),
        ),
        migrations.AlterField(
            model_name='responseinstances',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User who answered the question'),
        ),
    ]
