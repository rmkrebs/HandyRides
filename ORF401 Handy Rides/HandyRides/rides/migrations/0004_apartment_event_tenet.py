# Generated by Django 3.1.6 on 2022-04-27 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0003_auto_20220316_0244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=64)),
                ('rent', models.IntegerField(default=0)),
                ('ac', models.BooleanField(default=False)),
                ('bedrooms', models.IntegerField(default=0)),
                ('bathrooms', models.IntegerField(default=0)),
                ('amenities', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=64)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('age_21_up', models.BooleanField(default=False)),
                ('byob', models.BooleanField(default=False)),
                ('entry_fee', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Tenet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('age_21_up', models.BooleanField(default=False)),
                ('job_industry', models.CharField(max_length=64)),
                ('university', models.CharField(max_length=64)),
                ('bio', models.CharField(max_length=250)),
                ('hobbies', models.CharField(max_length=64)),
            ],
        ),
    ]
