# Generated by Django 4.1.7 on 2023-03-05 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_alter_doctor_name_alter_patient_blood_report_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Name',
            field=models.CharField(default='Timothy Casey', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Name',
            field=models.CharField(default='Lucille Simms', max_length=100),
        ),
    ]
