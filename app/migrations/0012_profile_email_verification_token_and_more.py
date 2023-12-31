# Generated by Django 4.2.6 on 2023-10-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_profile_email_verification_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_verification_token',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
