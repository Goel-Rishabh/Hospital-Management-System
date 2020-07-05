# Generated by Django 2.0 on 2020-06-16 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_login', '0003_doctor_login_mobile_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor_degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=20)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_login.doctor_degree')),
            ],
        ),
    ]