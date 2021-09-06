# Generated by Django 3.2.6 on 2021-08-19 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19', '0002_covidvaccinestatewise'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateWiseTestingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('state', models.CharField(max_length=100)),
                ('total_samples', models.IntegerField(null=True)),
                ('negative', models.IntegerField(null=True)),
                ('positive', models.IntegerField(null=True)),
            ],
        ),
    ]