# Generated by Django 3.2 on 2022-01-21 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220121_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexpirnce',
            name='responsibility',
            field=models.ManyToManyField(blank=True, to='users.Responsibility'),
        ),
    ]
