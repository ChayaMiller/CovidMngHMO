# Generated by Django 4.0.4 on 2022-10-18 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Pid', models.CharField(editable=False, max_length=9, unique=True)),
                ('address', models.CharField(max_length=300)),
                ('birthday', models.DateField()),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('photo', models.ImageField(upload_to='')),
                ('sickDate', models.DateField(blank=True, null=True)),
                ('recoveryDate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacDate', models.DateField(blank=True, null=True)),
                ('producer', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
            ],
        ),
    ]
