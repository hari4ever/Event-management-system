# Generated by Django 4.2.6 on 2023-11-23 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formApp', '0004_remove_mydata_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('ph_no', models.CharField(max_length=199)),
                ('email', models.CharField(max_length=199)),
                ('address', models.CharField(max_length=199)),
            ],
        ),
    ]
