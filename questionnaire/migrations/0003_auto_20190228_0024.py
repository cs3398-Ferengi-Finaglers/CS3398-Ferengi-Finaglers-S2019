# Generated by Django 2.1.7 on 2019-02-28 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_auto_20190227_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=500)),
                ('KNNvalue', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.RemoveField(
            model_name='questions',
            name='answers',
        ),
        migrations.AddField(
            model_name='answers',
            name='belongsToWhichQuestion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Questions'),
        ),
    ]
