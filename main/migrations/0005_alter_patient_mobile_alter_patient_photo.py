# Generated by Django 4.0.4 on 2022-10-20 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_patient_phone_alter_patient_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
