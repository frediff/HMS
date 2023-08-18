# Generated by Django 4.1.7 on 2023-03-06 09:27

from django.db import migrations, models
import names


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_remove_user_username_alter_patient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=names.get_first_name, max_length=100),
        ),
    ]