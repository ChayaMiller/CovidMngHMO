# Generated by Django 4.0.4 on 2022-10-20 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_patient_mobile_alter_patient_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(blank=True, default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(blank=True, default=0, max_length=10),
        ),
    ]
