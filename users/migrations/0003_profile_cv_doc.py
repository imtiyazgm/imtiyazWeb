# Generated by Django 3.2 on 2022-01-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_workexpirnce'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cv_doc',
            field=models.FileField(blank=True, default='CV/ImtiyazCV.docx', null=True, upload_to='CV/'),
        ),
    ]
