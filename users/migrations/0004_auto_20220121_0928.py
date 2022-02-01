# Generated by Django 3.2 on 2022-01-21 05:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_cv_doc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsibility',
            fields=[
                ('responsibility', models.CharField(blank=True, max_length=50, null=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='workexpirnce',
            name='responsibility',
            field=models.ManyToManyField(blank=True, null=True, to='users.Responsibility'),
        ),
    ]