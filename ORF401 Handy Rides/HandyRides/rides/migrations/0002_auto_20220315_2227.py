# Generated by Django 3.1.6 on 2022-03-16 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='origination',
        ),
        migrations.AddField(
            model_name='person',
            name='blind',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='blood_type',
            field=models.CharField(default='Ukn', max_length=3),
        ),
        migrations.AddField(
            model_name='person',
            name='car_electric',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='car_make',
            field=models.CharField(default='Unknown', max_length=64),
        ),
        migrations.AddField(
            model_name='person',
            name='car_range',
            field=models.CharField(default='Unknown', max_length=64),
        ),
        migrations.AddField(
            model_name='person',
            name='convicted_felon',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='dnr_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(default='Unknown', max_length=64),
        ),
        migrations.AddField(
            model_name='person',
            name='kids',
            field=models.CharField(default='Unknown', max_length=64),
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='Unknown', max_length=64),
        ),
        migrations.AddField(
            model_name='person',
            name='origination_city',
            field=models.CharField(default='Unknown', max_length=64),
        ),
        migrations.AddField(
            model_name='person',
            name='origination_state',
            field=models.CharField(default='UK', max_length=2),
        ),
        migrations.AddField(
            model_name='person',
            name='pets',
            field=models.CharField(default='Unknown', max_length=64),
        ),
        migrations.AddField(
            model_name='person',
            name='prefered_music',
            field=models.CharField(default='Unknown', max_length=64),
        ),
        migrations.AddField(
            model_name='person',
            name='premium',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='smoker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='social',
            field=models.CharField(default='Unknown', max_length=64),
        ),
        migrations.AlterField(
            model_name='person',
            name='destination_city',
            field=models.CharField(default='Unknown', max_length=64),
        ),
        migrations.AlterField(
            model_name='person',
            name='destination_state',
            field=models.CharField(default='Unknown', max_length=2),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(default='Unknown', max_length=64),
        ),
    ]
