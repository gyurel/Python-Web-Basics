# Generated by Django 4.0.1 on 2022-02-07 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_employee_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.CharField(choices=[('SoftUni', 'SoftUni'), ('Google', 'Google'), ('Facebook', 'Facebook')], max_length=8),
        ),
    ]
