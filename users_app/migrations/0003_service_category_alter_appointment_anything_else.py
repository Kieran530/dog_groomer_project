# Generated by Django 4.2.1 on 2023-06-23 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.CharField(choices=[('wash', 'Wash'), ('left_add_on', 'Left Add-on'), ('right_add_on', 'Right Add-on')], default='wash', max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='anything_else',
            field=models.TextField(default=''),
        ),
    ]
