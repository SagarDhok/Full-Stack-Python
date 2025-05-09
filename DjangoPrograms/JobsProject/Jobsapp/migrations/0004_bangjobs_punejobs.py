# Generated by Django 4.1 on 2025-04-22 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobsapp', '0003_alter_hydjobs_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bangjobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('eligibility', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Punejobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('eligibility', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
            ],
        ),
    ]
