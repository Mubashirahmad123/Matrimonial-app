# Generated by Django 4.2.6 on 2023-10-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('occupation', models.CharField(max_length=100, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('is_married', models.BooleanField(default=False)),
            ],
        ),
    ]