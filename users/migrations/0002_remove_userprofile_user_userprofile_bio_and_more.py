# Generated by Django 5.0.2 on 2024-02-27 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default=11, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]