# Generated by Django 4.1.7 on 2023-03-05 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_alter_doctor_name_alter_patient_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Blood_Report_ID',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='RID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.treatment'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Name',
            field=models.CharField(default='Janet Pursley', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Name',
            field=models.CharField(default='Dale Healey', max_length=100),
        ),
    ]
