# Generated by Django 2.0.1 on 2018-01-29 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(to='news.Tag', verbose_name='Теги'),
        ),
    ]
