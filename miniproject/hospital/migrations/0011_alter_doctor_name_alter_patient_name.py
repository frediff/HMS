# Generated by Django 4.1.7 on 2023-03-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_alter_doctor_name_alter_patient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Name',
            field=models.CharField(default='Willie Barrett', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Name',
            field=models.CharField(default='Joseph Bright', max_length=100),
        ),
    ]
