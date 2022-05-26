# Generated by Django 4.0.4 on 2022-05-26 09:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructor',
            name='x',
            field=models.FloatField(blank=True, help_text='xx.xxxxxx', validators=[django.core.validators.MinValueValidator(8)], verbose_name='X'),
        ),
        migrations.AlterField(
            model_name='constructor',
            name='y',
            field=models.FloatField(blank=True, help_text='xx.xxxxxx', validators=[django.core.validators.MinValueValidator(8)], verbose_name='Y'),
        ),
    ]