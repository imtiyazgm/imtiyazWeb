# Generated by Django 3.2 on 2022-01-31 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_blgodetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blogImage',
            field=models.ImageField(blank=True, default='blog_images/default.jpeg', null=True, upload_to='blog_images/'),
        ),
    ]
