# Generated by Django 3.1.3 on 2020-12-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweetapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]
