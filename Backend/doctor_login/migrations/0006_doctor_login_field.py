# Generated by Django 2.0 on 2020-06-16 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_login', '0005_auto_20200616_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_login',
            name='field',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
