# Generated by Django 2.0 on 2020-06-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_appointment',
            name='fees',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
