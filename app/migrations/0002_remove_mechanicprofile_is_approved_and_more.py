# Generated by Django 4.2.4 on 2024-03-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mechanicprofile',
            name='is_approved',
        ),
        migrations.AddField(
            model_name='mechanicprofile',
            name='status',
            field=models.CharField(choices=[('approved', 'Approved'), ('pending', 'Pending')], default='pending', max_length=200),
        ),
    ]
