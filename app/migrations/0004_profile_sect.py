# Generated by Django 4.2.6 on 2023-10-09 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_caste_fatherprofile_hobby_religion_sect_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sect',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='app.sect'),
        ),
    ]