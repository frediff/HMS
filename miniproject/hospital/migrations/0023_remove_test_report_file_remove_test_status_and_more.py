# Generated by Django 4.1.7 on 2023-03-09 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0022_auto_20230306_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='Report_File',
        ),
        migrations.RemoveField(
            model_name='test',
            name='Status',
        ),
        migrations.AddField(
            model_name='test',
            name='Report',
            field=models.CharField(default='', max_length=4095),
        ),
    ]