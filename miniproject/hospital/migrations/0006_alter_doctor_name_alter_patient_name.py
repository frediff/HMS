# Generated by Django 4.1.7 on 2023-03-05 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_remove_patient_blood_report_id_alter_appointment_rid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Name',
            field=models.CharField(default='Latasha Bieker', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Name',
            field=models.CharField(default='Hugh Moreno', max_length=100),
        ),
    ]
