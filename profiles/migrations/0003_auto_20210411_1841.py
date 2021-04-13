# Generated by Django 3.1.7 on 2021-04-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_default_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_email',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]