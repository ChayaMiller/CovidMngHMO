# Generated by Django 4.0.4 on 2022-10-20 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_patient_mobile_alter_patient_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccine',
            name='patient',
        ),
        migrations.AddField(
            model_name='vaccine',
            name='patient_id',
            field=models.CharField(default=0, max_length=10),
        ),
    ]