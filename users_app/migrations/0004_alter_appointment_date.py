# Generated by Django 4.2.1 on 2023-06-24 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0003_service_category_alter_appointment_anything_else'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
