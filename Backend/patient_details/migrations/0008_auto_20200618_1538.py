# Generated by Django 2.0 on 2020-06-18 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_details', '0007_auto_20200618_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_appointment',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]