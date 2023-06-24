# Generated by Django 4.2.1 on 2023-06-22 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('breed', models.CharField(max_length=255)),
                ('coat_type', models.CharField(max_length=255)),
                ('weight', models.IntegerField()),
                ('dry_flakeyskin', models.BooleanField(default=False)),
                ('sheds', models.BooleanField(default=False)),
                ('ear_gunk', models.BooleanField(default=False)),
                ('sensitive_ears', models.BooleanField(default=False)),
                ('butt_dragger', models.BooleanField(default=False)),
                ('fleas', models.BooleanField(default=False)),
                ('anything_else', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('services', models.ManyToManyField(related_name='services', to='users_app.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='users_app.user')),
            ],
        ),
    ]
