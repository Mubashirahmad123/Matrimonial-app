# Generated by Django 4.2.6 on 2023-10-16 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_profile_email_verification_token_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email_verification_token',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_email_verified',
        ),
    ]
